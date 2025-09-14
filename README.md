# Contacts API

REST API для управління контактами, побудований з використанням FastAPI та SQLAlchemy.

## Функціональність

- Створення, читання, оновлення та видалення контактів (CRUD операції)
- Пошук контактів за ім'ям, прізвищем або email
- Отримання контактів з днями народження на найближчі 7 днів
- Автоматична генерація Swagger документації

## Структура проекту

```
src/
├── database/           # Конфігурація бази даних та моделі
│   ├── db.py          # Налаштування підключення до БД
│   └── models.py      # SQLAlchemy моделі
├── repository/        # Репозиторій для роботи з даними
│   └── contacts.py    # CRUD операції для контактів
├── routes/           # API роутери
│   └── contacts.py   # Ендпоінти для контактів
├── schemas/          # Pydantic схеми для валідації
│   └── contacts.py   # Схеми для контактів
├── exceptions.py     # Обробка помилок
└── config.py         # Конфігурація додатка
tests/                # Тести
├── test_full_api.py  # Повний тест API
├── test_error_handling.py # Тест обробки помилок
├── simple_test.py    # Простий тест
└── README.md         # Документація тестів
main.py               # Головний файл додатка
pyproject.toml        # Poetry конфігурація та залежності
.env.example          # Приклад налаштувань середовища
```

## Poetry команди

### Основні команди
```bash
# Встановити всі залежності
poetry install

# Додати нову залежність
poetry add package_name

# Додати залежність для розробки
poetry add --group dev package_name

# Активувати віртуальне середовище
poetry shell

# Запустити команду у віртуальному середовищі
poetry run command

# Показати інформацію про проект
poetry show

# Оновити залежності
poetry update
```

### Скрипти проекту
```bash
# Запустити сервер
poetry run uvicorn main:app --reload

# Форматування коду
poetry run black src/

# Сортування імпортів
poetry run isort src/

# Лінтинг
poetry run flake8 src/

# Запуск тестів
# Базова перевірка (без сервера і БД)
poetry run python tests/test_basic.py

# Основні тести з реальною базою даних (потребує запущеного сервера)
poetry run python tests/test_full_api.py
poetry run python tests/test_error_handling.py

# Тести з TestClient (без потреби в сервері)
poetry run python tests/test_with_client.py

# Простий тест
poetry run python tests/simple_test.py

# Перевірка якості коду (весь pipeline)
poetry run black src/ && poetry run isort src/ && poetry run flake8 src/ --max-line-length=88
```

## Розробка

### Перед комітом
Рекомендується запускати перевірки якості коду:
```bash
# Форматування та перевірка
poetry run black src/
poetry run isort src/
poetry run flake8 src/ --max-line-length=88
```

### Корисні команди Poetry
```bash
# Показати інформацію про проект
poetry show

# Показати дерево залежностей  
poetry show --tree

# Додати нову залежність
poetry add package-name

# Додати dev залежність
poetry add --group dev package-name

# Експорт залежностей у requirements.txt (якщо потрібно)
poetry export -f requirements.txt --output requirements.txt
```

## Встановлення та запуск

### Передумови
- Python 3.8+
- PostgreSQL
- Poetry (для управління залежностями)

### Встановлення Poetry (якщо ще не встановлено)
```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Linux/Mac
curl -sSL https://install.python-poetry.org | python3 -
```

### Налаштування проекту

1. Клонуйте репозиторій:
```bash
git clone https://github.com/YOUR_USERNAME/goit-pythonweb-hw-08.git
cd goit-pythonweb-hw-08
```

2. Встановіть залежності через Poetry:
```bash
poetry install
```

3. Активуйте віртуальне середовище Poetry:
```bash
poetry shell
```

4. Запустіть PostgreSQL базу даних через Docker:
```bash
# Запустити PostgreSQL в Docker (потрібен Docker)
docker-compose up -d

# Або встановіть PostgreSQL локально і створіть:
# - базу даних: contacts_db
# - користувача: user з паролем: password
```

5. Налаштуйте змінні середовища:
```bash
cp .env.example .env
# Відредагуйте .env файл з вашими налаштуваннями БД
```

6. Запустіть додаток:
```bash
# Через Poetry
poetry run uvicorn main:app --reload
```

Додаток буде доступний за адресою: http://127.0.0.1:8000

**Швидкі посилання:**
- API документація (Swagger): http://127.0.0.1:8000/docs
- API документація (ReDoc): http://127.0.0.1:8000/redoc
- OpenAPI JSON (для Postman): http://127.0.0.1:8000/openapi.json

## API Документація

**Swagger UI**: http://127.0.0.1:8000/docs
**ReDoc**: http://127.0.0.1:8000/redoc

**Різниця між Swagger UI та ReDoc:**
- **Swagger UI** - інтерактивне тестування API прямо в браузері
- **ReDoc** - красива, зручна для читання документація з кращим дизайном

### Postman колекція

Для імпорту API в Postman використовуйте OpenAPI JSON схему:

**JSON Schema URL**: `http://127.0.0.1:8000/openapi.json`

**Як імпортувати в Postman:**
1. Запустіть сервер: `poetry run uvicorn main:app --host 127.0.0.1 --port 8000`
2. Відкрийте Postman
3. Натисніть "Import" → "Link"
4. Вставте URL: `http://127.0.0.1:8000/openapi.json`
5. Натисніть "Continue" → "Import"

Альтернативно, можете скопіювати JSON схему з браузера:
- Перейдіть на `http://127.0.0.1:8000/openapi.json`
- Скопіюйте весь JSON
- У Postman: "Import" → "Raw text" → вставте JSON

📋 **Детальний гід по Postman**: [postman-guide.md](postman-guide.md)

## Ендпоінти

### Контакти

- `POST /api/contacts/` - Створити новий контакт
- `GET /api/contacts/` - Отримати список контактів (з пагінацією та пошуком)
- `GET /api/contacts/{contact_id}` - Отримати контакт за ID
- `PUT /api/contacts/{contact_id}` - Оновити контакт
- `DELETE /api/contacts/{contact_id}` - Видалити контакт
- `GET /api/contacts/birthdays` - Отримати контакти з днями народження на наступні 7 днів

### Параметри пошуку

- `search` - Пошук за ім'ям, прізвищем або email
- `skip` - Пропустити N записів (для пагінації)
- `limit` - Обмежити кількість записів (max 100)

## Приклад використання

### Створення контакту

```bash
curl -X POST "http://127.0.0.1:8000/api/contacts/" \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Іван",
  "last_name": "Петренко",
  "email": "ivan@example.com",
  "phone_number": "+380501234567",
  "birth_date": "1990-05-15",
  "additional_data": "Друг з університету"
}'
```

### Пошук контактів

```bash
curl "http://127.0.0.1:8000/api/contacts/?search=іван"
```

### Дні народження

```bash
curl "http://127.0.0.1:8000/api/contacts/birthdays"
```

## Технології

- **FastAPI** - Веб-фреймворк
- **SQLAlchemy** - ORM для роботи з базою даних
- **PostgreSQL** - База даних
- **Pydantic** - Валідація даних
- **Uvicorn** - ASGI сервер
- **Poetry** - Управління залежностями та пакетами
- **Black** - Форматування коду
- **isort** - Сортування імпортів
- **flake8** - Лінтинг коду

## Автор
Serhii Palamarchuk

Створено в рамках домашнього завдання GoIT Python Web Development
