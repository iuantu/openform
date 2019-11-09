# Form builder

## 实验环境

28核 XEON (超线程) + 64 GB 400GB SSD

## 应用

## 使用的库

- Flask webframework
- Gunicorn

## 接口

- POST /form/mysql
- POST /form/mongodb
- GET /form/mysql/{id}/rows
- GET /form/mongodb/{id}/rows

## MongoDB 和MySQL配置

目前使用默认配置

## 压力测试脚本

### 使用的库

- [Jinja](https://jinja.palletsprojects.com)
- [Gevent](http://www.gevent.org/intro.html)
- [Click](https://click.palletsprojects.com/en/7.x/)

```shell
$ load -c 100 -t 100 -n 100 http://127.0.0.1/form/mysql -d {form_id: 1, user_id: {%sequqnce(10)%}}

This is iUanTuBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        flask
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      1
Time taken for tests:   3.002 seconds
Complete requests:      10000
Failed requests:        0
Requests per second:    3330.97 [#/sec] (mean)
Time per request:       0.300 [ms] (mean)

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      0
  95%      0
  98%      1
  99%      1
 100%    133 (longest request)
```

```
def sequence(step):
    """ 每多少次请求步进一
    """
    pass
```

## 实验结果

请求日志保存为csv表格。

- Unix timestamp 保留小数点后两位
- URL 
- Response time 单次请求响应时间

### 图表

使用Excel制作趋势图按时间显示响应平均值。
