import random

import slae_p.slae_logic as ss
from add_def import *



def test_roots():
    """Тест получения корня слау"""
    assert ss.roots([[1, 2],[3, 4]], [6, 8]) == [-4.0, 5.0]

def test_roots1():
    """Тест получения корня слау"""
    assert is_vector_almost_equal(ss.roots([[3, 2, -5],[2, -1, 3],[1, 2, -1]], [-1, 13, 9]), [3.0, 5.0, 4.0])

def test_roots2():
    """Тест получения корня слау"""
    assert is_vector_almost_equal(ss.roots([[1, 1, 1],[4, 2, 1],[9, 3, 1]], [0, 1, 3]), [0.5, -0.5, 0.0])

def test_roots3():
    """Тест получения корня слау"""
    assert is_vector_almost_equal(ss.roots([[4, -7, 8], [2, -4, 5], [-3, 11, 1]], [-23, -13, 16]), [-2, 1, -1])

def test_roots4():
    """Тест получения корня слау"""
    assert is_vector_almost_equal(ss.roots([[2, 3], [4, 3]], [2, 7]), [2.5, -1])

def test_jg():
    """Тест получения единичной матрици методом Жордана-Гауса, из любой матрици"""
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(round(random.random()*10, 5))
        matrix.append(row)

    assert is_matrix_almost_equal(ss.jordan_gauss(matrix), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])