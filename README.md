# django-project


[![codecov](https://codecov.io/gh/jfobatista/django-project/branch/main/graph/badge.svg?token=SpPFL9AHKR)](https://codecov.io/gh/jfobatista/django-project)

[![codecov](https://codecov.io/gh/jfobatista/django-project/branch/main/graph/badge.svg?token=SpPFL9AHKR)](https://codecov.io/gh/jfobatista/django-project)

### <strong>Instruções para instalação</strong>:

#### Criar e ativar ambiente virtual Python (venv):

```python -m venv .venv```

```source .venv/bin/activate```

#### <strong>Instalar dependências</strong>:

```pip install -r requirements.txt```

#### <strong>Instalar dependências, inclusive de desenvolvimento</strong>:

```pip install -r requirements-dev.txt```

#### Copiar variáveis de ambiente:

```cp contrib/env-sample .env```

#### Configuração DB:

```python manage.py makemigrations```

```python manage.py migrate```

#### Rodar Django:

```python manage.py runserver```