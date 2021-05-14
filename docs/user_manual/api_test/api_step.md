## 单接口用例步骤

### 前置脚本
前置脚本可以添加为请求的子步骤，在请求发送前执行，可以用在修改请求内容、初始化请求需要的参数值等场景。

目前 MeterSphere 支持以下几种语言的前置脚本：

- BeanShell
- Groovy
- Python2
- JavaScript

与 JMeter 一样，脚本在加载前已经内置了部分变量，在脚本中可以直接使用这些变量。

- `log` - [Logger]，用于在脚本执行过程中打印日志
```
//打印 `Hello World!` 到 info 日志中
log.info("Hello World!");
```
- `Label` - 前置脚本所属请求的请求名称
- `SampleResult` - 当前请求请求结果 [SamplerResult]() 的指针
```
//设置请求结果成功或失败
SampleResult.setSuccessful(true/false);
//设置请求返回码
SampleResult.setResponseCode("code");
//设置请求返回消息
SampleResult.setResponseMessage("message");
```
- `sampler` - 当前请求 [sampler]() 的指针
```
//获取当前请求名称
sampler.getName();
```
- `vars` - [JMeterVariables]()，用于操作变量
```
//获取变量 VAR1 的值
vars.get("VAR1");
//设置变量 VAR2 的值为 value
vars.put("VAR2","value");
//移除变量 VAR3
vars.remove("VAR3");
```

!!! info "说明"
    不同脚本语言语法不同，以上示例仅针对 BeanShell 或 Groovy。

### 后置脚本
后置脚本与前置脚本类似，可以添加为请求的子步骤，在请求发送后执行，可以用于处理响应结果，从中提取变量等场景。

### 断言规则
断言的主要功能是通过验证响应报文是否满足需求规约来验证接口运行是否正确。

![!断言界面](../../img/api/断言界面.png)

!!! info "界面说明"
    1. 断言方式选择
    2. 断言配置区域，根据选择的断言方式不同，展示不同的配置内容
    3. 是否忽略结果状态选项，例如希望进行返回码为 401 的断言时，需要勾选该选项，否则请求仍会被视为失败状态。
    4. 添加断言按钮，在同一个断言步骤内可以添加多条断言，断言编辑完成后需要点击 `添加` 按钮进行添加。
    5. 保存按钮，保存当前断言规则步骤内容。
    6. 推荐 JSONPath 断言，当请求的响应体是 JSON 格式时，可以使用该功能辅助生成 JSONPath 断言。
    7. 清空 JSONPath 断言，清空自动添加的 JSONPath 断言。

目前 MeterSphere 支持以下几种形式的断言规则：

- 正则
- JSONPath
- XPath
- 响应时间
- 脚本

#### 正则断言
正则断言较为灵活，适用于请求的响应内容不是 JSON、XML、HTML 等这样的标准且常见的结构化文本时。
![!正则断言](../../img/api/正则断言.png)

!!! info "参数说明"
    1. **对象**：希望进行断言的对象，支持选择 `Response Code`，`Response Headers`，`Response Data`
    2. **Perl型正则表达式**：断言对象需要匹配的正则表达式，匹配成功则断言成功，否则断言失败。

!!! warn "示例"
    **请求的响应体**：
    ```
    id="ddc86657-d402-4c10-b458-2ba2e4604cef"&name="myorg"&description="test org"
    ```
    **断言需求**：判断响应体中包含 `name="任意文本"`。

    **断言配置**：

    - **对象**：`Response Data`
    - **Perl型正则表达式**：`name=".*?"`

#### JSONPath 断言
JSONPath 断言适用于请求的响应内容是 JSON 格式时，可以方便的通过 [JSONPath 表达式]() 定位到特定字段，设定其期望值。
![!JSONPath断言](../../img/api/JSONPath断言.png)

!!! info "参数说明"
    1. **JSONPath表达式**：JSONPath 表达式，通过该表达式定位到特定字段。
    2. **期望值**：通过 JSONPath 表达式定位的字段的期望值，支持正则表达式。

!!! warn "示例"
    **请求的响应体**：
    ```json
    {
        "success": true,
        "message": null,
        "data": {
            "id": "ddc86657-d402-4c10-b458-2ba2e4604cef",
            "name": "myorg",
            "description": "form api",
            "createTime": 1611154807818,
            "updateTime": 1611154807818
        }
    }
    ```
    **断言需求**：判断响应体 `data` 中的 `name` 字段值为 `myorg`
    
    **断言配置**：

        - **JSONPath 表达式**：$.data.name
        - **期望值**：myorg

