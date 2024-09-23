import tkinter as tk
from tkinter import ttk

def on_enter(event):
    button['style'] = 'Hover.TButton'  # Устанавливаем стиль при наведении

def on_leave(event):
    button['style'] = 'TButton'  # Возвращаем оригинальный стиль

root = tk.Tk()
root.configure(bg="black")
root.title('Кнопка с наведением')

# Создаем стиль для кнопки
style = ttk.Style()
style.configure('TButton', background='SystemButtonFace', foreground='black')
style.configure('Hover.TButton', background='lightblue', foreground='black')

# Используем ttk.Button вместо tk.Button
button = ttk.Button(root, text='Наведи на меня', style='TButton')
button.pack(pady=20)

# Привязываем события
button.bind("<Enter>", on_enter)  # Наведение курсора
button.bind("<Leave>", on_leave)   # Уход курсора

root.mainloop()
