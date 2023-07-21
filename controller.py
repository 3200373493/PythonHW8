from database import*
from view import*

def main():
    while True:
        num = input_number()
        if num == 1:
            info = input_info()
            write_info(info)
        elif num == 2:
            char=input_char()
            find_info(char)
        elif num == 3:
            char=input_char()
            lst_sel=find_info(char)
            sel_num=select_num()   
            info = input_info()
            change_data(lst_sel[sel_num-1],info)
            print("Изменения внесены")    
        elif num ==4:
            char=input_char()
            lst_sel=find_info(char)
            sel_num=select_num()   
            delete_data(lst_sel[sel_num-1])
            print("Контакт удален") 
        elif num ==5:
            view()                 
        elif num == 6:
            print("Выход из программы....")
            break
main()

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

