MeterSphere 接口测试基于 JMeter 实现，因此 JMeter 中的内置函数及变量在 MeterSphere 中都可以正常使用。内置函数及变量可以用在多个位置，包括请求名称、请求参数、请求内容等。

内置函数一般以两个下划线开头，并使用类似 `${__functionName(var1,var2,var3)}` 的形式调用。

其中 `__functionName` 代表函数名，`var1`，`var2` 和 `var3` 分别是传给该函数的三个参数。

变量可以通过类似 `${varName}` 的形式引用，其中 `varName` 代表变量名。

## 内置函数列表

<table>
    <tbody>
        <tr>
            <th>函数类型</th>
            <th>函数名称</th>
            <th>函数说明</th>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__threadNum">threadNum</a></td>
            <td>get thread number</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__threadGroupName">threadGroupName</a></td>
            <td>get thread group name</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__samplerName">samplerName</a></td>
            <td>get the sampler name (label)</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__machineIP">machineIP</a></td>
            <td>get the local machine IP address</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__machineName">machineName</a></td>
            <td>get the local machine name</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__time">time</a></td>
            <td>return current time in various formats</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__timeShift">timeShift</a></td>
            <td>return a date in various formats with the specified amount of seconds/minutes/hours/days added</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__log">log</a></td>
            <td>log (or display) a message (and return the value)</td>
        </tr>
        <tr>
            <td>Information</td>
            <td> <a href="#__logn">logn</a></td>
            <td>log (or display) a message (empty return value)</td>
        </tr>
        <tr>
            <td>Input</td>
            <td> <a href="#__StringFromFile">StringFromFile</a></td>
            <td>read a line from a file</td>
        </tr>
        <tr>
            <td>Input</td>
            <td> <a href="#__FileToString">FileToString</a></td>
            <td>read an entire file</td>
        </tr>
        <tr>
            <td>Input</td>
            <td> <a href="#__CSVRead">CSVRead</a></td>
            <td>read from CSV delimited file</td>
        </tr>
        <tr>
            <td>Input</td>
            <td> <a href="#__XPath">XPath</a></td>
            <td>Use an XPath expression to read from a file</td>
        </tr>
        <tr>
            <td>Input</td>
            <td> <a href="#__StringToFile">StringToFile</a></td>
            <td>write a string to a file</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__counter">counter</a></td>
            <td>generate an incrementing number</td>
        </tr>
        <tr>
            <td>Formatting</td>
            <td> <a href="#__dateTimeConvert">dateTimeConvert</a></td>
            <td>Convert a date or time from source to target format</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__digest">digest</a></td>
            <td>Generate a digest (SHA-1, SHA-256, MD5...)</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__intSum">intSum</a></td>
            <td>add int numbers</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__longSum">longSum</a></td>
            <td>add long numbers</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__Random">Random</a></td>
            <td>generate a random number</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__RandomDate">RandomDate</a></td>
            <td>generate random date within a specific date range</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__RandomFromMultipleVars">RandomFromMultipleVars</a></td>
            <td>extracts an element from the values of a set of variables separated by <span class="code">|</span></td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__RandomString">RandomString</a></td>
            <td>generate a random string</td>
        </tr>
        <tr>
            <td>Calculation</td>
            <td> <a href="#__UUID">UUID</a></td>
            <td>generate a random type 4 UUID</td>
        </tr>
        <tr>
            <td>Scripting</td>
            <td> <a href="#__groovy">groovy</a></td>
            <td>run an Apache Groovy script</td>
        </tr>
        <tr>
            <td>Scripting</td>
            <td> <a href="#__BeanShell">BeanShell</a></td>
            <td>run a BeanShell script</td>
        </tr>
        <tr>
            <td>Scripting</td>
            <td> <a href="#__javaScript">javaScript</a></td>
            <td>process JavaScript (Nashorn)</td>
        </tr>
        <tr>
            <td>Scripting</td>
            <td> <a href="#__jexl2">jexl2</a></td>
            <td>evaluate a Commons Jexl2 expression</td>
        </tr>
        <tr>
            <td>Scripting</td>
            <td> <a href="#__jexl3">jexl3</a></td>
            <td>evaluate a Commons Jexl3 expression</td>
        </tr>
        <tr></tr>
        <td>Properties</td>
        <td> <a href="#__isPropDefined">isPropDefined</a> </td>
        <td>Test if a property exists</td>
        </tr>
        <tr>
            <td>Properties</td>
            <td> <a href="#__property">property</a> </td>
            <td>read a property</td>
        </tr>
        <tr>
            <td>Properties</td>
            <td> <a href="#__P">P</a></td>
            <td>read a property (shorthand method)</td>
        </tr>
        <tr>
            <td>Properties</td>
            <td> <a href="#__setProperty">setProperty</a></td>
            <td>set a JMeter property</td>
        </tr>
        <tr>
            <td>Variables</td>
            <td> <a href="#__split">split</a></td>
            <td>Split a string into variables</td>
        </tr>
        <tr>
            <td>Variables</td>
            <td> <a href="#__eval">eval</a></td>
            <td>evaluate a variable expression</td>
        </tr>
        <tr>
            <td>Variables</td>
            <td> <a href="#__evalVar">evalVar</a></td>
            <td>evaluate an expression stored in a variable</td>
        </tr>
        <tr>
            <td>Properties</td>
            <td> <a href="#__isVarDefined">isVarDefined</a> </td>
            <td>Test if a variable exists</td>
        </tr>
        <tr>
            <td>Variables</td>
            <td> <a href="#__V">V</a></td>
            <td>evaluate a variable name</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__char">char</a></td>
            <td>generate Unicode char values from a list of numbers</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__changeCase">changeCase</a></td>
            <td>Change case following different modes</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__escapeHtml">escapeHtml</a></td>
            <td>Encode strings using HTML encoding</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__escapeOroRegexpChars">escapeOroRegexpChars</a></td>
            <td>quote meta chars used by ORO regular expression</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__escapeXml">escapeXml</a></td>
            <td>Encode strings using XMl encoding</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__regexFunction">regexFunction</a></td>
            <td>parse previous response using a regular expression</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__unescape">unescape</a></td>
            <td>Process strings containing Java escapes (e.g. \n &amp; \t)</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__unescapeHtml">unescapeHtml</a></td>
            <td>Decode HTML-encoded strings</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__urldecode">urldecode</a></td>
            <td>Decode a application/x-www-form-urlencoded string</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__urlencode">urlencode</a></td>
            <td>Encode a string to a application/x-www-form-urlencoded string</td>
        </tr>
        <tr>
            <td>String</td>
            <td> <a href="#__TestPlanName">TestPlanName</a></td>
            <td>Return name of current test plan</td>
        </tr>
    </tbody>
</table>