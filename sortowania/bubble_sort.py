import random

my_numbers = []
for i in range(100):
    my_numbers.append(random.randint(1, 1001))

for j in range(0, len(my_numbers)):
    for k in range(0, len(my_numbers) - 1):
        if my_numbers[k] > my_numbers[k + 1]:
            my_numbers[k], my_numbers[k + 1] = my_numbers[k + 1], my_numbers[k]

print(my_numbers)
