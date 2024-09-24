import customtkinter as ctk
from googletrans import Translator


WIDTH = 150
HEIGHT = 58
TITLE = 'Переводчик v1.3'
TEXT_COLOR = 'whitesmoke'

# Создаем окно
root = ctk.CTk()
root.title(TITLE)
# root.resizable(False, False)  # Запрещаем изменение размера окна

# --- frame_1 -------------------------------------
frame_1 = ctk.CTkFrame(root)
label_1 = ctk.CTkLabel(frame_1, text="Текст: ", width=70)
text_1 = ctk.CTkTextbox(
    frame_1, width=500)

label_1.pack(side="left", padx=20)
text_1.pack(side="left")
frame_1.pack(pady=(10, 10), padx=(10, 10))
# --- / frame_1 -----------------------------------

# --- frame_2 -------------------------------------
frame_2 = ctk.CTkFrame(root)
label_2 = ctk.CTkLabel(frame_2, text="Перевод: ", width=70)
text_2 = ctk.CTkTextbox(
    frame_2, width=500)

label_2.pack(side="left", padx=20)
text_2.pack(side="left")
frame_2.pack(pady=(0, 10), padx=(10, 10))
# --- / frame_2 -----------------------------------

# --- frame_3 -------------------------------------
frame_3 = ctk.CTkFrame(root)
button_ru = ctk.CTkButton(
    frame_3, text='Перевести на русский',
    fg_color="green", hover_color="darkgreen", text_color=TEXT_COLOR)
button_en = ctk.CTkButton(
    frame_3, text='Перевести на английский',
    fg_color="blue", hover_color="darkblue", text_color=TEXT_COLOR)

button_ru.pack(side="left")
button_en.pack(side="left")
frame_3.pack(pady=(0, 10), padx=(10, 10))
# --- / frame_3 -----------------------------------

# --- frame_4 -------------------------------------
frame_4 = ctk.CTkFrame(root)
button_ru = ctk.CTkButton(
    frame_4, text='Вставить из буфера',
    fg_color="gray", hover_color="dimgray", text_color=TEXT_COLOR)
button_en = ctk.CTkButton(
    frame_4, text='Очистить',
    fg_color="gray", hover_color="dimgray", text_color=TEXT_COLOR)

button_ru.pack(side="left")
button_en.pack(side="left")
frame_4.pack(pady=(0, 10), padx=(10, 10))
# --- / frame_4 -----------------------------------

# --- frame_5 -------------------------------------
frame_5 = ctk.CTkFrame(root)
button_help = ctk.CTkButton(
    frame_5, text='Помощь',
    fg_color="gray", hover_color="dimgray", text_color=TEXT_COLOR)
button_exit = ctk.CTkButton(
    frame_5, text='Выход',
    fg_color="red", hover_color="maroon", text_color=TEXT_COLOR)

button_help.pack(side="left")
button_exit.pack(side="left")
frame_5.pack(pady=(0, 10), padx=(10, 10))
# --- / frame_5 -----------------------------------

root.mainloop()