"""Переводчик с любых языков на русский и английский язык"""
import os
import tkinter as tk
from tkinter import messagebox
import httpcore
from googletrans import Translator  # type: ignore
import customtkinter as ctk  # type: ignore


BUFFER = os.popen('xsel -o').read()  # Получаем значение из буфера обмена
WIDTH_TEXT = 800
HEIGHT = 8
TITLE = 'Переводчик v1.4'
TEXT_COLOR = 'whitesmoke'
FONT = ("Arial", 20)
TRANSLATE_RU = 'Перевести на русский 🇷🇺'
TRANSLATE_EN = 'Перевести на английский 🇺🇸'
INFO_TEXT = 'Переводчик с любых языков на русский и английский язык'
# Инициализация переводчика
translator = Translator()


def click_translation(program, language: str, value_1, value_2):
    """Перевод текста"""
    text_input = value_1.get("1.0", 'end')
    if text_input:
        try:
            translation = translator.translate(text_input, dest=language)
        except httpcore.ConnectError as e:
            error = f'Ошибка подключения к интернету.\n {e}'
            program.withdraw()  # Скрываем основное окно
            messagebox.showerror(TITLE, error)
            program.destroy()
            raise ConnectionError(error) from e
        else:
            value_2.configure(state="normal")
            value_2.delete("1.0", 'end')  # Очищаем содержимое текстового поля
            value_2.insert('end', translation.text)
            value_2.configure(state="disabled")


def click_button_byfer(value_1):
    """Вставить текст из буфера обмена"""
    try:
        byfer = value_1.clipboard_get()  # Получаем текст из буфера обмена
    except tk.TclError:
        messagebox.showinfo("Ошибка", "Буфер обмена пуст.")
        byfer = ''
    value_1.delete("1.0", 'end')  # Очищаем содержимое текстового поля
    value_1.insert('end', byfer)  # Вставляем текст из буфера


def click_button_clear(value_1, value_2):
    """Очистить поле"""
    value_1.delete("1.0", tk.END)
    value_2.configure(state="normal")
    value_2.delete("1.0", tk.END)
    value_2.configure(state="disabled")


def close_app(program):
    """Закрыть программу"""
    program.destroy()


def help_text(program):
    """Горячии клавиши"""
    text = f'{INFO_TEXT}\n\n'
    text += 'Горячие клавиши:\n'
    text += 'Esc - Закрыть приложение\n'
    text += 'F1 - Помощь\n'
    text += f'F2 - {TRANSLATE_RU}\n'
    text += f'F3 - {TRANSLATE_EN}\n'
    text += 'Ctrl+c - Копировать\n'
    text += 'Ctrl+v - Вставить\n'
    text += 'Enter - Переместить курсор на поле ввода текста\n'
    info_window = ctk.CTkToplevel(program)
    info_window.title("Помощь")

    info_window.resizable(False, False)
    label = ctk.CTkLabel(
        info_window, text=text, font=FONT, justify='left', width=WIDTH_TEXT)
    label.pack(pady=(10, 0))
    close_button = ctk.CTkButton(
        info_window, text="Закрыть", command=info_window.destroy,
        fg_color="red", hover_color="maroon", text_color=TEXT_COLOR)
    close_button.pack(pady=(10, 10))


def on_key_press(program, event, value_1, value_2):
    """Обработка нажатия клавиш"""
    if event.keysym == 'Return':  # Проверяем, нажата ли клавиша Enter
        value_1.focus_set()  # Устанавливаем фокус на value_1
        return "break"  # Игнорируем нажатие Enter
    if event.keysym == 'Escape':
        close_app(program)
    if event.keysym == 'F1':
        help_text(program)
    if event.keysym == 'F2':
        click_translation(program, 'ru', value_1, value_2)
    if event.keysym == 'F3':
        click_translation(program, 'en', value_1, value_2)


if __name__ == '__main__':
    root = ctk.CTk()
    root.title(TITLE)
    root.resizable(False, False)  # Запрещаем изменение размера окна
    root.option_add('*Font', FONT)
    root.geometry("800x510")  # Ширина 300 пикселей, высота 200 пикселей

    # --- frame_1 -------------------------------------
    frame_1 = ctk.CTkFrame(root)
    label_1 = ctk.CTkLabel(frame_1, text="Текст: ", width=90, font=FONT)
    text_1 = ctk.CTkTextbox(
        frame_1, width=WIDTH_TEXT, font=FONT)
    text_1.insert(tk.END, BUFFER)

    label_1.pack(side="left", padx=20)
    text_1.pack(side="left")
    # --- / frame_1 -----------------------------------

    # --- frame_2 -------------------------------------
    frame_2 = ctk.CTkFrame(root)
    label_2 = ctk.CTkLabel(frame_2, text="Перевод: ", width=90, font=FONT)
    text_2 = ctk.CTkTextbox(
        frame_2, width=WIDTH_TEXT, font=FONT)
    text_2.configure(state="disabled")

    label_2.pack(side="left", padx=20)
    text_2.pack(side="left")
    # --- / frame_2 -----------------------------------

    # --- frame_3 -------------------------------------
    frame_3 = ctk.CTkFrame(root)
    button_ru = ctk.CTkButton(
        frame_3, text=TRANSLATE_RU,
        fg_color="green", hover_color="darkgreen", text_color=TEXT_COLOR,
        command=lambda: click_translation(root, 'ru', text_1, text_2))
    button_en = ctk.CTkButton(
        frame_3, text=TRANSLATE_RU,
        fg_color="blue", hover_color="darkblue", text_color=TEXT_COLOR,
        command=lambda: click_translation(root, 'en', text_1, text_2))

    button_ru.pack(side="left", padx=10)
    button_en.pack(side="left", padx=10)
    # --- / frame_3 -----------------------------------

    # --- frame_4 -------------------------------------
    frame_4 = ctk.CTkFrame(root)
    button_byfer = ctk.CTkButton(
        frame_4, text='Вставить из буфера',
        fg_color="slategray", hover_color="darkslategray",
        text_color=TEXT_COLOR,
        command=lambda: click_button_byfer(text_1))
    button_clear = ctk.CTkButton(
        frame_4, text='Очистить',
        fg_color="slategray", hover_color="darkslategray",
        text_color=TEXT_COLOR,
        command=lambda: click_button_clear(text_1, text_2))

    button_help = ctk.CTkButton(
        frame_4, text='Помощь',
        fg_color="slategray", hover_color="darkslategray",
        text_color=TEXT_COLOR,
        command=lambda: help_text(root))
    button_exit = ctk.CTkButton(
        frame_4, text='Выход',
        fg_color="red", hover_color="maroon", text_color=TEXT_COLOR,
        command=lambda: close_app(root))

    button_byfer.pack(side="left", padx=10)
    button_clear.pack(side="left", padx=10)
    button_help.pack(side="left", padx=10)
    button_exit.pack(side="left", padx=10)
    # --- / frame_4 -----------------------------------

    root.bind("<KeyPress>", lambda event: on_key_press(
        root, event, text_1, text_2))
    frame_1.pack(pady=(10, 10), padx=(10, 10))
    frame_2.pack(pady=(0, 10), padx=(10, 10))
    frame_3.pack(pady=(0, 15))
    frame_4.pack(pady=(0, 10))
    click_translation(root, 'ru', text_1, text_2)  # переводить текст из буфера

    root.mainloop()
