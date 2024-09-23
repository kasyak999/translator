import tkinter as tk
import httpcore
from tkinter import messagebox
from googletrans import Translator
import os


# translator = Translator()
# translation = translator.translate("как дела?", dest="ru")
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# BYFER = os.system('xsel -o')  # выполнить команду
BYFER = os.popen('xsel -o').read()  # получаем значение в переменую
WIDTH = 50
HEIGHT = 8

root_tk = tk.Tk()
root_tk.configure(bg="black")  # Светло-серый фон
# root.geometry("700x500")  # Ширина 300 пикселей, высота 200 пикселей
root_tk.option_add("*Font", ("Arial", 20))
root_tk.option_add("*foreground", "white")
root_tk.option_add("*background", "black")
root_tk.title("Переводчик v1.2")

# Привязываем клавишу Esc к функции закрытия
root_tk.bind('<Escape>', lambda event: close_app())
root_tk.resizable(False, False)  # Запрещаем изменение размера окна
# Создаем рамку для всего приложения
root = tk.Frame(root_tk, borderwidth=10, relief=tk.RAISED)
root.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)


def click_button_ru(text_1, text_2):
    """Перевод на русский"""
    text_1 = text_1.get("1.0", tk.END)
    translator = Translator()
    translation = translator.translate(text_1, dest="ru")

    with open('perevod.txt', 'w') as f:
        f.write(translation.text)
    with open('perevod.txt', 'r') as f:
        text_content = f.read()
        text_2.delete("1.0", tk.END)  # Очищаем содержимое текстового поля
        text_2.insert(tk.END, text_content)  # Вставляем текст из файла
        os.remove("perevod.txt")


def click_button_en(text_1, text_2):
    """Перевод на английский"""
    text_1 = text_1.get("1.0", tk.END)
    translator = Translator()
    translation = translator.translate(text_1, dest="en")
    with open('perevod.txt', 'w') as f:
        f.write(translation.text)
    with open('perevod.txt', 'r') as f:
        text_content = f.read()
        text_2.delete("1.0", tk.END)  # Очищаем содержимое текстового поля
        text_2.insert(tk.END, text_content)  # Вставляем текст из файла
        os.remove("perevod.txt")


def click_button_byfer(text_1):
    byfer = text_1.clipboard_get()  # Получаем текст из буфера обмена
    text_1.delete("1.0", tk.END)  # Очищаем содержимое текстового поля
    text_1.insert(tk.END, byfer)  # Вставляем текст из файла


def click_button_clear(text_1, text_2):
    """Очистить поле"""
    text_1.delete("1.0", tk.END)
    text_2.delete("1.0", tk.END)


def close_app(event=None):
    """Закрыть программу"""
    root_tk.destroy()


def show_text():
    text = 'Esc - Закрыть приложение.\n'
    text += 'Ctrl+c - Копировать\n'
    text += 'Ctrl+v - Вставить.\n'
    info_window = tk.Toplevel(root_tk, borderwidth=10, relief=tk.RAISED)
    info_window.title("Помощь")

    info_window.resizable(False, False)
    label = tk.Label(info_window, text=text, justify=tk.LEFT)
    label.pack()
    close_button = tk.Button(
        info_window, text="Закрыть", command=info_window.destroy, bg="red")
    close_button.pack(pady=20)


def main():
    # --- frame_1 -------------------------------------
    frame_1 = tk.Frame(root)
    label_1 = tk.Label(frame_1, text="Текст: ", justify=tk.LEFT)
    text_1 = tk.Text(
        frame_1, wrap=tk.WORD, width=WIDTH, height=HEIGHT,
        bg='darkslategrey')
    scrollbar_1 = tk.Scrollbar(frame_1, command=text_1.yview)  # Создаем полосу прокрутки
    text_1.config(yscrollcommand=scrollbar_1.set)  # Связываем текстовое поле с полосой прокрутки
    text_1.insert(tk.END, BYFER)
    text_1.config(insertbackground='white')  # цвет курсора

    label_1.pack(side=tk.LEFT, padx=20)
    text_1.pack(side=tk.RIGHT)  # Размещаем Text слева
    scrollbar_1.pack(side=tk.RIGHT, fill=tk.Y)  # Размещаем Scrollbar справа
    # --- / frame_1 -----------------------------------

    # --- frame_2 -------------------------------------
    frame_2 = tk.Frame(root)
    label_2 = tk.Label(frame_2, text="Перевод: ")
    text_2 = tk.Text(
        frame_2, wrap=tk.WORD, width=WIDTH, height=HEIGHT,
        bg='darkslategrey')
    scrollbar_2 = tk.Scrollbar(frame_2, command=text_2.yview)  # Создаем полосу прокрутки
    text_2.config(yscrollcommand=scrollbar_2.set)
    text_2.config(insertbackground='white')  # цвет курсора

    label_2.pack(side=tk.LEFT, padx=20)
    text_2.pack(side=tk.RIGHT)
    scrollbar_2.pack(side=tk.RIGHT, fill=tk.Y)  # Размещаем Scrollbar справа
    # --- / frame_2 -----------------------------------

    # --- frame_3 -------------------------------------
    frame_3 = tk.Frame(root)
    button = tk.Button(
        frame_3, text='Перевести на русский',
        command=lambda: click_button_ru(
            text_1, text_2), bg="green")
    button_en = tk.Button(
        frame_3, text='Перевести на english',
        command=lambda: click_button_en(
            text_1, text_2), bg="blue")
    button_byfer = tk.Button(
        frame_3, text='Вставить из буфера',
        command=lambda: click_button_byfer(text_1), bg="gray")
    button_close = tk.Button(
        frame_3, text='Очистить',
        command=lambda: click_button_clear(text_1, text_2),
        bg="gray")
    button.pack(fill="both", side=tk.LEFT)
    button_byfer.pack(fill="both", side=tk.LEFT)
    button_close.pack(fill="both", side=tk.LEFT)
    button_en.pack(fill="both", side=tk.LEFT)
    # --- / frame_3 -----------------------------------

    # --- frame_4 -------------------------------------
    frame_4 = tk.Frame(root)
    button_help = tk.Button(
        frame_4, text='Помощь', command=lambda: show_text(),
        bg="gray")
    button_exit = tk.Button(
        frame_4, text='Закрыть', command=root_tk.destroy,
        bg="red")
    button_exit.pack(fill="both", side=tk.RIGHT)
    button_help.pack(fill="both", side=tk.RIGHT)
    # --- / frame_4 -------------------------------------

    frame_1.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    frame_2.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    frame_3.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    frame_4.pack(fill=tk.BOTH, expand=True)

    click_button_ru(text_1, text_2)


if __name__ == '__main__':
    try:
        main()
    except httpcore._exceptions.ConnectError as e:
        error = f'Ошибка подключения к интернету:\n {e}'
        root_tk.withdraw()  # Скрываем основное окно
        messagebox.showerror("Ошибка", error)
        raise ConnectionError(error) from e

    # Запускаем цикл обработки событий
    root.mainloop()
