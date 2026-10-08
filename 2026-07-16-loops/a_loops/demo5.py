import random

my_list = []
size = 10


while len(my_list) < size:
    my_list.append(random.randint(10, 99))

print(my_list)
