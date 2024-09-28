import os
import time

directory=os.getcwd()
print(directory)
for root, dirs, files in os.walk(directory):
     for file in files:
         print(file)


print(f'Обнаружен файл: {file}, Путь: {os.path.join(file)}, '
            f'Размер: {os.path.getsize('filename.txt')} байт, '
            f'Время изменения: {os.path.getmtime('filename.txt')}, Родительская директория: {os.getcwd()}')