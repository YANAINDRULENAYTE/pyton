# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь
# заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате:
# текст в нижнем регистре, допускается нижнее подчеркивание и цифры,
# потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя,
# te$T@test.net - неверно указан email
#(спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

name = input ('Input name ')
surname = input ('Input surname ')
email = input ('Input e-mail ')

pattern = '^([A-Z][a-z]+)' 
pattern1 = '^([a-z0-9_]+)@[a-zA-Z0-9]+\.(ru|org|com)$'

search_result = re.search(pattern, name)

if search_result:
    print ('correct')
else:
    print ('incorrect name')

search_result1 = re.search(pattern, surname)

if search_result1:
    print ('correct')
else:
    print ('incorrect surname')

search_result2 = re.search(pattern1, email)

if search_result2:
    print ('correct')
else:
    print ('incorrect e-mail')



# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

import re

pattern = '[\.{2, }]'
search_result = re.search(pattern, some_str)
if search_result:
    print('True')
else:
    print ('False')
  