#### XPath 断言
XPath 断言适用于请求的响应内容是 XML、HTML 等格式时，可以方便的通过 [XPath 表达式]() 定位到特定字段，设定其期望值。
![!XPath断言](../../img/api/XPath断言.png)

!!! info "参数说明"
    1. **XPath表达式**：需要进行匹配的 XPath 表达式

!!! warn "示例"
    **请求的响应体**：
    ```xml
    <root xmlns:foo="http://www.foo.org/" xmlns:bar="http://www.bar.org">
        <employees>
            <employee id="1">Johnny Dapp</employee>
            <employee id="2">Al Pacino</employee>
            <employee id="3">Robert De Niro</employee>
            <employee id="4">Kevin Spacey</employee>
            <employee id="5">Denzel Washington</employee>
        </employees>
        <foo:companies>
            <foo:company id="6">Tata Consultancy Services</foo:company>
            <foo:company id="7">Wipro</foo:company>
            <foo:company id="8">Infosys</foo:company>
            <foo:company id="9">Microsoft</foo:company>
            <foo:company id="10">IBM</foo:company>
            <foo:company id="11">Apple</foo:company>
            <foo:company id="12">Oracle</foo:company>
        </foo:companies>
    </root>
    ```
    **断言需求**：判断响应体中的 id 为 10 的公司名称为 `IBM`

    **断言配置**：

        - **XPath 表达式**：//foo:company[@id=10]='IBM'

#### 响应时间断言
响应时间断言适用于对请求的响应时间有特定要求时。
![!响应时间断言](../../img/api/响应时间断言.png)

!!! info "参数说明"
    1. **响应时间在...毫秒以内**：以毫秒为单位的响应时间期望，当实际响应时间小于等于该值时断言成功。

#### 脚本断言
脚本断言提供了更加强大、灵活的处理能力，通过可以根据自身需求选择合适的语言编写脚本来设定断言结果，适用于常规断言无法满足需求时。
![!脚本断言](../../img/api/脚本断言.png)

!!! info "参数说明"
    1. **编辑按钮**：点击弹出脚本断言编辑页面。、
    2. **添加按钮**：脚本编辑完成后，点击添加到断言列表中。
    3. **脚本生成工具**：针对简单的变量值判断的脚本，可以通过该工具快速生成脚本。
    4. **脚本名称**：断言脚本的名称。
    5. **脚本内容**：断言脚本内容。
    6. **语言切换及代码模板**：切换脚本语言，与前后置脚本一样，目前支持 `BeanShell`、`Groovy`、`Python` 及 `JavaScript` 脚本语言。

与前后置脚本一样，脚本在加载前已经内置了部分变量，除了在之前已经介绍过的变量外，脚本断言中的脚本还额外提供了以下变量。

- `AssertionResult` - 断言结果对象，可以通过 `AssertionResult.setFailure(true)` 方法设置断言是否成功，通过 `AssertionResult.setFailureMessage("message")` 方法设置断言失败提示信息。

### 提取参数
参数提取功能主要用于从请求响应中提取特定返回值并存储到变量中，便于在后续的步骤中引用该返回值。
![!提取参数界面](../../img/api/提取参数界面.png)

!!! info "界面说明"
    1. 提取方式选择
    2. 提取参数区域，根据选择的提取方式不同，展示不同的配置内容
    3. 是否提取多个匹配结果，例如当匹配到多个值时，可以返回 `varName_n` 形式的多个变量。
    4. 添加提取规则按钮，在同一个提取参数步骤内可以添加多条提取规则，提取规则编辑完成后需要点击 `添加` 按钮进行添加。
    5. 保存按钮，保存当前提取参数步骤内容。
    6. 推荐JSONPath提取，当请求的响应体是 JSON 格式时，可以使用该功能辅助生成 JSONPath 提取规则。
    7. 清空JSONPath提取，清空自动添加的 JSONPath 提取规则。

目前 MeterSphere 支持以下几种形式的提取方式：

- 正则
- JSONPath
- XPath

#### 正则提取
正则提取较为灵活，适用于请求的响应内容不是 JSON、XML、HTML 等这样的标准且常见的结构化文本时。
![!正则提取](../../img/api/正则提取.png)

