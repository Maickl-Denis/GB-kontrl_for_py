# -*- coding: utf-8 -*-
import os
from helper import Nout
def menu():
    n = Nout()
    print("Привет ты в программе заметки в консоли")
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
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
                    # Список с фильтрами
                    case 2:
                        pass
                    # Редактировать заметку
                    case 3:
                        pass
                    # Удалить заметку
                    case 4:
                        pass
                    case 0:
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
                break

def first_menu():
    try:
        ls = {1: "Читать заметки", 2: "Добавить заметку", 3: "Сохранить все изменения", 0: "Выход"}
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
        ls = {1: "Показать список заметок", 2: "Показать список заметок с фильтрами", 3: "Редактировать заметку",
              4: "Удалить заметку", 0: "Выход"}
        num = int(input(f"1. {ls[1]}\n"
                        f"2. {ls[2]}\n"
                        f"3. {ls[3]}\n"
                        f"4. {ls[4]}\n"
                        f"0. {ls[0]}\n"
                        "Выберете пункт меню:  "))
    except ValueError:
        return -1, None
    else:
        return num, ls.get(num)


if __name__ == "__main__":
    menu()

    # 3: "Читать заметку", 4: "Редактировать заметку",
    # 5: "Удалить заметку",