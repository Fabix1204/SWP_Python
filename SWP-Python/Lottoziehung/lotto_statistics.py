import random

statistics = {i:0 for i in range(1, 46)}

def draw():
    numbers = list(range(1, 46))
    lotto_list = []
    for i in range(6):
        rand = random.randint(0, 44 - i)
        lotto_list.append(numbers[rand])
        statistic_method(lotto_list[i])
        numbers[rand], numbers[44 - i] = numbers[44 - i], numbers[rand]
    return lotto_list

def statistic_method(number):
    statistics[number] += 1

for i in range(1000):
    draw()
print(statistics)