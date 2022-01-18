import requests
from bs4 import BeautifulSoup
import json
import csv
import random
from time import sleep

#  **** 1 *******

# url = "https://health-diet.ru/table_calorie/"
#
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"
}
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)
#
# with open('index.html', "w", encoding="utf-8") as file:
#     file.write(src)

#  ****** 2 *******

# with open("index.html", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# all_prod_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_cats_dict = {}
# for item in all_prod_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#     all_cats_dict[item_text] = item_href
#
# with open("all_cats_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_cats_dict, file, ensure_ascii=False, indent=4)

with open("all_cats_dict.json", encoding="utf-8") as file:
    all_cats = json.load(file)

iteration_count = int(len(all_cats)) - 1
count = 0
print(f"Всего итераций: {iteration_count}")

for cats_name, cats_href in all_cats.items():

    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in cats_name:
            cats_name = cats_name.replace(item, "_")

    req = requests.get(url=cats_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{cats_name}.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open(f"data/{count}_{cats_name}.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    # проверка страницы на наличие таблицы с продуктами
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    # собираем заголовки таблицы
    table_head = soup.find(class_='mzr-tc-group-table').find("tr").find_all("th")
    print(table_head)
    products = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f"data/{count}_{cats_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                products,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    # собираем данные продуктов
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
    product_info = []
    for item in products_data:
        product_tds = item.find_all("td")

        title = product_tds[0].find("a").text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        with open(f"data/{count}_{cats_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
    with open(f"data/{count}_{cats_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Итерация {count}. {cats_name} записан...")
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print("Работа завершена")
        break

    print(f"Осталось итераций: {iteration_count}")
    sleep(random.randrange(2, 4))
