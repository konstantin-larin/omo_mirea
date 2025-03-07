from itertools import product
import numpy as np



def pascal_triangle(n):
    triangle = []
    for i in range(n):
        prev_row = triangle[i - 1] if i > 0 else []
        current_row = []

        for j in range(i + 1):
            num = 0
            if j == 0 or j > len(prev_row) - 1:
                num = 1
            else:
                num = prev_row[j - 1] + prev_row[j]
            current_row.append(num)
        triangle.append(current_row)

    return triangle
def print_pascal_triangle(n):
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)
# print_pascal_triangle(5)

def digits_plus(m):
    digits = '123456789'
    operators = ["+", "-", ""]
    for ops in product(operators, repeat=len(digits) - 1):
        expression = "".join(d + op for d, op in zip(digits, ops)) + digits[-1]
        if eval(expression) == m:
            return expression
    return "Нет решения"

# print(digits_plus(45))
# print(digits_plus(100))
# print(digits_plus(200))
def inverse_matrix():
    n = int(input("Введите размер матрицы: "))
    elements = np.empty((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            num = int(input("Введите элемент на строке " + str(i + 1) + " столбце " + str(j + 1) + ": "))
            elements[i][j] = num

    return np.linalg.inv(elements)

# print(inverse_matrix())

def ex_4():
    nums = range(64)
    matrix_1 = np.ndarray(shape=(8, 8), dtype='U5')
    matrix_2 = np.ndarray(shape=(8, 8), dtype='U5')

    for num in nums:
        i = num // 8
        j = num - i * 8


        matrix_1[j if i % 2 == 0 else 7 - j, i] = (str(num) + ' v' if 7 - j > 0 else ' ->') if i % 2 == 0 else (str(num) + ' ^' if j < 7  else str(num) + ' ->')
        matrix_2[i, 7 - j if i % 2 == 0 else j] = ('<- ' if 7 - j > 0 else 'v ') + str(num) if i % 2 == 0 else str(num) + (' ->' if j < 7 else ' v')

    print("Матрица 1:")
    # print(matrix_1)

    print("Матрица 2:")
    # print(matrix_2)

    matrix_3 = np.zeros(shape=(8, 8), dtype=int)
    tl, br = [0, 0], [7, 7] # с двух краев матрицы ползут змейки
    maxi = 63
    mini = 0

    #[0,0]
    # [0,1] -> [1, 0]
    # [2, 0] -> [0, 2]
    # [0, 3] -> [3, 0]

    #[7, 7]
    #[7, 6] -> [6, 7]
    #[5,7] -> [7,5]
    #[7, 4] -> [4, 7]
    col_to_row = False

    while True:
        matrix_3[tl[0], tl[1]] = mini
        matrix_3[br[0], br[1]] = maxi
        mini += 1
        maxi -= 1

        if col_to_row:
            if tl[1] == 0:
                tl[0] += 1
                br[0] -= 1
                col_to_row = False
                continue
            tl[0] += 1
            tl[1] -= 1

            br[1] += 1
            br[0] -= 1

        else:
            if tl[0] == 0:
                tl[1] += 1
                br[1] -= 1
                col_to_row = True
                continue
            tl[1] += 1
            tl[0] -= 1

            br[0] += 1
            br[1] -= 1

        if mini > maxi:
            break



    # while tl[0] != br[0] or tl[1] != br[1]:
        #ход змейки tl - с позиции [0, 1] должны придти к позиции [1, 0] и тп то есть итеративно одно увеличивается другое уменьшается
        # br - тоже самое только вместо 0 цифра 7
        #при этом

    print("Матрица 3:")
    print(matrix_3)
ex_4()