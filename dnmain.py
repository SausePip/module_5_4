class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if len(args) > 0:
            name = args[0]
            cls.houses_history.append(name)
        return instance

        #     одинаковые названия?

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, House):
            new_name = f'{self.name} + {other.name}'
            new_floors = self.number_of_floors + other.number_of_floors
            return House(new_name, new_floors)
        elif isinstance(other, int):
            new_name = self.name
            new_floors = self.number_of_floors + other
            return House(new_name, new_floors)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            self.name = f'{self.name} + {other.name}'
        elif isinstance(other, House):
            self.number_of_floors += other
        else:
            return NotImplemented
        return self

    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


