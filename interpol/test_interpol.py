from interpol.interpol_logic import *


def check(is_passed, msg):
    if is_passed:
        print(msg + ' :PASSED')
    else:
        print(msg + ' :FAILED')

test_date = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
dots = get_dots_obj(test_date)
systems = get_system_obj(dots)

def test_get_y():
    """Тест получение y"""
    assert get_y(2, systems) == 3.0, "Should be 3.0"

def test_basis_polinom():
    """Тест подсчёта базис полинома"""
    assert basis_polinom(0, 2, dots) == 0.24, "Should be 0.24"

def test_basis_polinom1():
    """Тест подсчёта базис полинома"""
    assert basis_polinom(0, 3, dots) == 0, "Should be 0"

def test_basis_polinom2():
    """Тест подсчёта базис полинома"""
    assert basis_polinom(0, 1, dots) == 1.0, "Should be 1.0"

def test_basis_polinom3():
    """Тест подсчёта базис полинома"""
    assert basis_polinom(2, 3, dots) == 0, "Should be 0"

def test_basis_polinom4():
    """Тест подсчёта базис полинома"""
    assert basis_polinom(1, 3, dots) == 1.0, "Should be 1.0"

def test_polinom_lag():
    """Тест полинома"""
    assert polinom_lag(1, dots) == 2.0, "Should be 2.0"

def test_polinom_lag1():
    """Тест полинома"""
    assert polinom_lag(3, dots) == 4.0, "Should be 4.0"

def test_polinom_lag2():
    """Тест полинома"""
    assert polinom_lag(3.5, dots) == 3.0, "Should be 3.0"

def test_polinom_lag3():
    """Тест полинома"""
    assert polinom_lag(6, dots) == 7.0, "Should be 7.0"

def test_get_y1():
    """Тест получение y"""
    assert get_y(-1.5, systems) == -0.5, "Should be -0.5"

def test_get_y2():
    """Тест получение y"""
    assert get_y(3, systems) == 4.0, "Should be 4.0"

def test_get_y3():
    """Тест получение y"""
    assert get_y(5, systems) == 5.4, "Should be 5.4"

def test_get_y4():
    """Тест получение y"""
    assert get_y(9, systems) == 11.8, "Should be 11.8"