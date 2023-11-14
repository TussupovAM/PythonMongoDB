# PythonMongoDB

 pip install -r requirements.txt
 python manage.py runserver

Отправьте POST запрос на `final/api/user/register/` с данными пользователя в формате JSON:

```json
{
    "email": "user@example.com",
    "password": "your_password",
    "username": "your_username"
}

Логин
Отправьте POST запрос на final/api/user/login/ с данными в формате JSON:
{
    "email": "user@example.com",
    "password": "your_password"
}
