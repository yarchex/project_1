import tkinter as tk
from tkinter import messagebox
from password_generator.generator import PasswordGenerator


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")

        # Настройка интерфейса
        tk.Label(root, text="Длина пароля:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Уровень сложности:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.level_var = tk.StringVar(value="medium")
        levels = [("Простой", "simple"), ("Средний", "medium"), ("Высокий", "high")]
        for i, (text, value) in enumerate(levels):
            tk.Radiobutton(root, text=text, variable=self.level_var, value=value).grid(row=1, column=i + 1, padx=5, pady=10)

        self.result_label = tk.Label(root, text="Ваш пароль появится здесь", font=("Arial", 12), fg="blue")
        self.result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        tk.Button(root, text="Сгенерировать", command=self.generate_password).grid(row=3, column=0, columnspan=3, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            level = self.level_var.get()
            generator = PasswordGenerator(length, level)
            password = generator.generate()
            self.result_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
