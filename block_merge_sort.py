a = '9 23 13 2 22 5 14 17 21 19 6 12 4 1 20 3 7 15 0 10 18 11 8 16'
nb = '24'
def max_blocks(arr):
    n = len(arr)
    max_block_count = 0  # Количество блоков
    current_max = 0  # Максимальное значение в текущем блоке

    for i in range(n):
        current_max = max(current_max, arr[i])
        # Если индекс достиг максимального значения в текущем блоке,
        # это означает, что мы можем завершить блок здесь.
        if current_max == i:
            max_block_count += 1
            current_max = 0  # Сброс для следующего блока, если он есть

    return max_block_count


# Чтение ввода пользователя
n = int(nb)  # количество чисел для сортировки
arr = list(map(int, a.split()))  # числа для сортировки

# Вывод результата
print(max_blocks(arr))