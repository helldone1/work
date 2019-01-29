__author__ = 'Федоров Владислав Николаевич'

# Задача 1
import os
import shutil
import sys

path_dir = [('dir_' + str(i + 1)) for i in range(9)]

def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')

# Задача 2
def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)


main_path = os.getcwd()

# Задача 3
def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        0
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')

def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')
