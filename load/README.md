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
$ venv/bin/gunicorn --bind 0.0.0.0:5000 app:app -w 10
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
        "name": "CJ",
        "email": "cj@iuantu.com",
        "title": "Python 工程师",
        "company": "元图（上海）网络科技有限公司",
        "bio": "简介： 不知道该说什么。"
    }
}
```

```
curl http://127.0.0.1:5000/form/mysql -H "Content-Type: application/json" -X POST -d '{"form_id": 1, "user_id": 1, "values": {"name": "CJ", "email": "cj@iuantu.com", "title": "Python \\u5de5\\u7a0b\\u5e08", "company": "\\u5143\\u56fe\\uff08\\u4e0a\\u6d77\\uff09\\u7f51\\u7edc\\u79d1\\u6280\\u6709\\u9650\\u516c\\u53f8", "bio": "\\u7b80\\u4ecb\\uff1a \\u4e0d\\u77e5\\u9053\\u8be5\\u8bf4\\u4ec0\\u4e48\\u3002"}}'
```