aaa = '5 3 2 6 0 5 3 3 5 9 10 2 8 10'
bbb = '5 3 2 6 0'


# a_number = int(input())
b_list: list = list(map(int, sorted(aaa.split())))
# c_number = int(input())
d_list: list = list(map(int, (bbb.split())))


# Подсчитываем количество каждого элемента в списке b
b_dict = {}
for elem in b_list:
    if elem not in b_dict:
        b_dict[elem] = 0
    b_dict[elem] += 1

sorted_b = []  # Отсортированный список b

# Добавляем элементы согласно порядку из списка d
for elem in d_list:
    if elem in b_dict and b_dict[elem] > 0:
        sorted_b.extend([elem] * b_dict[elem])
        b_dict.pop(elem)

# Добавляем оставшиеся элементы из b
for elem, count in sorted(b_dict.items()):
    sorted_b.extend([elem] * count)
# return ' '.join(map(str, b_numbers_to_sort))
print(' '.join(map(str, sorted_b)))