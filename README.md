본 레포지토리는 [Poetry](https://python-poetry.org) 를 통해 의존성을 관리하고 있습니다.

# 실행

```bash
$ pip install poetry


# Allocate your virtual environment and install project dependencies
$ poetry install

# Activate virtual environment
$ poetry shell

# Initialize and run application
(.venv) $ python manage.py makemigration && python manage.py migrate
(.venv) $ python manage.py runserver
```docs: create README.md