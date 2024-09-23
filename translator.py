import tkinter as tk
import httpcore
from tkinter import messagebox
from googletrans import Translator
import os
from tkinter import ttk


BYFER = os.popen('xsel -o').read()  # Получаем значение из буфера обмена
WIDTH = 50
HEIGHT = 8
TITLE = 'Переводчик v1.2'

# Инициализация переводчика
translator = Translator()


def click_translation(language, text_1, text_2):
    """Перевод текста"""
    text_2.config(state="normal")
    text_input = text_1.get("1.0", tk.END).strip()

    if text_input:
        try:
            translation = translator.translate(text_input, dest=language)
        except httpcore._exceptions.ConnectError as e:
            error = f'Ошибка подключения к интернету.\n {e}'
            root.withdraw()  # Скрываем основное окно
            messagebox.showerror(TITLE, error)
            root.destroy()
            raise ConnectionError(error) from e
        text_2.delete("1.0", tk.END)  # Очищаем содержимое текстового поля
        text_2.insert(tk.END, translation.text)  # Вставляем переведенный текст
    text_2.config(state="disabled")


def click_button_byfer(text_1, text_2):
    """Вставить текст из буфера обмена"""
    text_2.config(state="normal")
    byfer = text_1.clipboard_get()  # Получаем текст из буфера обмена
    text_1.delete("1.0", tk.END)  # Очищаем содержимое текстового поля
    text_1.insert(tk.END, byfer)  # Вставляем текст из буфера
    text_2.config(state="disabled")


def click_button_clear(text_1, text_2):
    """Очистить поле"""
    text_2.config(state="normal")
    text_1.delete("1.0", tk.END)
    text_2.delete("1.0", tk.END)
    text_2.config(state="disabled")


def close_app():
    """Закрыть программу"""
    root.destroy()


def help_text():
    """Горячии клавиши"""
    text = 'Esc - Закрыть приложение\n'
    text += 'Ctrl+c - Копировать\n'
    text += 'Ctrl+v - Вставить\n'
    text += 'Enter - Переместить курсор на поле ввода текста\n'
    info_window = tk.Toplevel(root, borderwidth=10, relief=tk.RAISED)
    info_window.title("Помощь")

    info_window.resizable(False, False)
    label = tk.Label(info_window, text=text, justify=tk.LEFT)
    label.pack()
    close_button = tk.Button(
        info_window, text="Закрыть", command=info_window.destroy, bg="red")
    close_button.pack(pady=20)


def on_key_press(event, text_1):
    """Обработка нажатия клавиш"""
    if event.keysym == 'Return':  # Проверяем, нажата ли клавиша Enter
        text_1.focus_set()  # Устанавливаем фокус на text_1
        return "break"  # Игнорируем нажатие Enter
    if event.keysym == 'Escape':
        close_app()


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg="black")
    root.option_add("*Font", ("Arial", 20))
    root.option_add("*foreground", "whitesmoke")  # Цвет текста
    root.option_add("*background", "black")
    root.title(TITLE)
    root.resizable(False, False)  # Запрещаем изменение размера окна

    # --- frame_1 -------------------------------------
    frame_1 = tk.Frame(root)
    label_1 = tk.Label(frame_1, text="Текст: ", justify=tk.LEFT)
    text_1 = tk.Text(
        frame_1, wrap=tk.WORD, width=WIDTH, height=HEIGHT,
        bg='darkslategrey')
    scrollbar_1 = tk.Scrollbar(frame_1, command=text_1.yview)
    text_1.config(yscrollcommand=scrollbar_1.set)
    text_1.insert(tk.END, BYFER)
    text_1.config(insertbackground='white')

    label_1.pack(side=tk.LEFT, padx=20)
    text_1.pack(side=tk.RIGHT)
    scrollbar_1.pack(side=tk.RIGHT, fill=tk.Y)
    # --- / frame_1 -----------------------------------

    # --- frame_2 -------------------------------------
    frame_2 = tk.Frame(root)
    label_2 = tk.Label(frame_2, text="Перевод: ")
    text_2 = tk.Text(
        frame_2, wrap=tk.WORD, width=WIDTH, height=HEIGHT,
        bg='darkslategrey')
    scrollbar_2 = tk.Scrollbar(frame_2, command=text_2.yview)
    text_2.config(yscrollcommand=scrollbar_2.set)
    text_2.config(insertbackground='white')
    text_2.config(state="disabled")

    label_2.pack(side=tk.LEFT, padx=20)
    text_2.pack(side=tk.RIGHT)
    scrollbar_2.pack(side=tk.RIGHT, fill=tk.Y)
    # --- / frame_2 -----------------------------------

    # --- frame_3 -------------------------------------
    frame_3 = tk.Frame(root)
    button_ru = tk.Button(
        frame_3, text='Перевести на русский',
        command=lambda: click_translation('ru', text_1, text_2), bg="green")
    button_en = tk.Button(
        frame_3, text='Перевести на английский',
        command=lambda: click_translation('en', text_1, text_2), bg="blue")

    button_ru.pack(fill="both", side=tk.LEFT, expand=True)
    button_en.pack(fill="both", side=tk.LEFT, expand=True)
    # --- / frame_3 -----------------------------------

    # --- frame_4 -------------------------------------
    frame_4 = tk.Frame(root)
    button_byfer = tk.Button(
        frame_4, text='Вставить из буфера',
        command=lambda: click_button_byfer(text_1, text_2), bg="gray")
    button_clear = tk.Button(
        frame_4, text='Очистить',
        command=lambda: click_button_clear(text_1, text_2), bg="gray")

    button_byfer.pack(fill="both", side=tk.LEFT, expand=True)
    button_clear.pack(fill="both", side=tk.LEFT, expand=True)
    # --- / frame_4 -----------------------------------

    # --- frame_5 -------------------------------------
    frame_5 = tk.Frame(root)
    button_help = tk.Button(
        frame_5, text='Помощь', command=help_text, bg="gray")
    button_exit = tk.Button(
        frame_5, text='Закрыть', command=close_app, bg="red")

    button_exit.pack(fill="both", side=tk.RIGHT)
    button_help.pack(fill="both", side=tk.RIGHT)
    # --- / frame_5 -------------------------------------

    frame_1.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    frame_2.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    frame_3.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    frame_4.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    frame_5.pack(fill=tk.BOTH, expand=True)

    root.bind("<KeyPress>", lambda event: on_key_press(event, text_1))
    click_translation('ru', text_1, text_2)  # Сразу переводить текст
    root.mainloop()  # Запускаем цикл обработки событий
