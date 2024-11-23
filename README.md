# Password Generator

## Описание
Этот проект представляет собой генератор паролей с тремя уровнями сложности: 
- **Простой (simple):** только строчные буквы.
- **Средний (medium):** строчные и заглавные буквы, а также цифры.
- **Высокий (high):** строчные и заглавные буквы, цифры и спецсимволы.

## Как использовать
1. Скопируйте репозиторий:
    ```bash
    git clone https://github.com/username/password_generator.git
    cd password_generator
    ```
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3. Запустите приложение:
    ```bash
    python -m password_generator.app
    ```

## Пример работы
### Ввод:
```bash
Введите длину пароля: 12
Выберите уровень сложности (simple, medium, high): high
