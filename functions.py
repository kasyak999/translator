from googletrans import Translator
import tkinter as tk
import os


# translator = Translator()
# translation = translator.translate("как дела?", dest="ru")
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


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


def click_button_exit(root):
    """Закрыть программу"""
    root.destroy()
