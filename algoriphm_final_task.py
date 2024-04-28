# ID посылки 113149185

short_command = str(input())


def encrypted_instruction(command) -> str:
    """
    Функция принимает строку содержащую зашифрованную инструкцию.
    Возвращается расшифрованная строка с командами без скобок и чисел.
    """
    stack = []
    for char in command:  # Поиск коротких команд до ]
        if char != ']':
            stack.append(char)
        else:
            substring = ''
            while stack[-1] != '[':  # Подготовка команд
                substring = stack.pop() + substring
            stack.pop()  # Удаляет открывающую скобку

            repeat_count = ''
            while stack and stack[-1].isdigit():  # Проверка готовности к умножению
                repeat_count = stack.pop() + repeat_count

            stack.append(substring * int(repeat_count))

    return ''.join(stack)

print(encrypted_instruction(short_command))
