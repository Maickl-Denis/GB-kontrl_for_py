# -*- coding: utf-8 -*-
import os
from helper import Nout
def menu():
    n = Nout()
    print("Привет ты в программе заметки в консоли")
    work =True
    while work:
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        num, men = first_menu()
        match num:
            # 1. Показать все заметки
            case 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                num, men = work_nout()
                match num:
                    # Вывести список заметок
                    case 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        n.print()
                        num, men = re_up_del_nout()
                        match num:
                            # Читать заметку
                            case 1:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                n.print()
                                n.read_nout(input("Выберкрите заметку (ID) :"))
                            # Редактировать заметку
                            case 2:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                n.print()
                                n.edit_nout(input("Выберкрите заметку (ID) :"))
                            # Удалить заметку
                            case 3:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                n.print()
                                n.del_nout(input("Выберкрите заметку (ID) :"))
                            # Выход
                            case 0:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                continue
                    # Список с фильтрами
                    case 2:
                        pass
                    case 0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
            # 2. Добавить заметку
            case 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                n.add_nout()
            #3. Сохранить все изменения
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                n.save_db()
            # Выход
            case 0:
                if n.db == n.load_db():
                    work = False
                else:
                    while True:
                        save_data = input("Есть не сохраненные данные, вы желаете их сохранить? [Д/н]:")
                        if save_data == "Д":
                            n.save_db()
                            work = False
                            break
                        elif save_data == "н":
                            work = False
                            break

def first_menu():
    try:
        ls = {1: "Работа с заметками", 2: "Добавить заметку", 3: "Сохранить все изменения", 0: "Выход"}
        num = int(input(f"1. {ls[1]}\n"
                        f"2. {ls[2]}\n"
                        f"3. {ls[3]}\n"
                        f"0. {ls[0]}\n"
                        "Выберете пункт меню:  "))
    except ValueError:
        return -1, None
    else:
        return num, ls.get(num)

def work_nout():
    try:
        ls = {1: "Показать список заметок", 2: "Показать список заметок с фильтрами", 0: "Выход"}
        num = int(input(f"1. {ls[1]}\n"
                        f"2. {ls[2]}\n"
                        f"0. {ls[0]}\n"
                        "Выберете пункт меню:  "))
    except ValueError:
        return -1, None
    else:
        return num, ls.get(num)

def re_up_del_nout():
    try:
        ls = {1: "Читать заметку", 2: "Редактировать заметку", 3: "Удалить заметку", 0: "Выход"}
        num = int(input(f"1. {ls[1]}\n"
                        f"2. {ls[2]}\n"
                        f"3. {ls[3]}\n"
                        f"0. {ls[0]}\n"
                        "Выберете пункт меню:  "))
    except ValueError:
        return -1, None
    else:
        return num, ls.get(num)


if __name__ == "__main__":
    menu()
