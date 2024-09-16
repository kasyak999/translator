import tkinter as tk
import functions
import os


# BYFER = os.system('xsel -o')  # выполнить команду
BYFER = os.popen('xsel -o').read()  # получаем значение в переменую
WIDTH = 10
HEIGHT = 10


root = tk.Tk()
root.configure(bg="black")  # Светло-серый фон
# root.geometry("700x500")  # Ширина 300 пикселей, высота 200 пикселей
root.option_add("*Font", ("Arial", 20))
root.option_add("*foreground", "white")
root.option_add("*background", "black")
root.title("Переводчик v1.0")


frame_1 = tk.Frame(root)
label_1 = tk.Label(frame_1, text="Введите текст")
text_1 = tk.Text(frame_1, wrap=tk.WORD, width=WIDTH, height=HEIGHT)
scrollbar_1 = tk.Scrollbar(frame_1, command=text_1.yview)  # Создаем полосу прокрутки
text_1.config(yscrollcommand=scrollbar_1.set)  # Связываем текстовое поле с полосой прокрутки
text_1.insert(tk.END, BYFER)

label_1.pack(side=tk.TOP)
text_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Размещаем Text слева
scrollbar_1.pack(side=tk.RIGHT, fill=tk.Y)  # Размещаем Scrollbar справа


frame_2 = tk.Frame(root)
label_2 = tk.Label(frame_2, text="Перевод")
text_2 = tk.Text(frame_2, wrap=tk.WORD, width=WIDTH, height=HEIGHT)
scrollbar_2 = tk.Scrollbar(frame_2, command=text_2.yview)  # Создаем полосу прокрутки
text_2.config(yscrollcommand=scrollbar_2.set)

label_2.pack(side=tk.TOP)
text_2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_2.pack(side=tk.RIGHT, fill=tk.Y)  # Размещаем Scrollbar справа


frame_3 = tk.Frame(root)
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


frame_4 = tk.Frame(root)
button_exit = tk.Button(
    frame_4, text='Закрыть', command=lambda: functions.click_button_exit(root),
    bg="red")
button_exit.pack(fill="both", side=tk.RIGHT)


# Размещаем элементы в grid
frame_1.grid(column=0, row=0, sticky="ew")
frame_2.grid(column=0, row=1, sticky="ew")
frame_3.grid(column=0, row=2, sticky="ew")
frame_4.grid(column=0, row=3, sticky="ew")


functions.click_button_ru(text_1, text_2)  # Сразу переводим текст из фуфера

# Запрещаем изменение размера окна
root.resizable(False, False)
# Запускаем цикл обработки событий
root.mainloop()
