

def del_rep_num(arr):
    win = []
    sisi = []
    for i in arr:
        if i not in win:
            win.append(i)
        else:
            sisi.append('_')

    join = win + sisi
    return ' '.join(str(el) for el in join)

if __name__=='__main__':
    b = '0 0 1 1 1 2 2 3 3 4'
    # n = int(input())  # количество чисел для сортировки
    # b = input()
    arr = list(map(int, b.split()))
    print(del_rep_num(arr))
