# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# кормить
# корову и коз доить, овец стричь, собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)
#
# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными
# и дополнить их в дочерних классах, если потребуется.
#
# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и
# подоить/постричь/собрать яйца, если надо.
#
# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

# import random

class farm_animals:
    type_ = ''
    name = 'animal'
    # condition = 'living' # 'dead'
    # health = 'good' # 'bad'
    weight = 0 # kg
    size = 'small' # all burn small (small, medium, large, huge)
    voice = ''
    color = ''
    satiety = 'low' # сытость low, medium, high
    return_animal = ''
    return_animal_num = 0
    # position = 'farm' # stall, pasture, farm

    def feeding_high(self):
        self.satiety = 'high'
        self.weight = self.weight * 1.26
        print(f'Животное типа "{self.type_}" по имени {self.name.capitalize()} покормили с лихвой!')

    def feeding_medium(self):
        self.satiety = 'medium'
        self.weight = self.weight * 1.13
        print(f'Животное типа "{self.type_}" по имени {self.name.capitalize()} покормили в меру. '
              f'Не забудьте покормить позже.')

    def time(self, hours):
        """
        Указываается время прошедшее с момента последнего кормления животного.

        :param hours:
        :return:
        """
        if hours < 2:
            self.satiety = 'high'
            self.weight = self.weight * 0.96
        elif 2 <= hours < 4:
            self.satiety = 'high'
            self.weight = self.weight * 0.93
        elif 4 <= hours < 6:
            self.satiety = 'medium'
            self.weight = self.weight * 0.89
            print(f'Животное {self.name.capitalize()} можно покормить.')
        elif 6 <= hours < 8:
            self.satiety = 'medium'
            self.weight = self.weight * 0.86
            print(f'Животное {self.name.capitalize()} пора бы покормить.')
        elif 8 <= hours < 10:
            self.satiety = 'medium'
            self.weight = self.weight * 0.83
            print(f'Животное {self.name.capitalize()} пора покормить!')
        elif 10 <= hours < 12:
            self.satiety = 'low'
            self.weight = self.weight * 0.80
            print(f'Животное {self.name.capitalize()} надо скорее покормить!')
        elif 14 <= hours < 16:
            self.satiety = 'low'
            self.weight = self.weight * 0.76
            print(f'Животное {self.name.capitalize()} необходимо немедленно покормить!')
        elif 16 <= hours < 18:
            self.satiety = 'low'
            self.weight = self.weight * 0.73
        else:
            print(f'Внимание!!! Необходимо срочно покормить {self.name}!!! Животное мучается от голода!')

    def touch(self):
        print(f'{self.type_.capitalize()} {self.name.capitalize()} говорит тебе {self.voice.upper()}!!!')

    def get(self, numb):
        """
        вот тут хотелось бы услышать мнение проверяющего - верно ли так делать как я здесь?
        задавать подобные условия в родительском классе (упоминая дочерние классы)?
        не вернее ли указать это отдельно в каждом  дочернем классе?...

        :param numb:
        :return:
        """
        self.return_animal_num += numb
        if isinstance(self, birds):
            print(f'{self.type_.capitalize()} по имени {self.name.capitalize()} дал(а) {self.return_animal_num} шт. '
                  f'{self.return_animal.replace("йца","иц")}')
        elif isinstance(self, cow):
            print(f'{self.type_.capitalize()} по имени {self.name.capitalize()} дал(а) {self.return_animal_num} литров '
                  f'{self.return_animal.replace("ко", "ка")}')
        elif isinstance(self, goat):
            print(f'{self.type_.capitalize()} по имени {self.name.capitalize()} дал(а) {self.return_animal_num} литров '
                  f'{self.return_animal.replace("ко", "ка")}')
        elif isinstance(self, sheep):
            print(f'{self.type_.capitalize()} по имени {self.name.capitalize()} дал(а) {self.return_animal_num} кг '
                  f'{self.return_animal.replace("ть", "ти")}')
        else:
            print(f'{self.type_.capitalize()} по имени {self.name.capitalize()} дал(а) {self.return_animal_num} '
                  f'единиц типа {self.return_animal}')

