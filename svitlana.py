occupied = []  # список клітинок 

while True:  # цикл 
    
    # 1 крок 
    # хід 
    coordinates = input("Твій хід (наприклад, 11, 23, 32): ")
    
    # 2 крок перевірки
    # перевірка на двоцифрове число
    if not (coordinates.isdigit() and len(coordinates) == 2):
        print(" Помилка Введи рівно дві цифри")
        continue 
    
    # Перевірка на правильність кординат
    if coordinates[0] not in '123' or coordinates[1] not in '123':
        print(" Помилка тільки цифри 1, 2, 3")
        continue
    
    # перевірка на зайнятість
    if coordinates in occupied:
        print(" Ця клітинка вже зайнята спробуй іншу")
        continue
    
    #обробка ходу 
    occupied.append(coordinates) 
    
    # 
    num = int(coordinates) 
    line = num % 10         
    column = num // 10      

    if len(occupied) == 9:
        print("Всі клітинки зайняті")
        break

    # результат 

    print(f" Колонка {column}, рядок {line}")
    
    # print(f" Зайняті клітинки: {occupied}")
    # print("-" * 40)  # для краси