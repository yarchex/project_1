import random
import string


class PasswordGenerator:
    """Класс для генерации паролей с разными уровнями сложности."""

    LEVELS = {
        'simple': string.ascii_lowercase,
        'medium': string.ascii_letters + string.digits,
        'high': string.ascii_letters + string.digits + string.punctuation,
    }

    def __init__(self, length: int, level: str = 'medium'):
        """
        Инициализация генератора.

        :param length: Длина пароля.
        :param level: Уровень сложности ('simple', 'medium', 'high').
        """
        self.length = length
        self.level = level

    def validate(self):
        """Проверка корректности параметров."""
        if self.length < 1:
            raise ValueError("Длина пароля должна быть больше 0.")
        if self.level not in self.LEVELS:
            raise ValueError("Уровень сложности должен быть: 'simple', 'medium' или 'high'.")

    def generate(self) -> str:
        """Генерация пароля."""
        self.validate()
        characters = self.LEVELS[self.level]
        return ''.join(random.choice(characters) for _ in range(self.length))
