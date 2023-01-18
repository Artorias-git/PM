import matrix.matrix_logic as mat

def join_add_matrix(arr, add):
    """приклеить добавочную часть"""
    cop_arr = mat.copy2d(arr)
    for i in range(len(cop_arr)):
        if type(add[i]) == int: add[i] = [add[i]]
        cop_arr[i] = cop_arr[i] + add[i]
    return cop_arr

def creat_e(n):
    """создать единичную матрицу
    :param n: Размер arr
    """
    e = mat.create_new_matrix(n, n)
    for i in range(n):
      e[i][i] = 1
    return e

def input_for_roots(matr, b):
    """создаёт добавочную часть из списка b"""
    cop = mat.copy2d(matr)
    for i in range(len(cop)):
        cop[i].append(b[i])
    return cop

def input_for_reverse(matr, block):
    """создаёт добавочную часть из единичной матрицы"""
    cop = mat.copy2d(matr)
    for i in range(len(cop)):
        for j in range(block):
            cop[i].append(0)
        cop[i][i + block] = 1
    return cop

def swap_row_if_necessity(i, arr):
    """меняет строки местами, если ведущий элемент равен 0"""
    if arr[i][i] == 0:
        if i + 1 >= len(arr):
            idx2 = i - 1
        else:
            idx2 = i + 1
        mat.swap_row(arr, i, idx2)

def jordan_gauss(matrix, do_copu = True):
    """метод Жордана-Гаусса (с добавочной частью)
    :param arr: разширенная матрица
    """
    arr = mat.copy2d(matrix)
    for i in range(len(arr)):
        swap_row_if_necessity(i, arr)
        pick = arr[i][i] # берём направляющую строки
        arr = mat.multiply_by_scal(arr, pick ** -1) #деление матрицы на направляющую
        for j in range(len(arr)): #обнуление всех элементов столбца i, кроме строки j
            if j != i:
                arr = mat.difference_mul_row(arr, j, i, arr[j][i])

    for i in range(len(arr)): #приведение матрицы к единичному виду
        arr = mat.multiply_row_by_scal(arr, i, (arr[i][i] ** -1))
    return arr

def revers(arr, do_cope=True):
    cop = mat.copy2d(arr)
    cop = join_add_matrix(cop, creat_e(len(arr)))
    revers_matrix = jordan_gauss(cop)
    for i in range(len(arr)):
        revers_matrix[i] = revers_matrix[i][len(arr):]
    return revers_matrix


def roots(arr, b, do_copy=True):
    cop = mat.copy2d(arr)
    cop = join_add_matrix(cop, b)
    jg = jordan_gauss(cop)
    res = []
    for i in range(len(jg)):
        res.append(jg[i][len(arr)])
    return res

def roots_by_revers(arr, b):
    revered = revers(arr)
    res = []
    for i in range(len(revered)):
        sum = 0
        for j in range(len(b)):
            sum += revered[i][j] * b[j]
        res.append(sum)
    return res


