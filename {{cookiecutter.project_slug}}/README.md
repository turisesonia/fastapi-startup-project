# {{ cookiecutter.project_slug }}

### Environment

```
Python 3.8
Fastapi
{% if cookiecutter.redis == "y" -%}
Redis
{% endif -%}
{% if cookiecutter.mongo == "y" -%}
MongoDB
{% endif -%}

{% if cookiecutter.sql == "postgres" -%}
PostgreSQL
{% elif cookiecutter.sql == "mysql" -%}
MySQL
{% else -%}
{% endif -%}
```
