import vector.vector_logic as vc
import pytest
from add_def import *


def check(is_passed, msg):
    if is_passed:
        print(msg + ' :PASSED')
    else:
        print(msg + ' :FAILED')

def test_summ():
    """Тест сложения векторов"""
    assert vc.summ([1, 2],[3, 4]) == [4, 6], "Should be [4, 6]"

def test_diff():
    """Тест вычитания векторов"""
    assert vc.diff([1, 2],[3, 4]) == [-2, -2], "Should be [-2, -2]"

def test_mult_scal():
    """Тест умножения векторов на скаляр"""
    assert vc.mult_scal([1, 2, 3], 2) == [2, 4, 6]

def test_division_scal():
    """Тест деления векторов на скаляр"""
    assert vc.division_scal([1, 2, 3, 4], 2) == [0.5, 1.0, 1.5, 2.0]

def test_scal_zero_div():
    """Тест деления векторов на скаляр"""
    a = [1, 2, 3, 4]
    b = 0
    with pytest.raises(ZeroDivisionError):
        res = vc.division_scal(a, b)

def test_scal_mult_vectors():
    """Тест скалярного произведения векторов"""
    assert vc.scal_mult_vectors([1, 2],[3, 4]) == 11.0, "Should be 11.0"

def test_scal_mult_vectors2():
    """Тест скалярного произведения векторов"""
    a = [1, 2]
    b = [3]
    with pytest.raises(TypeError):
        res = vc.division_scal(a, b)

def test_collinear():
    """Тест коллинеарности"""
    assert vc.collinear([1, 2],[3, 4]) == False

def test_collinear2():
    """Тест коллинеарности"""

    assert vc.collinear([1, 1],[-1, -1]) == True

def test_collinear3():
    """Тест коллинеарности"""
    assert vc.collinear([0, 0],[0, -2]) == True

def test_collinear4():
    """Тест коллинеарности"""
    assert vc.collinear([0, 1],[0, -2]) == True

def test_CosAngle():
    """Тест косинус"""
    assert vc.cos_angle([1, 0], [0, 1]) == 0.0

def test_CosAngle2():
    """Тест косинус"""
    assert vc.cos_angle([1, 0], [-1, 0]) == -1.0


def test_direction():
    """Тест сонаправленность"""
    assert vc.direction([1, 0],[-1, 0]) == False

def test_direction2():
    """Тест сонаправленность"""
    assert vc.direction([0, 1],[0, 2]) == True

def test_direction3():
    """Тест сонаправленность"""
    assert vc.direction([2, 2],[2, 2]) == True

def test_opposite_direction():
    """Тест противоположнонаправленность"""
    assert vc.opposite_direction([1, 0],[-1, 0]) == True

def test_opposite_direction2():
    """Тест противоположнонаправленность"""
    assert vc.opposite_direction([1, 1],[2, 2]) == False

def test_equality():
    """Тест равенство векторов"""
    assert vc.equality([0, 2],[2, 2]) == False

def test_equality2():
    """Тест равенство векторов"""
    assert vc.equality([2, 2],[2, 2]) == True



def test_ESPequality():
    """Тест равенство векторов с заданной точностью"""
    assert vc.esp_equality([2, 2], [2, 2], 1E-1) == True

def test_ESPequality2():
    """Тест равенство векторов с заданной точностью"""
    assert vc.esp_equality([2, 2], [2, 2.2], 1E-1) == False

def test_normalization():
    """Тест нормировка"""
    assert vc.normalization([3, 4]) == [0.6, 0.8]

def test_lenght():
    """Тест длинна"""
    assert vc.lenght([3, 4]) == 5

def test_change_direction_opposite():
    """Тест изменить направление"""
    assert vc.change_direction_opposite([3, 5, 8]) == [-3, -5, -8]

def test_change_direction_opposite2():
    """Тест изменить направление"""
    assert vc.change_direction_opposite([0, -1, 3]) == [0, 1, -3]

def test_angle():
    """Тест угол"""
    assert is_scalar_almost_equal(vc.angle([0, 1], [1, 0]),  90.0, 1E-2)

def test_angle2():
    """Тест угол"""
    assert is_scalar_almost_equal(vc.angle([1, 0], [-1, 0]), 180.0, 1E-1)

def test_angle3():
    """Тест угол"""
    assert is_scalar_almost_equal(vc.angle([1, 1], [1, 0]), 45.0, 1E-2)


def test_proj_a_to_b():
    """Тест угол"""
    assert vc.proj_a_to_b([4, 5], [6, 0]) == 4.0

def test_proj_a_to_b2():
    """Тест угол"""
    assert vc.proj_a_to_b([1, 2], [3, 4]) == 2.2