# Ex 1
import json

prod_list = []
price_list = []
while True:
    prod_ = input('назание товара: ')
    if prod_ == 'стоп':
        break
    else:
        price_ = int(input('стоимость товара: '))
        prod_list.append(prod_)
        price_list.append(price_)
        obj = dict(zip(prod_list, price_list))
    with open('data_15.json', 'w', encoding='UTF-8') as file:
        json.dump(obj, file, ensure_ascii=False)

# Ex.2
with open('data_15.json', 'r', encoding='UTF-8') as file_1:
    product = json.load(file_1)
    sum_ = 0
    for value in product.values():
        sum_ += int(value)
    print(f'сумма  покупок равна {sum_}')
