# file = open('recipes.txt', 'rt', encoding='utf-8')
# result = file.read()
# print(result)
# print(type(result))
# file.close()

from pprint import pprint
with open('venv/recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        prod_count = int(file.readline())
        list_ingrid = []
        for _ in range(prod_count):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            list_ingrid.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish] = list_ingrid
    pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for i in cook_book[dish]:
            i['quantity'] = int(i['quantity']) * person_count
            ingredients = i.pop('ingredient_name')
            shop_list[ingredients] = i
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))