!!! info "参数说明"
    1. **对象**：希望进行提取的对象，支持选择 `Body`，`Request Headers`，`Response Headers`，`URL`，`Response Code`，`Response Message` 等对象。
    2. **变量名**：保存提取值的变量名，后续可以通过 `${varName}` 形式引用到，如果选择了匹配多个，可以通过 `${varName_#}` 获取到匹配的总个数，通过 `${varName_n}` 依次获取到每个匹配值。
    2. **Perl型正则表达式**：提取特定值使用的正则表达式，将提取正则表达式中的第一个组。

!!! warn "示例"
    **请求的响应体**：
    ```
    id="ddc86657-d402-4c10-b458-2ba2e4604cef"&name="myorg"&description="test org"
    ```
    **提取需求1**：响应体中 `name` 字段的值。

    **提取配置**：

    - **对象**：`Body`
    - **变量名**：name
    - **Perl型正则表达式**：`name="(.*?)"`

#### JSONPath 提取
JSONPath 提取适用于请求的响应内容是 JSON 格式时，可以方便的通过 [JSONPath 表达式]() 定位到特定字段进行提取。
![!JSONPath提取](../../img/api/JSONPath提取.png)

!!! info "参数说明"
    1. **变量名**：保存提取值的变量名，后续可以通过 `${varName}` 形式引用到，如果选择了匹配多个，可以通过 `${varName_#}` 获取到匹配的总个数，通过 `${varName_n}` 依次获取到每个匹配值。
    2. **JSONPath表达式**：JSONPath 表达式，通过该表达式定位到要提取的字段。

!!! warn "示例"
    **请求的响应体**：
    ```json
    {
        "success": true,
        "message": null,
        "data": {
            "id": "ddc86657-d402-4c10-b458-2ba2e4604cef",
            "name": "myorg",
            "description": "form api",
            "createTime": 1611154807818,
            "updateTime": 1611154807818
        }
    }
    ```
    **提取需求**：提取响应体 `data` 中的 `name` 字段并存储在 `name` 变量中。
    
    **提取配置**：
    
    - **变量名**：name
    - **JSONPath 表达式**：$.data.name

#### XPath 提取
XPath 提取适用于请求的响应内容是 XML、HTML 等格式时，可以方便的通过 [XPath 表达式]() 定位到特定字段进行提取。
![!XPath提取](../../img/api/XPath提取.png)

!!! info "参数说明"
    1. **变量名**：保存提取值的变量名，后续可以通过 `${varName}` 形式引用到，如果选择了匹配多个，可以通过 `${varName_#}` 获取到匹配的总个数，通过 `${varName_n}` 依次获取到每个匹配值。
    1. **XPath表达式**：需要进行匹配的 XPath 表达式

