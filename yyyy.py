import time
import threading


def qwe():
    time.sleep(1)
    return 2 + 2


def qwe1():
    time.sleep(1)
    return 5 * 5


def progress():
    functions = [qwe, qwe1]
    # print(len(functions))
    # step = int(100 / 10)
    step = len(functions)
    step = int(100 / step)
    for i in range(0, 100, step):
        time.sleep(1)
        print(f'\r{i}%', end='')
    print('')


if __name__ == '__main__':
    # qwe()
    # qwe1()
    # Создаем поток для прогресс-бара
    progress_thread = threading.Thread(target=progress)
    
    # Запускаем поток прогресс-бара
    progress_thread.start()
    
    # Ждем завершения потока прогресс-бара
    progress_thread.join()