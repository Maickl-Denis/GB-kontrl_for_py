import json
from menu import menu



if __name__ == '__main__':
    try:
        if json.load(open('noute_base.json', encoding='utf-8')):
            pass
    except:
        result = {"__service_tag__": {
                    "count": 0}}
        with open('noute_base.json', 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
    menu()