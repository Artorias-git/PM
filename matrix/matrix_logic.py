import vector.vector_logic as vc

def copy2d(mat, do_copy=True):
    if do_copy:
        new_mat = []
        for i in range(len(mat)):
            new_mat.append(vc.copy1d(mat[i]))
        return new_mat
    return mat

def is_same_size(a, b):
    return len(a) == len(b)

# убрать проверку из функций, оставить только в input_matrix
def is_matrix(a):
    l = len(a[0])
    if l < 2: return False
    for i in a:
        if l != len(i):
            return False
    return True

def is_correct_index(mat, idx):
    """проверка индекса строки на принодлежность к матрице"""
    return 0 <= idx < len(mat)

def create_new_matrix(a, b):
    """создание нулевой матрицы размером a на b"""
    return [[0 for j in range(a)] for i in range(b)]

def addition(mat1, mat2):
    """сложение матриц"""
    new_matrix = []
    if is_same_size(mat1, mat2):
        for i in range(len(mat1)):
            new_matrix.append(vc.summ(mat1[i], mat2[i]))
    return new_matrix

def difference(mat1, mat2):
    """вычитание матриц"""
    new_matrix = []
    if is_same_size(mat1, mat2):
        for i in range(len(mat1)):
            new_matrix.append(vc.diff(mat1[i], mat2[i]))
    return new_matrix

def transposition(mat):
    "Транспонирование матрицы"
    new_matrix = []
    if is_matrix(mat):
        new_matrix = create_new_matrix(len(mat), len(mat[0]))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_matrix[j][i] = mat[i][j]
    return new_matrix

def multiply_by_scal(mat, scal):
    """умножение матрици на скаляр"""
    new_matrix = []
    if is_matrix(mat):
        for i in range(len(mat)):
            new_matrix.append(vc.mult_scal(mat[i], scal))
        return new_matrix

def multiply_matrix(mat1, mat2):
    """умножение матриц"""
    if is_matrix(mat1) and is_matrix(mat2):
        res = create_new_matrix(len(mat2[0]), len(mat1))
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res

def get_row_by_index(mat, idx):
    """Получить строку из матрицы"""
    if is_matrix(mat):
        if is_correct_index(mat, idx):
            return mat[idx]

def get_col_by_index(mat, idx):
    """Получить столбец из матрицы"""
    if is_matrix(mat):
        new_matrix = transposition(mat)
        if is_correct_index(mat, idx):
            return get_row_by_index(new_matrix, idx)

def swap_row(mat, idx1, idx2):
    """Поменять строки местами"""
    if is_matrix(mat):
        if is_correct_index(mat, idx1) and is_correct_index(mat, idx2):
            temp = mat[idx1]
            mat[idx1] = mat[idx2]
            mat[idx2] = temp
            return mat

def multiply_row_by_scal(mat, idx, scal):
    """Умножить строку на скаляр"""
    if is_matrix(mat):
        if is_correct_index(mat, idx):
            mat[idx] = vc.mult_scal(mat[idx], scal)
            return mat

def addition_mul_row(mat, idx1, idx2, scal):
    """сложение строк матрицы с индексами х + у, умноженную на скаляр"""
    if is_matrix(mat):
        if is_correct_index(mat, idx1) and is_correct_index(mat, idx2):
            temp = vc.mult_scal(mat[idx2], scal)
            mat[idx1] = vc.summ(mat[idx1], temp)
            return mat

def difference_mul_row(mat, idx1, idx2, scal):
    """вычитание строк матрицы с индексами х + у, умноженную на скаляр"""
    if is_matrix(mat):
        if is_correct_index(mat, idx1) and is_correct_index(mat, idx2):
            temp = vc.mult_scal(mat[idx2].copy(), scal)
            mat[idx1] = vc.diff(mat[idx1], temp)
            return mat

def printer(mat):
    """выводит матрицу"""
    for i in range(len(mat)):
        print(mat[i])
    print("\n")