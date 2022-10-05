from cities import all_cities


def city_game(all_cities, current_city, unused_cities):
    unused_cities = all_cities
    count = 1
    while True:
        try:
            current_city, unused_cities = select_city(current_city, unused_cities)
            count += 1
        except:
            break
    print(f"Мы использовали {count} город(а/ов)")
    print("Остальные города не подходят.")


def select_city(current_city, unused_cities):
    for city in unused_cities:
        if (
            city[0].lower() == current_city[-1]
            or current_city[-2 : len(city)] == "ый"
            and city[0].lower() == current_city[-3]
            or current_city[-1] in "ыйъьц"
            and city[0].lower() == current_city[-2]
        ):
            print(city)
            unused_cities.remove(city)
            return city, unused_cities
        else:
            continue
    print("Игра окончена.")
    return 0


print("Привет, поиграем в города?")
unused_cities = {}
current_city = input("С какого города начнем?")

city_game(all_cities, current_city, unused_cities)
