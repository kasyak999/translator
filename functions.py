from googletrans import Translator
import tkinter as tk
import os


# translator = Translator()
# translation = translator.translate("как дела?", dest="ru")
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
#

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
root_tk.title("Переводчик v1.1")

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
