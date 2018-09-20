import os
import sys

def make_dir():
    dir_name = input('Input directory name: ')
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} успешно создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))

def remove_dir():
    dir_name = input('Input directory name: ')
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('Директория {} успешно удалена'.format(dir_name))
    except FileExistsError:
        print('Директория {} не существует'.format(dir_name))


def view_dir():
    dir_name = input('Input directory name: ')
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        list = os.listdir(dir_path)
        print(list)
    except FileNotFoundError:
        print('Директория {} не существует'.format(dir_name))


def go_to_dir():
    dir_name = input('Input directory name: ')
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('Успешно')
    except FileNotFoundError:
        print('Директория {} не существует'.format(dir_name))



    
    
