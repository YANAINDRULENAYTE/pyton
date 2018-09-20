# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range (1, 10):
    new_path = 'dir_{}'.format(i)
    os.makedirs(new_path)

for i in range (1, 10):
    new_path = 'dir_{}'.format(i)
    os.removedirs(new_path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os, os.path
print([name for name in os.listdir('.') if not os.path.isfile(name)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import os

destdir = os.path.abspath('destdir')
os.makedirs(destdir)
from shutil import copyfile, copy
copy(__file__, destdir)


    
