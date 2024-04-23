a = '10'
b = '2 2 4 7 7 8 1 0 2 9 8 2 3 5 2 7 7'
c = '6'
d = '2 4 3 5 6 0'

a_number = int(a)
b_numbers_to_sort: list = list(map(int, b.split()))
c_number = int(c)
d_numbers_to_sort: list = list(map(int, d.split()))
# print(a_number)
# print(b_numbers_to_sort)
# print(c_number)
# print(d_numbers_to_sort)

# a_number = int(input())
# b_numbers_to_sort: list = list(map(int, sorted(input().split())))
# c_number = int(input())
# d_numbers_to_sort: list = list(map(int, reversed(input().split())))

def insertion_sort(a_number, b_numbers_to_sort, c_number, d_numbers_to_sort):
    for i in range(1, c_number):
        current = d_numbers_to_sort[i]
        prev = i - 1
        per =


        while prev >= 0 or b_numbers_to_sort[prev] != current:
            b_numbers_to_sort[prev + 1] = b_numbers_to_sort[prev]
            prev -= 1
        b_numbers_to_sort[prev + 1] = current

    return ' '.join(map(str, b_numbers_to_sort))


print(insertion_sort(a_number, b_numbers_to_sort, c_number, d_numbers_to_sort))
