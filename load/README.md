## 安装

1. 安装 virtualenv
```
$ virtualenv -p python3 --no-site-packages venv
```

2. 安装依赖
```shell
$ venv/bin/pip3 install -r requirements.txt
```

3. 运行
并发测试时提高 `-w`的值，按并发数调整。

```shell
$ venv/bin/gunicorn --bind 0.0.0.0:5000 openbuilder:app -w 10
```

4. 调试模式
```shell
$ env FLASK_DEBUG=True FLASK_APP=openbuilder.py venv/bin/flask run
```

## 提交表单

```
POST /form/mongodb HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "form_id": 1,
    "user_id": 1,
    "values": {
        1: "CJ",
        2: "cj@iuantu.com",
        3: "Python 工程师",
        4: "元图（上海）网络科技有限公司"
        6: "简介： 不知道该说什么。"
    }
}
```