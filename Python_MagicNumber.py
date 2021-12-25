import random

def is_valid_input(element):
    if element.isdigit():
        return True
    else:
        return False

def user_input():
    number = input("Введите число: ")
    while not is_valid_input(number):
        number = input("Введите число: ")
    return int(number)

def begin_game(magic_number_min, magic_number_max):
    magic_number = random.randint(magic_number_min, magic_number_max)
    print(f"Я загадал случайное число от {magic_number_min} до {magic_number_max}")

    user_number = user_input()
    while user_number != magic_number:
        if user_number > magic_number:
            print(f"{user_number} больше моего числа")
        else:
            print(f"{user_number} меньше моего числа")
        user_number = user_input()
    print(f"Ты угадал число! Это {magic_number}")

def is_valid_difficulty(element):
    if element.isdigit() and int(element) >= 1 and int(element) <= 4:
        return True
    else:
        return False

def choose_difficulty(difficulty):
    if difficulty == 1:
        return 1, 100
    elif difficulty == 2:
        return 1, 1_000
    elif difficulty == 3:
        return 1, 10_000
    elif difficulty == 4:
        return 1, 100_000

def select_difficulty():
    print("1 - Легко")
    print("2 - Средне")
    print("3 - Тяжело")
    print("4 - Очень тяжело")
    difficulty = input("Выбери сложность: ")
    while not is_valid_difficulty(difficulty):
        difficulty = input("Выбери сложность: ")
    return choose_difficulty(int(difficulty))

def game():
    magic_number_min, magic_number_max = select_difficulty()
    begin_game(magic_number_min, magic_number_max)

game()
