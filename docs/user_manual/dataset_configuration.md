# 权限矩阵

<table>
    <colgroup>
        <col>
        <col>
        <col>
        <col>
        <col>
        <col>
        <col>
        <col>
        <col>
        <col>
    </colgroup>
    <tbody>
        <tr>
            <td>一级功能</td>
            <td>二级功能</td>
            <td>三级功能</td>
            <td>具体用例</td>
            <td>系统管理员</td>
            <td>组织管理员</td>
            <td>工作空间管理员</td>
            <td>工作空间用户</td>
            <td>工作空间只读用户</td>
            <td colspan="1">无角色用户</td>
        </tr>
        <tr>
            <td rowspan="43">系统管理</td>
            <td rowspan="26">系统</td>
            <td rowspan="5">用户管理</td>
            <td>列出系统中的所有用户</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>指定用户&nbsp;ID、用户名、邮箱、电话、密码等信息创建新用户</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定用户的用户名、邮箱、电话、密码等信息</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>删除指定用户</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>启用、禁用指定用户，用户禁用后无法登录系统</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">组织管理</td>
            <td>列出系统中的所有组织</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>指定组织名称、描述等信息创建新组织</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定组织的名称、描述等信息</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>删除指定组织</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">组织成员管理</td>
            <td>列出该组织中的所有成员及其角色信息</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择系统中已有用户并指定组织级角色添加至组织成员</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定成员在该组织中的角色</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>从组织中删除指定成员（去除角色信息）</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">工作空间管理</td>
            <td>列出系统中的所有工作空间</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>指定工作空间名称、描述及所属组织等信息创建新工作空间</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定工作空间的名称、描述及所属组织等信息</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>删除指定工作空间</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">工作空间成员管理</td>
            <td>列出该工作空间中的所有成员及其角色信息</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择系统中已有用户并指定工作空间级角色添加至工作空间成员</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定成员在该工作空间中的角色</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>从工作空间中删除指定成员（去除角色信息）</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">测试资源池管理</td>
            <td>列出系统中的所有测试资源池</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>指定测试资源池名称、具体配置等信息创建新测试资源池</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定测试资源池的名称、具体等信息</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>删除指定测试资源池</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>系统设置</td>
            <td>配置&nbsp;SMTP&nbsp;信息</td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="12">组织</td>
            <td rowspan="4">组织成员管理</td>
            <td>列出该组织中的所有成员及其角色信息</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择系统中已有用户并指定组织级角色添加至组织成员</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定成员在该组织中的角色</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>从组织中删除指定成员（去除角色信息）</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">组织下工作空间管理</td>
            <td>列出系统中的所有工作空间</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>指定工作空间名称、描述及所属组织等信息创建新工作空间</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定工作空间的名称、描述及所属组织等信息</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>删除指定工作空间</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">组织下工作空间成员管理</td>
            <td>列出该工作空间中的所有成员及其角色信息</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择系统中已有用户并指定工作空间级角色添加至工作空间成员</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定成员在该工作空间中的角色</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>从工作空间中删除指定成员（去除角色信息）</td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">工作空间</td>
            <td rowspan="4">工作空间成员管理</td>
            <td>列出该工作空间中的所有成员及其角色信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择系统中已有用户并指定工作空间级角色添加至工作空间成员</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定成员在该工作空间中的角色</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>从工作空间中删除指定成员（去除角色信息）</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td><br></td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>个人信息</td>
            <td>个人设置</td>
            <td>修改自己的用户名、邮箱、电话、密码等信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1">Y</td>
        </tr>
        <tr>
            <td rowspan="23">测试跟踪</td>
            <td>首页</td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="5">项目</td>
            <td rowspan="5">项目</td>
            <td>列出当前工作空间中的所有项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>指定项目名称、描述等信息，在当前工作空间创建新项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>修改指定项目的名称、描述等信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>删除指定项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>在项目列表中点击项目名称，进入该项目下的测试用例页面</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="9">测试用例</td>
            <td rowspan="4">测试用例树</td>
            <td>以树状形式展示项目的模块及子模块</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>在用例树中的任一节点均可创建该节点的子节点，用例树最多支持&nbsp;5&nbsp;级子节点</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>通过前端拖拽的方式移动用例树的某个节点到指定位置</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>从用例树中删除某个节点，该节点及其子节点下下的所有用例，移动到名为‘未归类用例&nbsp;’的虚拟1&nbsp;级节点</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="5">测试用例管理</td>
            <td>以列表形式展示当前选中的用例树某节点下的所有用例</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>在当前选中的用例树节点下，新建测试用例；测试用例信息包含用例名称、所属模块、优先级、执行步骤等信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>删除指定的测试用例</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择某个测试用例，编辑修改测试用例相关信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择某个测试用例，编辑修改测试用例维护人信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="8">测试计划</td>
            <td rowspan="3">测试计划列表</td>
            <td>以列表形式展示当前工作空间中所有项目下的所有测试计划</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>指定测试计划的名称、描述、所属项目等信息创建测试计划</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择某个测试计划，编辑修改测试计划相关信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="5">测试计划中的用例管理</td>
            <td>从该测试计划所属项目中，选择用例树节点或具体用例，添加到该测试计划，并指定该用例的执行人等信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>以只读的形式展示当前已添加到测试计划中的用例树</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>以列表形式展示当前选中的用例树某节点下的所有用例</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择测试计划中的某个测试用例，编辑修改执行人等相关信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>选择测试计划中的某个测试用例，编辑修改执行结果等相关信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="15">接口测试</td>
            <td rowspan="5">项目</td>
            <td><br></td>
            <td>列出当前工作空间中的所有项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>指定项目名称、描述等信息，在当前工作空间创建新项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>修改指定项目的名称、描述等信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>删除指定项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>在项目列表中点击项目名称，进入该项目下的接口管理页面</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td>接口</td>
            <td><br></td>
            <td>TBD</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="5">测试</td>
            <td><br></td>
            <td>以列表形式展示当前工作空间中所有项目下的所有接口测试</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>点击创建测试按钮，选择测试所属项目，填写测试的具体配置信息并保存测试</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>删除指定的接口测试</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择某个接口测试，查看并编辑修改该接口测试具体信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>仅查看</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择某个接口测试执行该测试，测试开始执行后自动跳转到该次执行产生的测试报告</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">报告</td>
            <td><br></td>
            <td>以列表形式展示当前工作空间中所有项目下的所有测试报告</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>删除指定的测试报告</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择某个测试报告，查看测试报告详细内容</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择多个测试报告对比查看测试报告内容</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="13">性能测试</td>
            <td rowspan="4">项目</td>
            <td><br></td>
            <td>列出当前工作空间中的所有项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>指定项目名称、描述等信息，在当前工作空间创建新项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>修改指定项目的名称、描述等信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>删除指定项目</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="5">测试</td>
            <td><br></td>
            <td>以列表形式展示当前工作空间中所有项目下的所有性能测试</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>点击创建测试按钮，选择测试所属项目，填写测试的具体配置信息并保存测试</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>删除指定的性能测试</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择某个性能测试，查看并编辑修改该性能测试具体信息</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>仅查看</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择某个性能测试执行该测试，测试开始执行后自动跳转到该次执行产生的测试报告</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td rowspan="4">报告</td>
            <td><br></td>
            <td>以列表形式展示当前工作空间中所有项目下的所有测试报告</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>删除指定的测试报告</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td><br></td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择某个测试报告，查看测试报告详细内容</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
        <tr>
            <td><br></td>
            <td>选择多个测试报告对比查看测试报告内容</td>
            <td><br></td>
            <td><br></td>
            <td>Y</td>
            <td>Y</td>
            <td>Y</td>
            <td colspan="1"><br></td>
        </tr>
    </tbody>
</table>