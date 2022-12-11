# 3. Создайте программу для игры в ""Крестики-нолики"".

#box = [
#    [0,0,0],
#    [0,0,0],
#    [0,0,0]
#    ]

#def print_box(func_box: list) -> str:
#    return "{func_box[0]},{func_box[1]},{func_box[2]},\n,{func_box[3]},{func_box[4]},{func_box[5]}\n{func_box[6]},{func_box[7]},{func_box[8]}"

#print(box)

import copy
import fnmatch

mas = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
       ]

# вывод массива
def print_box(func_box: list) -> str:
    for i in func_box: 
        print(' '.join(list(map(str, i))))
    print('\n')

# заполнение массива
def init_box(func_box: list, number: int) -> list:
    for i in range(len(func_box)):
        for j in range(len(func_box[i])): 
            #print(func_box[i][j])
            func_box[i][j] = number
            ...
    return func_box

def dict_elements(func_box: list, number: int) -> list:
    number = 5
    match int(number):
        case 1:
            print('!!!')
        case 2:
            print('!!!')
        case _:
            print("!!!")
    return func_box

print(dict_elements)
print_box(mas)
b = []
b = copy.deepcopy(mas)
print_box(init_box(b,5))
print_box(mas)