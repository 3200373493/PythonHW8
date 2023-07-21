def input_number():
    ask = int(input("1-Добавить пользователя\n2-Найти пользователя\n3-Изменить пользователя\n4-Удалить пользователя\n5-Показать список контактов\n6-Выйти\n"))
    return ask

def input_info():
    fio=input("Введите ФИО человека- ")
    birth=input("Введите дату рождения человека- ")
    tele=input("Введите телефон человека- ")
    info=f"{fio},{birth},{tele}\n"
    return info

def input_char():
    char=input("Введите характеристику поиска-")
    return char

def select_num():
    num=int(input("Введите номер записи в поиске-"))
    return num