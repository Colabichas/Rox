import os
import subprocess
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

# Функция для запуска приложения
def start_application():
    file_path = filedialog.askopenfilename(title="Выберите приложение для запуска", filetypes=[("Executable files", "*.exe")])
    if file_path:
        try:
            subprocess.Popen(file_path)
            messagebox.showinfo("Успех", f"Приложение {os.path.basename(file_path)} запущено!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось запустить приложение: {e}")

# Функция для остановки приложения
def stop_application():
    app_name = app_name_entry.get()
    if app_name:
        try:
            os.system(f"taskkill /f /im {app_name}")
            messagebox.showinfo("Успех", f"Приложение {app_name} остановлено!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось остановить приложение: {e}")
    else:
        messagebox.showwarning("Внимание", "Введите имя приложения для остановки.")

# Функция для открытия файла с кодом
def open_code_file():
    file_path = filedialog.askopenfilename(title="Выберите файл с кодом", filetypes=[("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                code_editor.delete(1.0, tk.END)
                code_editor.insert(tk.END, file.read())
            code_file_label.config(text=f"Открыт файл: {file_path}")
            global current_file
            current_file = file_path
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")

# Функция для сохранения изменений в файле
def save_code_file():
    if current_file:
        try:
            with open(current_file, "w", encoding="utf-8") as file:
                file.write(code_editor.get(1.0, tk.END))
            messagebox.showinfo("Успех", "Файл успешно сохранен!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
    else:
        messagebox.showwarning("Внимание", "Сначала откройте файл для редактирования.")

# Создаем главное окно
root = tk.Tk()
root.title("Управление приложениями и редактирование кода")
root.geometry("800x600")

# Переменная для хранения текущего файла
current_file = None

# Блок для управления приложениями
management_frame = tk.LabelFrame(root, text="Управление приложениями", padx=10, pady=10)
management_frame.pack(fill="x", padx=10, pady=5)

# Кнопка для запуска приложения
start_button = tk.Button(management_frame, text="Запустить приложение", command=start_application)
start_button.pack(side="left", padx=5, pady=5)

# Поле для ввода имени приложения
app_name_entry = tk.Entry(management_frame, width=30)
app_name_entry.pack(side="left", padx=5, pady=5)

# Кнопка для остановки приложения
stop_button = tk.Button(management_frame, text="Остановить приложение", command=stop_application)
stop_button.pack(side="left", padx=5, pady=5)

# Блок для редактирования кода
code_frame = tk.LabelFrame(root, text="Редактирование кода", padx=10, pady=10)
code_frame.pack(fill="both", expand=True, padx=10, pady=5)

# Метка для отображения текущего файла
code_file_label = tk.Label(code_frame, text="Файл не выбран", anchor="w")
code_file_label.pack(fill="x", padx=5, pady=5)

# Текстовый редактор для кода
code_editor = scrolledtext.ScrolledText(code_frame, wrap=tk.WORD, width=80, height=20)
code_editor.pack(fill="both", expand=True, padx=5, pady=5)

# Кнопка для открытия файла
open_button = tk.Button(code_frame, text="Открыть файл", command=open_code_file)
open_button.pack(side="left", padx=5, pady=5)

# Кнопка для сохранения файла
save_button = tk.Button(code_frame, text="Сохранить файл", command=save_code_file)
save_button.pack(side="left", padx=5, pady=5)

# Запуск главного цикла
root.mainloop()