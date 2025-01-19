# ui.py
import tkinter as tk
from logic import create_employee, add_route_to_journal, display_journal


def main_ui():
    root = tk.Tk()
    root.title("Информационная система альпинистского клуба")

    tk.Label(root, text="Название клуба").grid(row=0, column=0)
    club_entry = tk.Entry(root)
    club_entry.grid(row=0, column=1)

    tk.Label(root, text="Контактная информация").grid(row=1, column=0)
    contact_entry = tk.Entry(root)
    contact_entry.grid(row=1, column=1)

    tk.Label(root, text="ФИО сотрудника").grid(row=2, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=2, column=1)

    tk.Label(root, text="Должность").grid(row=3, column=0)
    position_entry = tk.Entry(root)
    position_entry.grid(row=3, column=1)

    tk.Label(root, text="Стаж работы").grid(row=4, column=0)
    experience_entry = tk.Entry(root)
    experience_entry.grid(row=4, column=1)

    def add_employee():
        try:
            employee = create_employee(
                club_entry.get(),
                contact_entry.get(),
                name_entry.get(),
                position_entry.get(),
                int(experience_entry.get())
            )
            tk.Label(root, text=f"Сотрудник добавлен: {employee}").grid(row=6, column=0, columnspan=2)
        except ValueError:
            tk.Label(root, text="Ошибка ввода данных! Проверьте поля!").grid(row=6, column=0, columnspan=2)

    tk.Button(root, text="Добавить сотрудника", command=add_employee).grid(row=5, column=0, columnspan=2)

    # Отладочный вывод
    print("Интерфейс запущен")

    root.mainloop()


if __name__ == "__main__":
    main_ui()
