class House:  # создаем свой класс  "House"
    def __init__(self, name, number_of_floors):
        self.name = name  # создаем имена для домов которые мы укажем сами при вызове функции(метода)
        self.number_of_floors = number_of_floors  # создаем количество этажей для домов

    def go_to(self, new_floor):  # создаем новую функцию для новых этажей
        if new_floor > self.number_of_floors or new_floor < 1:  # условие при котором если если new_floor больше self.number_of_floors
            # или new_floor меньше одного, то програма будет выводить что не существует столько этажей
            print('Такого этажа не существует')
        else:
            count = 1  # создаеv счестик для будущего цикла while
            while count <= new_floor:
                print(count)
                count += 1

    def __len__(self):  # создаем функцию def с счетчиком которое будет выводить количество этажей
        return self.number_of_floors

    def __str__(self):  # создаем опять же таки функцию def которая будет выводить форматированную строку fкоторая будет выводить строку ниже
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)     # __eq__

h1 = h1 + 10    # __add__
print(h1)
print(h1 == h2)

h1 += 10    # __iadd__
print(h1)

h2 = 10 + h2    # __radd__
print(h2)

print(h1 > h2)      # __gt__
print(h1 >= h2)     # __ge__
print(h1 < h2)      # __lt__
print(h1 <= h2)     # __le__
print(h1 != h2)     # __ne__
