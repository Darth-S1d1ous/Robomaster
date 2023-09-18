import numpy as np

def matrix_input():
    mat = []
    cnt = 0
    i = '0'
    while True:
        lst = input('').split()
        if lst == ['s', 't', 'o', 'p']:
            break
        new_lst = []
        for j in range(0, len(lst)):
            new_lst.append(int(lst[j]))
        lst = new_lst
        mat.append(lst)
        cnt += 1

    print('')
    return mat, cnt

mat_1, cnt_1 = matrix_input()
mat_2, cnt_2 = matrix_input()

print('max_position of the first matrix:', end = ' ')
for i in mat_1:
    index = np.argmax(i)
    print(index + 1, end = ' ')
print('')
print('max_position of the second matrix:', end = ' ')
for i in mat_2:
    index = np.argmax(i)
    print(index + 1, end = ' ')
print('')

res = np.dot(mat_1, mat_2)
print('multiplication result: ')
for i in range(cnt_1):
    for j in range(cnt_1):
        print(res[i][j], end = ' ')
    print('')