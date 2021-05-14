
[Apache JMeter](https://jmeter.apache.org/) 是一个 Java 语言编写的开源性能测试工具，是目前最主流的开源性能测试工具。本资源集源自 [awesome-jmeter](https://github.com/aliesbelik/awesome-jmeter)，MeterSphere 团队针对国内用户进行了汉化、优化和进一步整理。

## 官方资源

- [Apache JMeter Project](https://jmeter.apache.org/) - Apache JMeter 官方网站
- [GitHub Repository](https://github.com/apache/jmeter) - Apache JMeter GitHub 代码库
- [JMeter Wiki](https://cwiki.apache.org/confluence/display/jmeter) - Apache JMeter 官方文档
- [Issue Tracking](https://jmeter.apache.org/issues.html) - Apache JMeter 缺陷跟踪系统
- [Mailing Lists](https://jmeter.apache.org//mail2.html) - Apache JMeter 邮件列表

## 下载安装

- [下载 Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi) - Apache JMeter: 官方下载

## 快速入门

- [The Beginner's Guide to Performance Testing with Apache JMeter](https://medium.com/better-programming/the-beginners-guide-to-performance-testing-with-apache-jmeter-5cc52c327ff6)

## 使用教程

- [JMeter Tutorials](https://artoftesting.com/jmeter-tutorial)
- [JMeter Tutorial for Load Testing: The Ultimate Guide](https://www.javacodegeeks.com/2014/11/jmeter-tutorial-load-testing.html)
- [RESTful API testing with JMeter](https://www.ibm.com/developerworks/cloud/library/cl-jmeter-restful/)
- [JMeter Tutorial](https://www.guru99.com/jmeter-tutorials.html) - By Guru99

## 最佳实践

- [JMeter 最佳实践 - 官方](https://jmeter.apache.org/usermanual/best-practices.html)
- [JMeter 最佳实践 - BlazeMeter](https://guide.blazemeter.com/hc/en-us/articles/207421405-JMeter-Best-Practices)
- [Concurrent, High Throughput Performance Testing with JMeter](https://planet.jboss.org/post/concurrent_high_throughput_performance_testing_with_jmeter)

## Scripting

- [Beanshell vs JSR223 vs Java JMeter Scripting](https://www.blazemeter.com/blog/beanshell-vs-jsr223-vs-java-jmeter-scripting-its-performance/) - Most popular scripting mechanisms performance comparison.
- [Testing with Groovy](https://static.packt-cdn.com/downloads/Testingwithgroovy.pdf) - Using JMeter and Groovy for load testing.

## 持续集成

- [JMeter Ant Task](https://github.com/jfifield/ant-jmeter) - Ant task to automate running JMeter test plans.
- [JMeter Maven Plugin](https://github.com/jmeter-maven-plugin/jmeter-maven-plugin) - Maven plugin that provides the ability to run JMeter tests as part of the build.
- [Jenkins Performance Plugin](https://plugins.jenkins.io/performance/) - Jenkins plugin to capture reports from JMeter and generate graphic charts with the trend report of performance and robustness.
- [Sonar JMeter Plugin](https://github.com/SonarQubeCommunity/sonar-jmeter) - Plugin to collect JMeter performance tests results and display in Sonar dashboard *(deprecated)*.

## 分布式测试

- [JMeter Distributed Testing Step-by-step](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.pdf)
- [JMeter Remote Testing](https://jmeter.apache.org/usermanual/remote-test.html)
- [Setting up a JMeter Cluster for web server load testing](https://www.howtoforge.com/setting-up-jmeter-cluster-for-load-testing/)

## 容器化

- [Dockerized JMeter](https://gist.github.com/hhcordero/abd1dcaf6654cfe51d0b) - Distributed load testing workflow with Docker and JMeter.
- [JMeter Docker Images](https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=0&q=jmeter&starCount=0)
- [Distributed JMeter testing using Docker](http://srivaths.blogspot.com/2014/08/distrubuted-jmeter-testing-using-docker.html)
- [A Docker solution to JMeter + InfluxDB + Grafana performance testing](https://medium.com/@ellenhuang523/a-docker-solution-to-jmeter-influxdb-grafana-performance-testing-568848de7a0f)
- [AutoMeter](https://github.com/intuit/autometer) - An automation tool for scaling load tests using distributed slaves, based on JMeter master-slave architecture.

## 与公有云集成

- Amazon Web Services
    - [jmeter-ec2](https://github.com/oliverlloyd/jmeter-ec2/) - Automates running Apache JMeter on Amazon EC2.
    - [gee](https://github.com/kowalcj0/gee) - A modified version of JMeter-EC2 project.
    - [os-jmeter-aws](https://github.com/OrdnanceSurvey/os-jmeter-aws) - Run JMeter on multiple AWS instances, view results in ELK.
    - [Load Testing with JMeter and Amazon EC2](https://medium.com/@alttaf/load-testing-with-jmeter-and-amazon-ec2-e143a7350596)
    - [Performance Testing in the Cloud with JMeter & AWS](http://web.archive.org/web/20190526033436/http://www.artofsoftwaredevelopment.com/performance/performance-testing-in-the-cloud-with-jmeter-aws)
    - [JMeter distributed testing with Amazon EC2](https://vedovini.net/2009/08/17/jmeter-distributed-testing-with-amazon-ec2/)
- Microsoft Azure
    - [Load Testing Pipeline with JMeter, ACI and Terraform](https://github.com/Azure-Samples/jmeter-aci-terraform) - Scalable cloud load/stress testing pipeline solution with Apache JMeter and Terraform to dynamically provision and destroy the required infrastructure on Azure.

## 结果处理和可视化

- [JMeter Report Dashboard](https://jmeter.apache.org/usermanual/generating-dashboard.html) - JMeter supports dashboard report generation to get graphs and statistics from a test plan.
- [JMeter Log Analysis](https://cwiki.apache.org/confluence/display/jmeter/LogAnalysis) - Suggestions and recipes for JMeter log analysis.
- [Analyzing JMeter Results](http://www.datazoo.de/articles/158/performance-testing-analyzing-jmeter-results)
- [JMeter Result Analysis: The Ultimate Guide](https://octoperf.com/blog/2017/10/19/how-to-analyze-jmeter-results/)
- [BlazeMeter Sense](https://sense.blazemeter.com/) - Service for storing and analysing performance test results.
- [JAnalyser](http://janalyser.com/) - Browser-based results analysis tool.
- [JMeter Result Analysis Plugin](https://github.com/afranken/jmeter-analysis-maven-plugin) - Maven plugin that parses JMeter test results and generates detailed reports with charts.
- [JMeter Results Analyser](https://sourceforge.net/projects/jmstats/) - Web-based application for collating, analysing and reporting JMeter test results.
- DB Results Collectors
    - [JMeter MySQLCollector Plugin](https://cwiki.apache.org/confluence/display/jmeter/MysqlCollectorPlugin) - Patch to configure listener to log into MySQL database.
- InfluxDB & Grafana
    - [Using JMeter with InfluxDB & Grafana](https://www.vinsguru.com/category/influxdb/) - Collection of guides to collect and visualize real-time test-results and server monitoring stats using InfluxDB & Grafana.
    - [How to Use Grafana to Monitor JMeter Non-GUI Results](https://dzone.com/articles/how-to-use-grafana-to-monitor-jmeter-non-gui-resul)
    - Grafana Dashboards
      - [JMeter Load Test Dashboard](https://grafana.com/grafana/dashboards/1152) - Grafana dashboard shows live load test metrics provided by JMeter (by NovaTec-APM).
      - [JMeter Dashboard using Core InfluxdbBackendListenerClient](https://grafana.com/grafana/dashboards/5496) - Monitor your Apache JMeter load test in real time with InfluxDB and Grafana (by Philippe M).
      - [JMeter Dashboard (3.2 and up)](https://grafana.com/grafana/dashboards/3351) - Monitor JMeter load test in real time with InfluxDB and Grafana (by adrianbanu).
      - [JMeter (via prometheus exporter)](https://grafana.com/grafana/dashboards/2492) - A Grafana dashboard to inspect JMeter metrics via Prometheus exporter (by chiabre).
    - [JMeter-InfluxBD-Writer Plugin](https://github.com/NovatecConsulting/JMeter-InfluxDB-Writer) - JMeter plugin to write load test data on-the-fly into InfluxDB.
    - [JMeter Results to InfluxDB](https://github.com/soprasteria/jmeter2influxdb) - Read JMeter results from csv file and put into InfluxDB database.
- ELK Stack
    - [Using ELK](http://ecmarchitect.com/archives/2014/09/09/3932) - Using Elasticsearch, Logstash, and Kibana to visualize JMeter test results.
    - [JMeter + ElasticSearch Live Monitoring](https://medium.com/@anthony.gauthier325/jmeter-elasticsearch-live-monitoring-c895c843c51e) - Using the ElasticSearch Backend listener and Grafana/Kibana to monitor results in realtime.
- Prometheus
    - [jmeter-prometheus-plugin](https://github.com/johrstrom/jmeter-prometheus-plugin) - A Prometheus Listener for Apache JMeter that exposes results in HTTP API.
- Backend Listener Implementations
    - [jmeter-elasticsearch-backend-listener](https://github.com/delirius325/jmeter-elasticsearch-backend-listener) - JMeter plugin to send test results to an ElasticSearch engine.
    - [jmeter-backend-azure](https://github.com/adrianmo/jmeter-backend-azure) - JMeter plugin to send test results to Azure Application Insights.
    - [jmeter-backend-listener-kafka](https://github.com/rahulsinghai/jmeter-backend-listener-kafka) - JMeter plugin to send test results to a Kafka server.
    - [jmeter-listener](https://gitlab.com/testload/jmeter-listener) - JMeter plugin to write load test data on-the-fly to ClickHouse, InfluxDB, ElasticSearch.

## Streaming Protocols

- [Easy and realistic Load Testing of HTTP Live Streaming (HLS) with Apache JMeter](https://www.ubik-ingenierie.com/blog/easy-and-realistic-load-testing-of-http-live-streaming-hls-with-apache-jmeter/)
- [Using JMeter to Load Test Live HLS Concurrency of Wowza Streaming Engine](https://www.realeyes.com/blog/wowza-streaming/)
- [Load testing HLS with Ruby JMeter](https://flood.io/blog/load-testing-hls-with-ruby-jmeter)
- [Media Live Streaming Load Testing with JMeter](https://www.blazemeter.com/live-streaming/) - Collection of articles by BlazeMeter ([HLS](https://www.blazemeter.com/hls/), [RTMP](https://www.blazemeter.com/rtmp/), WS, podcasts, etc.).
- [HLS JMeter Plugin](https://github.com/Blazemeter/HLSPlugin)

## Mobile Apps

- [Record iOS application HTTP requests](http://www.testautomationguru.com/jmeter-record-ios-application-http-requests/)
- [Load Testing Mobile Apps Made Easy](https://www.blazemeter.com/blog/load-testing-mobile-apps-made-easy/)
- [Performance Testing for Native Mobile Apps](https://www.blazemeter.com/blog/view-webcast-performance-testing-native-mobile-apps/)

## Plugins 列表、二次开发

- [JMeter Plugins list](https://docs.google.com/spreadsheets/d/1FYMw3zCMr2Y37QCG_vOyC3HyrLxxi7x5I3khWLj3isU/) - List of available plugins and extensions.
- [JMeter Plugins](https://jmeter-plugins.org/) - Independent set of plugins for Apache JMeter, with plugin manager references many plugins and simplifies installation.
- [Ubik Load Pack](https://ubikloadpack.com/) - Productivity extensions for Apache JMeter.
- [JMeter Developer Manual](https://cwiki.apache.org/confluence/display/jmeter/DeveloperManual)
- [How to write a plugin for JMeter](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)
- [How to build a JMeter plugin utilising groovy](https://web.archive.org/web/20180225144718/http://artur.ejsmont.org/blog/content/how-to-build-a-jmeter-plugin-utilising-groovy)
- [How to create a plugin in JMeter](https://stackoverflow.com/questions/20422640/how-to-create-a-plugin-in-jmeter)
- [Custom JMeter Samplers and Config Elements](http://codyaray.com/2014/07/custom-jmeter-samplers-and-config-elements)
- [Implement Custom JMeter Samplers](https://dzone.com/articles/implement-custom-jmeter-samplers)

## IDE 集成

- [Intellij IDEA IDE Plugin](https://plugins.jetbrains.com/plugin/7013-jmeter-plugin) - Create run configurations and run JMeter tests from Intellij IDEA.
- [JMeter + Eclipse HOWTO](https://cwiki.apache.org/confluence/display/jmeter/JMeterAndEclipseHowTo) - Develop the JMeter project with Eclipse IDE.

## 相关书籍

- [JMeter 性能测试实战 第2版](https://item.m.jd.com/product/12832578.html) 

## 培训课程

- [极客时间：性能测试实战 30 讲](https://time.geekbang.org/column/intro/264)
- [JMeter: Performance and Load Testing](https://www.linkedin.com/learning/jmeter-performance-and-load-testing) - By LinkedIn Learning.
- [BlazeMeter University](https://www.blazemeter.com/university/) - By BlazeMeter.
- [Apache JMeter Testing Courses](https://qainsights.com/services/) - By QAInsights.

## 相关博客

- [BlazeMeter Blog](https://www.blazemeter.com/jmeter/) - BlazeMeter blog about JMeter and performance testing.
- [Flood.io Blog](https://flood.io/blog) - Load testing thoughts, stories and ideas from Flood IO.
- [JMeter Blog](https://shantonusarker.blogspot.com/p/jmeter.html) - Another blog for performance & automation testing using JMeter.

## License

https://github.com/aliesbelik/awesome-jmeter

<a rel="license" href="https://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by/4.0/88x31.png" /></a>
