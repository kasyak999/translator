import tkinter as tk
import functions

# --- frame_1 -------------------------------------
frame_1 = tk.Frame(functions.root)
label_1 = tk.Label(frame_1, text="Текст: ", justify=tk.LEFT)
text_1 = tk.Text(
    frame_1, wrap=tk.WORD, width=functions.WIDTH, height=functions.HEIGHT,
    bg='darkslategrey')
scrollbar_1 = tk.Scrollbar(frame_1, command=text_1.yview)  # Создаем полосу прокрутки
text_1.config(yscrollcommand=scrollbar_1.set)  # Связываем текстовое поле с полосой прокрутки
text_1.insert(tk.END, functions.BYFER)
text_1.config(insertbackground='white')  # цвет курсора

label_1.pack(side=tk.LEFT, padx=20)
text_1.pack(side=tk.RIGHT)  # Размещаем Text слева
scrollbar_1.pack(side=tk.RIGHT, fill=tk.Y)  # Размещаем Scrollbar справа
# --- / frame_1 -----------------------------------

# --- frame_2 -------------------------------------
frame_2 = tk.Frame(functions.root)
label_2 = tk.Label(frame_2, text="Перевод: ")
text_2 = tk.Text(
    frame_2, wrap=tk.WORD, width=functions.WIDTH, height=functions.HEIGHT,
    bg='darkslategrey')
scrollbar_2 = tk.Scrollbar(frame_2, command=text_2.yview)  # Создаем полосу прокрутки
text_2.config(yscrollcommand=scrollbar_2.set)
text_2.config(insertbackground='white')  # цвет курсора

label_2.pack(side=tk.LEFT, padx=20)
text_2.pack(side=tk.RIGHT)
scrollbar_2.pack(side=tk.RIGHT, fill=tk.Y)  # Размещаем Scrollbar справа
# --- / frame_2 -----------------------------------

# --- frame_3 -------------------------------------
frame_3 = tk.Frame(functions.root)
button = tk.Button(
    frame_3, text='Перевести на русский',
    command=lambda: functions.click_button_ru(
        text_1, text_2), bg="green")
button_en = tk.Button(
    frame_3, text='Перевести на english',
    command=lambda: functions.click_button_en(
        text_1, text_2), bg="blue")
button_byfer = tk.Button(
    frame_3, text='Вставить из буфера',
    command=lambda: functions.click_button_byfer(text_1), bg="gray")
button_close = tk.Button(
    frame_3, text='Очистить',
    command=lambda: functions.click_button_clear(text_1, text_2),
    bg="gray")
button.pack(fill="both", side=tk.LEFT)
button_byfer.pack(fill="both", side=tk.LEFT)
button_close.pack(fill="both", side=tk.LEFT)
button_en.pack(fill="both", side=tk.LEFT)
# --- / frame_3 -----------------------------------

# --- frame_4 -------------------------------------
frame_4 = tk.Frame(functions.root)
button_help = tk.Button(
    frame_4, text='Помощь', command=lambda: functions.show_text(),
    bg="gray")
button_exit = tk.Button(
    frame_4, text='Закрыть', command=functions.root_tk.destroy,
    bg="red")
button_exit.pack(fill="both", side=tk.RIGHT)
button_help.pack(fill="both", side=tk.RIGHT)
# --- / frame_4 -------------------------------------

frame_1.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
frame_2.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
frame_3.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
frame_4.pack(fill=tk.BOTH, expand=True)

functions.click_button_ru(text_1, text_2)  # Сразу переводим текст из фуфера

# Запускаем цикл обработки событий
functions.root.mainloop()
