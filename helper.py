# -*- coding: utf-8 -*-
import json, time, os
from datetime import datetime


class Nout:
    def __init__(self):
        self.db = self.load_db()

    def load_db(self):
        return json.load(open('noute_base.json', encoding='utf-8'))

    def add_nout(self):

        print("Новая заметка")

        result = {self.db["__service_tag__"]["count"]: {
            "title": input("Введите название заметки: "),
            "text": input("Введите текст заметки: "),
            "create": datetime.now().strftime("%Y-%m-%d"),
            "update": None}}
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Заметка  {result[self.db['__service_tag__']['count']]['title']} добавлена")
        self.db.update(result)
        self.db["__service_tag__"]["count"]+=1

    def save_db(self):
        for i in range(4, 0, -1):
            print(f"\rДанные сохраняются..{i}", end='')
            time.sleep(0.33)
        with open('noute_base.json', 'w', encoding='utf-8') as file:
            json.dump(self.db, file, indent=4, ensure_ascii=False)


    def print(self):
        print(f"_____________________________\nID\t|Наименнование\n-----------------------------")
        for nout in range(1, len(self.db)):
            print(f"{nout}\t|{self.db[str(nout)]['title']}")
        print(f"-----------------------------")

    def read_nout(self, id):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.db.get(str(id)) and id != "__service_tag__":
            print(f"Заметка: {self.db[str(id)]['title']}\n-----------------------------\n{self.db[str(id)]['text']}\n\n"
                  f"Заметка создана: {self.db[str(id)]['create']}\n"
                  f"Заметка изменена: {self.db[str(id)]['update']}")
            input("Для продолжения работы нажмите любую клавишу...")
        else:
            input("Данная заметка не обнаружена.\nДля продолжения работы нажмите любую клавишу...")

    def del_nout(self, id):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.db.get(str(id)) and id != "__service_tag__":
            input(f"Заметка: {self.db[str(id)]['title']}, удалена!\nДля продолжения работы нажмите любую клавишу...")
            del self.db[str(id)]
        else:
            input("Данная заметка не обнаружена.\nДля продолжения работы нажмите любую клавишу...")

    def edit_nout(self, id):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.db.get(str(id)) and id != "__service_tag__":
            print(f"Заметка: {self.db[str(id)]['title']}\n-----------------------------")
            num = input(f"Что вы хотите изменить?\n\n1. Изменить название\n2. Изменить текст\n\n"
                        f"или введите любой символ для отмены\n\nВыберете пункт меню:  ")
            if num in ['1', '2']:
                match num:
                    case '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Старое название заметки: {self.db[str(id)]['title']}\n-----------------------------")
                        self.db[str(id)]['title'] = input("Введите новое название для заметки: ")
                        self.db[str(id)]['update'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    case '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Старый текст заметки:\n{self.db[str(id)]['text']}\n-----------------------------")
                        self.db[str(id)]['text'] = input("Введите новый текст заметки: \n")
                        self.db[str(id)]['update'] = datetime.now().strftime("%Y-%m-%d %H:%M")
            else:
                print("down")

        else:
            input("Данная заметка не обнаружена.\nДля продолжения работы нажмите любую клавишу...")

if __name__ == '__main__':
    n = Nout()
    n.edit_nout(1)
    # n.edit_nout(2)
    # n.edit_nout(13)
    # n.edit_nout("__service_tag__")

