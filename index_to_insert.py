def find_element(sorted_numbers, element):
    left, right = 0, len(sorted_numbers) - 1

    if element == sorted_numbers[0]:
        return 0
    if element < sorted_numbers[0]:
        return 0
    if element > sorted_numbers[-1]:
        return len(sorted_numbers)

    while left <= right:
        mid = left + (right - left) // 2
        if sorted_numbers[mid] == element:
            return mid
        elif sorted_numbers[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    return left

if __name__=='__main__':
    massive = '5 5 5 5'
    number_to_search = 5 # int(input())  # количество чисел для сортировки
    # b = input()
    arr = list(map(int, massive.split()))
    print(find_element(arr, number_to_search))