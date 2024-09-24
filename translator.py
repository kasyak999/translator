import tkinter as tk
import httpcore
from tkinter import messagebox
from googletrans import Translator
import os
import customtkinter as ctk


BYFER = os.popen('xsel -o').read()  # Получаем значение из буфера обмена
WIDTH_TEXT = 800
HEIGHT = 8
TITLE = 'Переводчик v1.3'
TEXT_COLOR = 'whitesmoke'
FONT = ("Arial", 20)
# Инициализация переводчика
translator = Translator()


def click_translation(language, text_1, text_2):
    """Перевод текста"""
    text_input = text_1.get("1.0", 'end')
    if text_input:
        try:
            translation = translator.translate(text_input, dest=language)
        except AttributeError as e:
            error = f'Превышиено количество запросов\n {e}'
            messagebox.showerror(TITLE, error)
            raise ConnectionError(error) from e
        except httpcore._exceptions.ConnectError as e:
            error = f'Ошибка подключения к интернету.\n {e}'
            root.withdraw()  # Скрываем основное окно
            messagebox.showerror(TITLE, error)
            root.destroy()
            raise ConnectionError(error) from e
        else:
            text_2.configure(state="normal")
            text_2.delete("1.0", 'end')  # Очищаем содержимое текстового поля
            text_2.insert('end', translation.text)  # Вставляем переведенный текст
            text_2.configure(state="disabled")


def click_button_byfer(text_1, text_2):
    """Вставить текст из буфера обмена"""
    text_2.configure(state="normal")
    try:
        byfer = text_1.clipboard_get()  # Получаем текст из буфера обмена
    except tk.TclError:
        messagebox.showinfo("Ошибка", "Буфер обмена пуст.")
        byfer = ''
    text_1.delete("1.0", 'end')  # Очищаем содержимое текстового поля
    text_1.insert('end', byfer)  # Вставляем текст из буфера
    text_2.configure(state="disabled")


def click_button_clear(text_1, text_2):
    """Очистить поле"""
    text_2.configure(state="normal")
    text_1.delete("1.0", tk.END)
    text_2.delete("1.0", tk.END)
    text_2.configure(state="disabled")


def close_app():
    """Закрыть программу"""
    root.destroy()


def help_text():
    """Горячии клавиши"""
    text = 'Esc - Закрыть приложение\n'
    text += 'Ctrl+c - Копировать\n'
    text += 'Ctrl+v - Вставить\n'
    text += 'Enter - Переместить курсор на поле ввода текста\n'
    info_window = ctk.CTkToplevel(root)
    info_window.title("Помощь")

    info_window.resizable(False, False)
    label = ctk.CTkLabel(
        info_window, text=text, font=FONT, justify='left', width=WIDTH_TEXT)
    label.pack()
    close_button = ctk.CTkButton(
        info_window, text="Закрыть", command=info_window.destroy,
        fg_color="red", hover_color="maroon", text_color=TEXT_COLOR)
    close_button.pack(pady=20)


def on_key_press(event, text_1):
    """Обработка нажатия клавиш"""
    if event.keysym == 'Return':  # Проверяем, нажата ли клавиша Enter
        text_1.focus_set()  # Устанавливаем фокус на text_1
        return "break"  # Игнорируем нажатие Enter
    if event.keysym == 'Escape':
        close_app()


if __name__ == '__main__':
    # Создаем окно
    root = ctk.CTk()
    root.title(TITLE)
    root.resizable(False, False)  # Запрещаем изменение размера окна
    root.option_add('*Font', FONT)

    # --- frame_1 -------------------------------------
    frame_1 = ctk.CTkFrame(root)
    label_1 = ctk.CTkLabel(frame_1, text="Текст: ", width=90, font=FONT)
    text_1 = ctk.CTkTextbox(
        frame_1, width=WIDTH_TEXT, font=FONT)

    label_1.pack(side="left", padx=20)
    text_1.pack(side="left")
    frame_1.pack(pady=(10, 10), padx=(10, 10))
    # --- / frame_1 -----------------------------------

    # --- frame_2 -------------------------------------
    frame_2 = ctk.CTkFrame(root)
    label_2 = ctk.CTkLabel(frame_2, text="Перевод: ", width=90, font=FONT)
    text_2 = ctk.CTkTextbox(
        frame_2, width=WIDTH_TEXT, font=FONT)
    text_2.configure(state="disabled")

    label_2.pack(side="left", padx=20)
    text_2.pack(side="left")
    frame_2.pack(pady=(0, 10), padx=(10, 10))
    # --- / frame_2 -----------------------------------

    # --- frame_3 -------------------------------------
    frame_3 = ctk.CTkFrame(root)
    button_ru = ctk.CTkButton(
        frame_3, text='Перевести на русский',
        fg_color="green", hover_color="darkgreen", text_color=TEXT_COLOR,
        command=lambda: click_translation('ru', text_1, text_2))
    button_en = ctk.CTkButton(
        frame_3, text='Перевести на английский',
        fg_color="blue", hover_color="darkblue", text_color=TEXT_COLOR,
        command=lambda: click_translation('en', text_1, text_2))

    button_ru.pack(side="left", padx=10)
    button_en.pack(side="left", padx=10)
    frame_3.pack(pady=(0, 15))
    # --- / frame_3 -----------------------------------

    # --- frame_4 -------------------------------------
    frame_4 = ctk.CTkFrame(root)
    button_byfer = ctk.CTkButton(
        frame_4, text='Вставить из буфера',
        fg_color="gray", hover_color="dimgray", text_color=TEXT_COLOR,
        command=lambda: click_button_byfer(text_1, text_2))
    button_clear = ctk.CTkButton(
        frame_4, text='Очистить',
        fg_color="gray", hover_color="dimgray", text_color=TEXT_COLOR,
        command=lambda: click_button_clear(text_1, text_2))
    
    button_help = ctk.CTkButton(
        frame_4, text='Помощь',
        fg_color="gray", hover_color="dimgray", text_color=TEXT_COLOR,
        command=help_text)
    button_exit = ctk.CTkButton(
        frame_4, text='Выход',
        fg_color="red", hover_color="maroon", text_color=TEXT_COLOR,
        command=close_app)

    button_byfer.pack(side="left", padx=10)
    button_clear.pack(side="left", padx=10)
    button_help.pack(side="left", padx=10)
    button_exit.pack(side="left", padx=10)
    frame_4.pack(pady=(0, 10))
    # --- / frame_4 -----------------------------------

    root.bind("<KeyPress>", lambda event: on_key_press(event, text_1))
    click_translation('ru', text_1, text_2)  # Сразу переводить текст из буфера
    root.mainloop()
