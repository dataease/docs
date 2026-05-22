#!/usr/bin/env python3
"""
If version already exists in changelog.md, exit 0 without modification.
Usage: python .github/scripts/gen_changelog.py v4.10.9
"""
from __future__ import annotations
import sys, json, re, html, urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

API_URL = "https://community.fit2cloud.com/v1/products/dataease/releases"
CHANGELOG = Path('docs/changelog.md')
MARKER = '## 2 更新内容'
TZ = timezone(timedelta(hours=8))

TITLE_MAP = {
    '安全漏洞修复': ('Warning', '**安全漏洞修复**', 'fix'),
    '新增功能': ('Abstract', '新增功能 :star2:', 'feat'),
    '功能优化': ('Abstract', '功能优化 :sunflower:', 'refactor'),
    '问题修复': ('Abstract', '问题修复 :palm_tree:', 'fix'),
    "What's new": ('Abstract', '新增功能 :star2:', 'feat'),
    'Improvements': ('Abstract', '功能优化 :sunflower:', 'refactor'),
    'Bug fixes': ('Abstract', '问题修复 :palm_tree:', 'fix'),
}
H2_UL = re.compile(r'<h2><a[^>]*></a>([^<]+)</h2>\n?(<ul>.*?</ul>)', re.S)
# 【新增】用于抓取 h2 后面紧跟的 p 标签 (感谢信息)
# 逻辑：匹配 <h2>...</h2> 后面可能有的换行，然后匹配 <p>...</p>
H2_P_THANKS = re.compile(r'<h2><a[^>]*></a>[^<]*</h2>\n?(<p>.*?</p>)', re.S)
LI = re.compile(r'<li>(.*?)</li>', re.S)


def fetch():
    with urllib.request.urlopen(API_URL, timeout=30) as r:
        return json.loads(r.read().decode())


def normalize(v: str) -> str:
    return v.replace('-lts','')


def find_release(target: str, data):
    for rel in data:
        if normalize(rel.get('version','')) == target:
            return rel
    return None


def build_block(rel: dict):
    version = normalize(rel['version'])
    ts = rel.get('publishTime')
    dt = datetime.fromtimestamp(ts/1000, tz=TZ) if ts else datetime.now(tz=TZ)
    date_str = f"{dt.year}年{dt.month}月{dt.day}日"
    html_content = rel.get('releaseNoteH', '')
    sections = []

    for title, ul_html in H2_UL.findall(html_content):
        items = LI.findall(ul_html)
        cleaned = []
        for it in items:
            if not it.strip():
                continue
            # 处理 CVE 链接：将 <a href="url">CVE-XXX</a> 转换为 [(CVE-XXX)](url)
            def replace_cve_link(match):
                url = match.group(1)
                cve_text = html.unescape(re.sub(r'<[^>]+>', '', match.group(2)).strip())
                return f'[({cve_text})]({url})'
            # 先处理 CVE 链接
            processed = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', replace_cve_link, it)
            # 再清理其他 HTML 标签
            processed = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', processed)).strip())
            if processed:
                cleaned.append(processed)
        thanks_note = ""
        # 简单有效的正则：查找当前 title 对应的 h2 后面的 p
        # 构造动态正则： <h2>...Title...</h2> ... <ul>...</ul> ... <p>(内容)</p>
        # 由于 ul_html 内容可能很长且有特殊字符，直接用 title 定位最安全
        safe_title = re.escape(title.strip())
        # 正则解释：匹配包含 title 的 h2，后面任意字符(非贪婪)，然后匹配一个 <p>...</p>
        p_pattern = re.compile(r'<h2><a[^>]*></a>' + safe_title + r'</h2>.*?<p>(.*?)</p>', re.S)
        p_match = p_pattern.search(html_content)
        if p_match:
            p_content = p_match.group(1)
            # 清理 HTML 标签，只留文本
            clean_p = html.unescape(re.sub(r'<[^>]+>', '', p_content)).strip()
            # 只有当内容包含"感谢"或者标题包含"安全"/"漏洞"时，才采纳
            if "感谢" in clean_p and "漏洞" in title:
                thanks_note = f"\n    {clean_p}"
        if not cleaned:
            continue
        admon, nice, tag = TITLE_MAP.get(title, ('info', title, 'note'))
        lines = '\n'.join(f"    - {i}" for i in cleaned)
        if thanks_note:
            if lines:
                lines += "\n" + thanks_note
        sections.append(f"!!! {admon} \"{nice}\"\n\n{lines}\n")
    if not sections:
        clean = html.unescape(re.sub(r'<[^>]+>','', html_content)).strip()
        if clean:
            sections.append(f"!!! info \"发布说明\"\n    - note: {clean}\n")
    block = '\n'.join([f"### {version}", date_str, ''] + sections)
    return block


def main():
    if len(sys.argv) < 2:
        print('Version arg required, e.g. v2.10.1 or v2.10.1-lts or 2.10.1', file=sys.stderr)
        return 1
    raw = sys.argv[1].strip()
    # Accept forms: v2.10.1 or v2.10.1-lts or 2.10.1
    if not raw.startswith('v'):
        raw = 'v' + raw
    target = normalize(raw)  # remove -lts suffix if present
    data = fetch()
    rel = find_release(target, data)
    if not rel:
        print(f'Target version {raw} (normalized {target}) not found in API list', file=sys.stderr)
        return 1
    if not CHANGELOG.exists():
        print('Changelog file missing.')
        return 1
    content = CHANGELOG.read_text(encoding='utf-8')
    # 【修复】使用正则严格匹配 Markdown 标题行 (例如: ### v2.10.19)
    # ^ 表示行首，#+ 表示一个或多个#，\s* 表示可选空格，re.escape 防止版本号中的点被当作通配符
    pattern = re.compile(r'^#+\s*' + re.escape(target) + r'\s*$', re.MULTILINE)

    if pattern.search(content):
        print(f'⚠️ Version {target} already exists in changelog.md (Detected by regex). Skip.')
        return 0
    block = build_block(rel)
    if MARKER in content:
        new_content = content.replace(MARKER, MARKER + '\n\n' + block, 1)
    else:
        new_content = MARKER + '\n\n' + block + content
    CHANGELOG.write_text(new_content, encoding='utf-8')
    print('Inserted changelog for', target)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