class horns_hoofs(farm_animals):
    # def __init__(self):
        color = ['brown', 'black', 'white', 'spotted']
        size = ['medium', 'large','huge']
        return_animal = 'milk', 'wool'

class cow(horns_hoofs, farm_animals):
    def __init__(self):
        self.type_ = 'корова'
        self.color = 'коричневая'
        self.voice = 'муууу'
        self.weight = 400
        self.size = 'huge'
        self.return_animal = 'молоко'

class sheep(horns_hoofs, farm_animals):
    def __init__(self):
        self.type_ = 'овца'
        self.color = 'белая'
        self.voice = 'бээээээ'
        self.weight = 90
        self.size = 'large'
        self.return_animal = 'шерсть' # 'milk' too, но тут овец не принято доить......

class goat(horns_hoofs, farm_animals):
    def __init__(self):
        self.type_ = 'коза'
        self.color = 'черный'
        self.voice = 'меееее'
        self.weight = 60
        self.size = 'medium'
        self.return_animal = 'молоко'

class birds(farm_animals):
    color = 'white', 'grey', 'multicolored'
    size = 'small'
    return_animal = 'яйца'

class goose(birds, farm_animals):
    def __init__(self):
        self.type_ = 'гусь'
        self.color = 'серый'
        self.voice = 'га-га-га'
        self.weight = 7

class chicken(birds, farm_animals):
    def __init__(self):
        self.type_ = 'курица'
        self.color = 'белая'
        self.voice = 'паа-паа-па'
        self.weight = 2

class duck(birds, farm_animals):
    def __init__(self):
        self.type_ = 'утка'
        self.color = 'разноцветная'
        self.voice = 'кря-кря-кря'
        self.weight = 4


cow_1 = cow()
cow_1.name = 'Манька'
sheep_1 = sheep()
sheep_1.name = 'Барашек'
sheep_1.weight = 95
sheep_2 = sheep()
sheep_2.name = 'Кудрявый'
sheep_2.weight = 85
goat_1 = goat()
goat_1.name = 'Рога'
goat_1.weight = 57
goat_2 = goat()
goat_2.name = 'Копыта'
goose_1 = goose()
goose_1.name = 'Серый'
goose_1.weight = 6.5
goose_2 = goose()
goose_2.name = 'Белый'
chicken_1 = chicken()
chicken_1.name = 'Ко-ко'
chicken_2 = chicken()
chicken_2.name = 'Кукареку'
duck_1 = duck()
duck_1.name = 'Кряква'


cow_1.get(12)
sheep_1.get(7)
sheep_2.get(10)
goat_1.get(1.5)
goat_2.get(2)
goose_1.get(2)
goose_2.get(1)
chicken_1.get(2)
chicken_2.get(1)
duck_1.get(2)

# визуальный разделитель
print('\n=====================================\n')

cow_1.touch()
sheep_1.touch()
sheep_2.touch()
goat_1.touch()
goat_2.touch()
goose_1.touch()
goose_2.touch()
chicken_1.touch()
chicken_2.touch()
duck_1.touch()

# визуальный разделитель
print('\n=====================================\n')

animals = [sheep_1, sheep_2, goat_1, goat_2, cow_1, goose_1, goose_2, chicken_1, chicken_2, duck_1]

weight_0 = 0
for animal in animals:
    weight_0 += animal.weight
print(f'Общий вес всех животных равен {weight_0} кг')

weight_1 = 0
name_1 = ''
type_1 = ''
for animal in animals:
    if weight_1 < animal.weight:
        weight_1 = animal.weight
        type_1 = animal.type_
        name_1 = animal.name
        continue
print('\nСамое тяжелое животное {} по имени {} c весом {} кг'.format(type_1, name_1, weight_1))
