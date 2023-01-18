import matrix.matrix_logic as mc

def test_addition():
    """Тест сложения матриц"""
    assert mc.addition([[1, 2],[3, 4]], [[3, 4], [1 ,1]]) == [[4, 6], [4, 5]], "Should be [[4, 6], [4, 5]]"

def test_addition2():
    """Тест сложения матриц"""
    assert mc.addition([[1, 2]], [[3, 4], [1 ,1]]) == [], "Should be []"

def test_difference():
    """Тест вычитания матриц"""
    assert mc.difference([[1, 2]], [[3, 4], [1 ,1]]) == [], "Should be []"

def test_difference2():
    """Тест вычитания матриц"""
    assert mc.difference([[1, 2],[3, 4]], [[3, 4], [1 ,1]]) == [[-2, -2], [2, 3]], "Should be [[-2, -2], [2, 3]]"

def test_transposition():
    """Тест транспонирование матриц"""
    assert mc.transposition([[2, 3, 5], [5, 7, 6]]) == [[2, 5], [3, 7], [5, 6]], "Should be [[2, 5], [3, 7], [5, 6]]"

def test_transposition2():
    """Тест транспонирование матриц"""
    assert mc.transposition([[2, 3, 5], [5, 7]]) == [], "Should be []"

def test_multiply_by_scal():
    """Тест умножение матрицы на скаляр"""
    assert mc.multiply_by_scal([[2, 3, 5], [5, 7, 6]], 5) == [[10, 15, 25], [25, 35, 30]], "Should be [[10, 15, 25], [25, 35, 30]]"

def test_multiply_by_scal2():
    """Тест умножение матрицы на скаляр"""
    assert mc.multiply_by_scal([[2, 3, 5], [5, 7]], 5) == None, "Should be None"

def test_multiply_by_scal3():
    """Тест умножение матрицы на скаляр"""
    assert mc.multiply_by_scal([[2, 3, 5], [5, 7, 6]], 0) == [[0, 0, 0], [0, 0, 0]], "Should be [[0, 0, 0], [0, 0, 0]]"

def test_multiply_matrix():
    """Тест умножение матрицы на скаляр"""
    assert mc.multiply_matrix([[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10]]) == [[25, 28], [57, 64], [89, 100]], "Should be [[25, 28], [57, 64], [89, 100]]"

def test_multiply_matrix2():
    """Тест умножение матрицы на скаляр"""
    assert mc.multiply_matrix([[1], [3, 4], [5, 6]], [[7, 8], [9, 10]]) == None

def test_get_row_by_index():
    """Тест получить строку по индексу"""
    assert mc.get_row_by_index([[1, 2], [3, 4], [5, 6]],0) == [1, 2]

def test_get_row_by_index2():
    """Тест получить строку по индексу"""
    assert mc.get_row_by_index([[1, 2], [3, 4], [5, 6]],3) == None

def test_get_col_by_index():
    """Тест получить столбец по индексу"""
    assert mc.get_col_by_index([[1, 2], [3, 4], [5, 6]], 0) == [1, 3, 5]

def test_get_col_by_index2():
    """Тест получить столбец по индексу"""
    assert mc.get_col_by_index([[1, 2], [3, 4], [5, 6]], 2) == None

def test_swap_row():
    """Тест поменять местами строки"""
    assert mc.swap_row([[1, 2], [3, 4], [5, 6]], 0, 1) == [[3, 4], [1, 2], [5, 6]]

def test_multiply_row_by_scal():
    """Тест умножить строку на скаляр"""
    assert mc.multiply_row_by_scal([[1, 2], [3, 4], [5, 6]], 0, 5) == [[5, 10], [3, 4], [5, 6]]

def test_addition_mul_row():
    """Тест сложение строк матрицы с индексами х + у, умноженную на скаляр"""
    assert mc.addition_mul_row([[1, 2], [3, 4], [5, 6]], 0, 1, 2) == [[7, 10], [3, 4], [5, 6]]

def test_difference_mul_row():
    """Тест вычитание строк матрицы с индексами х + у, умноженную на скаляр"""
    assert mc.difference_mul_row([[1, 2], [3, 4], [5, 6]], 0, 1, 2) == [[-5, -6], [3, 4], [5, 6]]

