# Open Form

Open Form 是一个开源、易用的表单构建器。可以帮助你轻松的完成市场调研、数据填报的工作。

[在线使用](https://oform.cn)

![预览](https://github.com/iuantu/openform/raw/master/doc/assets/preview.png)

# 特性

- 表单设计
- 表单填写
- 表单协作
- API访问
- 数据分析
- 数据查询
- 导出CSV表格

# 安装

## 数据库

MySQL为主要的数据库，有一部分功能使用其他数据库会有问题。

创建数据库

```sql
CREATE DATABASE IF NOT EXISTS openform DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

## Python

```bash
$ export FLASK_ENV=DEBUG
$ flask db upgrade
$ flask run
```

## Web

Web的项目目录在openform同名目录内，进入目录编译即可。静态文件的访问是使用软连接到flask的静态文件访问模块。

```bash
$ yarn
$ yarn build
```

如果是调试，使用 `yarn serve` 访问 http://localhost:8080 端口。

# 产品说明

- 登录
- 注册
- [表单设计](https://github.com/iuantu/openform/wiki/%E8%A1%A8%E5%8D%95%E8%AE%BE%E8%AE%A1)
- 表单列表
- 表单概述
- 表单预览
- 表单发布
- 数据统计