!!! warn "示例"
    **请求的响应体**：
    ```xml
    <root xmlns:foo="http://www.foo.org/" xmlns:bar="http://www.bar.org">
        <employees>
            <employee id="1">Johnny Dapp</employee>
            <employee id="2">Al Pacino</employee>
            <employee id="3">Robert De Niro</employee>
            <employee id="4">Kevin Spacey</employee>
            <employee id="5">Denzel Washington</employee>
        </employees>
        <foo:companies>
            <foo:company id="6">Tata Consultancy Services</foo:company>
            <foo:company id="7">Wipro</foo:company>
            <foo:company id="8">Infosys</foo:company>
            <foo:company id="9">Microsoft</foo:company>
            <foo:company id="10">IBM</foo:company>
            <foo:company id="11">Apple</foo:company>
            <foo:company id="12">Oracle</foo:company>
        </foo:companies>
    </root>
    ```
    **提取需求**：提取响应体中的 `id` 为 3 的员工的姓名，即上述响应中的 `Robert De Niro`，并存储在 `employeeName` 变量中。

    **提取配置**：

    - **变量名**：employeeName
    - **XPath 表达式**：string(//employee[@id='3'])

## 场景用例步骤

### 接口列表导入
通过接口列表导入功能，可以直接添加接口定义功能中已维护好的接口或接口下的用例，减少重复填写接口请求参数的情况。

#### 导入接口
![!导入接口](../../img/api/导入接口.gif)

#### 导入用例
![!导入用例](../../img/api/导入用例.gif)

!!! info "说明"
    导入用例时提供 `复制` 和 `引用` 两种方式。通过 `复制` 方式导入的用例，当原用例发生变化时，场景中导入的用例不会改变；通过 `引用` 方式导入的用例，当原用例发生变化时，场景中导入的用例也会随之改变。

### 自定义请求
通过添加自定义请求，用户可以自由编辑该请求的详细信息，该请求不需要事先存在于接口定义中。目前支持 HTTP、TCP、DUBBO、SQL 等不同类型的请求。
![!添加自定义请求](../../img/api/添加自定义请求.gif)

### 自定义脚本
自定义脚本与前后置脚本使用方式类似，但是可以独立添加，不需要依赖于某个已有请求作为其子步骤。目前支持的脚本语言及内置变量请参考 [前置脚本](#_2)。
![!添加自定义脚本](../../img/api/添加自定义脚本.gif)

### 场景导入
用户可以维护一些基础、通用场景，通过场景导入功能，可以直接将已有的场景添加到当前场景中，减少重复工作，提高场景的复用性。
![!场景导入](../../img/api/场景导入.gif)

!!! info "说明"
    导入场景时提供 `复制` 和 `引用` 两种方式。通过 `复制` 方式导入的场景，当原场景发生变化时，场景中导入的场景不会改变；通过 `引用` 方式导入的场景，当原场景发生变化时，场景中导入的场景也会随之改变。

### 条件控制器
当条件控制器中配置的条件满足时，条件控制器下的子步骤才会执行，否则子步骤会被跳过。
![!添加条件控制器](../../img/api/添加条件控制器.gif)

### 循环控制器
通过使用循环控制器，可以重复执行循环控制器下的子步骤，目前 MeterSphere 提供了 `次数循环`、`ForEach 循环` 和 `While 循环` 三种循环方式。
![!添加循环控制器](../../img/api/添加循环控制器.gif)

#### 次数循环
![!次数循环](../../img/api/次数循环.png)

!!! info "参数说明"
    1. **循环次数**：该循环控制器下的子步骤总共执行的次数。
    2. **循环间隔**：每次执行间的时间间隔，以毫秒为单位。
    3. **成功后是否继续循环**：仅循环控制器下存在一个请求时可以关闭。当关闭时，若循环控制器下的请求是成功状态，则立即终止循环，无论有没有达到循环次数。可以用在异步请求后轮询查询执行结果的场景，当查询结果符合预期时终止循环，避免多余的查询操作。

!!! info "示例"
    开启 `成功后继续循环`，循环总共执行了 5 次。
    ![!开启成功后继续循环](../../img/api/开启成功后继续循环.png)
    
    关闭 `成功后继续循环`，由于循环下的请求第一次便执行成功，循环仅执行了 1 次。
    ![!关闭成功后继续循环](../../img/api/关闭成功后继续循环.png)

#### ForEach 循环
ForEach 循环一般配合列表变量使用，例如存在 `ID_1`，`ID_2`，`ID_3` 形式的一组变量时，可以通过 ForEach 循环使用其中每个 ID 发送特定请求。
![!ForEach循环](../../img/api/ForEach循环.png)

!!! info "参数说明"
    1. **输出变量名称**：在循环中可以通过该变量引用到列表变量中当前迭代的变量值。
    2. **输入变量前缀**：列表变量的变量前缀。
    3. **循环间隔**：每次执行间的时间间隔，以毫秒为单位。

!!! info "示例"
    TBD

#### While 循环
While 循环更为灵活，当配置的条件满足时循环会一直进行。
![!While循环](../../img/api/While循环.png)

!!! info "参数说明"
    1. **变量**：要进行判断的变量。
    2. **判断条件**：变量与期望值的比较方式。
    3. **值**：要对变量进行判断的值。
    4. **循环超时时间**：由于 while 循环的特殊性，当条件满足时将会一直循环，为了避免死循环的情况出现，用户可以配置循环超时时间，到超过该事件后，不管循环条件是否满足，循环都将被终止。

!!! info "示例"
    TBD

### 等待控制器
当某个步骤执行后需要等待一段时间时使用。作为某个步骤的子步骤添加时，该步骤将等待若干时间后再执行；当作为上级步骤添加时，与之同级的所有步骤均会等待若干时间。
![!添加等待控制器](../../img/api/添加等待控制器.gif)

### 前置脚本
与单接口用例步骤中的前置脚本类似，请参考 [前置脚本](#_2)

### 后置脚本
与单接口用例步骤中的后置脚本类似，请参考 [后置脚本](#_3)

### 断言规则
与单接口用例步骤中的断言规则类似，请参考 [断言规则](#_4)

### 提取参数
与单接口用例步骤中的提取参数类似，请参考 [提取参数](#_8)

