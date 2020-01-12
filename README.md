# Install

```sql
CREATE DATABASE IF NOT EXISTS openform DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

```bash
$ export FLASK_ENV=DEBUG
$ flask db upgrade
$ flask run
```