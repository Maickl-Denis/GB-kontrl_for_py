# -*- coding: utf-8 -*-
import json, time
from datetime import datetime


class Nout:
    def __init__(self):
        self.db = json.load(open('noute_base.json', encoding='utf-8'))

    def add_nout(self):

        print("Новая заметка")

        result = {self.db["__service_tag__"]["count"]: {
            "title": input("Введите название заметки: "),
            "text": input("Введите текст заметки: "),
            "create": datetime.now().strftime("%Y-%m-%d"),
            "update": None}}

        self.db.update(result)
        self.db["__service_tag__"]["count"]+=1

    def save_db(self):
        print("Данные сохраняются")
        with open('noute_base.json', 'w', encoding='utf-8') as file:
            json.dump(self.db, file, indent=4, ensure_ascii=False)
        time.sleep(1)

    def print(self):
        print(f"_____________________\nID\t|\tНаименнование\n---------------------")
        for nout in range(0, len(self.db)-1):
            print(f"{nout}\t|\t{self.db[str(nout)]['title']}")
        print(f"---------------------")
        # print([self.db[str(nout)] for nout in range(0, len(self.db)-1)])

if __name__ == '__main__':
    n = Nout()
    n.print()
