"""
Распределяем образцы между заказчиками оптимальным образом — так,
чтобы выполнить требования максимального числа заказчиков.
Требование заказчика считается выполненным, если он получит образец,
вес которого равен заказанному или превышает заказанный вес.
Программа должна возвращает число заказчиков, которые получили образцы,
соответствующие их требованиям. Булыжники нельзя дробить на части,
а каждый заказчик может получить только по одному образцу.
"""
number_ordered = 10
aa = '8 5 5 8 6 9 8 2 4 7'
number_delivered = 8
ss = '9 8 1 1 1 5 10 8'

ordered: list = list(map(int, sorted(aa.split())))
deli: list = list(map(int, ss.split()))
delivered = sorted(deli)

# number_ordered = int(input())  # Получаем количество заказанных камней
# ordered: list = list(map(int, sorted(input().split())))  # Список заказа веса камней
# number_delivered = int(input())  # Количество камней полученных по факту
# delivered: list = list(map(int, sorted(input().split())))  # Список веса камней

def space_delivery(ordered, delivered):
    min_block_count = 0  # Количество блоков
    ord = 0
    deli_pointer = 0

    while ord < len(ordered) and deli_pointer < len(delivered):
        if ordered[ord] <= delivered[deli_pointer]:
            min_block_count += 1
            ord += 1
        deli_pointer += 1

    return min_block_count

print(space_delivery(sorted(ordered), sorted(delivered)))
