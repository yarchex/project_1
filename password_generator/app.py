from password_generator.generator import PasswordGenerator


def main():
    print("Добро пожаловать в генератор паролей!")
    try:
        length = int(input("Введите длину пароля: "))
        level = input("Выберите уровень сложности (simple, medium, high): ").strip().lower()

        generator = PasswordGenerator(length, level)
        password = generator.generate()

        print(f"Ваш сгенерированный пароль: {password}")
    except ValueError as error:
        print(f"Ошибка: {error}")
    except KeyboardInterrupt:
        print("\nВыход из программы. До свидания!")


if __name__ == "__main__":
    main()
