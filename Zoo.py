from math import ceil
from random import randint

class Animal:
    def __init__(self, name, pet_type):
        self.name = name
        self.hunger = 100
        self.pet_type = pet_type
        if self.pet_type == '':
            self.pet_type = 'Нету'


    def starvation(self):
        self.hunger -= randint(7, 19)


    def feed(self):
        if self.hunger <= 90:
            self.hunger += randint(9,13)
        else:
            self.hunger = 100


    def make_sound(self):
        print('мяу гаф грр?')


    def info(self):
        print(f'имя питомца: {self.name}, семейство питомца: {self.pet_type}, '
              f'сытость питомца: [{ceil(self.hunger/10) * '⏹'}{'•' * (10 - ceil(self.hunger / 10))}/{10 * '⏹'}]' )


class Cat(Animal):
    def make_sound(self):
        print("Мяу мррр мррр")


class Wolf(Animal):
    def make_sound(self):
        print("Гаф гаф гаф")


class Bear(Animal):
    def make_sound(self):
        print("Гррр гррр рр")


def pet_choose():
    if ANIMALS == []: print("В вольере некого нет")
    else:
        for i in ANIMALS: print(i.name, end=' ')


ANIMALS = []


while True:
    player_choose = input("""Выберите действие:
1) Добавить животное в зоопарк
2) Вывести информацию о животном
3) Погладить животное
4) Покормить животное
5) Пропустить день
6) Выйти
""")
    if player_choose == '1':
        name = input("Введите имя питомца: ")
        pet_type = input("Введите семейство (например, кошачьи): ")
        if pet_type == 'кошачьи':
            animal = Cat(name, pet_type)
        elif pet_type == "собачьи":
            animal = Wolf(name, pet_type)
        elif pet_type == "медвежьи":
            animal = Bear(name, pet_type)
        else:
            animal = Animal(name, pet_type)
        ANIMALS.append(animal)
    elif player_choose == '2':
        pet_choose()
        animal_choose = input('\nВведите имя животного, о котором хотите узнать\n')
        for i in range(len(ANIMALS)):
            if animal_choose == ANIMALS[i].name:
                ANIMALS[i].info()
                break
            else:
                print("Животное не найдено")
    elif player_choose == '3':
        pet_choose()
        animal_choose = input('\nВведите имя животного, которого хотите погладить\n')
        for i in range(len(ANIMALS)):
            if animal_choose == ANIMALS[i].name:
                ANIMALS[i].make_sound()
                break
            else:
                print("Животное не найдено")
    elif player_choose == '4':
        pet_choose()
        animal_choose = input('\nВведите имя животного, которого хотите покормить\n')
        for i in range(len(ANIMALS)):
            if animal_choose == ANIMALS[i].name:
                ANIMALS[i].feed()
                print(f'{ANIMALS[i].name}: [{ceil(ANIMALS[i].hunger / 10) * '⏹'}{'•' * (10 - ceil(ANIMALS[i].hunger / 10))}/{10 * '⏹'}]')
                break
            else:
                print("Животное не найдено")
    elif player_choose == '5':
        for i in range(len(ANIMALS)):
            ANIMALS[i].starvation()
        for i in range(len(ANIMALS)):
            print(f'{ANIMALS[i].name}: [{ceil(ANIMALS[i].hunger/10) * '⏹'}{'•' * (10 - ceil(ANIMALS[i].hunger / 10))}/{10 * '⏹'}]')
    else:
        break


