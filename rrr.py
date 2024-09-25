import tkinter as tk
import threading

# Создаем основное окно
root = tk.Tk()
root.title("Пример реальной задачи")
root.geometry("400x200")

# Создаем метку
label = tk.Label(root, text="Обработка данных...", font=("Arial", 16))
label.pack(pady=20)

# Создаем прогресс-бар
progress_bar = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300)
progress_bar.pack(pady=20)

def long_task():
    """Реальная задача: подсчет чисел"""
    total = 10_000_000  # Условно большая задача
    chunk = total // 100  # Примерный шаг для обновления прогресса
    counter = 0
    
    for i in range(total):
        # Выполняем долгую операцию (например, подсчет)
        counter += 1
        
        # Обновляем прогресс каждые "chunk" шагов
        if i % chunk == 0:
            progress = (i / total) * 100
            progress_bar.set(progress)
            # root.update_idletasks()  # Обновляем интерфейс
    
    # После выполнения
    label.config(text="Задача завершена!")

def start_task():
    """Запуск задачи в отдельном потоке"""
    threading.Thread(target=long_task).start()

# Кнопка для старта задачи
start_button = tk.Button(root, text="Начать задачу", command=start_task)
start_button.pack(pady=20)

# Запуск главного цикла приложения
root.mainloop()