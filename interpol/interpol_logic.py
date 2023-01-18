from slae_p.slae_logic import roots_by_revers
import numpy as np
from interpol.my_plot import draw_two_plot

class coord():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

class system():
    def __init__(self, arr, b):
        self.__arr = arr
        self.__b = b
        self.__roots = roots_by_revers(arr, b)
        self.__coeff_a = self.__roots[0]
        self.__coeff_b = self.__roots[1]
        self.__x1 = arr[0][0]
        self.__x2 = arr[1][0]
    @property
    def arr(self):
        return self.__arr
    @property
    def b(self):
        return self.__b
    @property
    def coeff_a(self):
        return self.__coeff_a
    @property
    def coeff_b(self):
        return self.__coeff_b
    @property
    def x1(self):
        return self.__x1
    @property
    def x2(self):
        return self.__x2

def get_dots_obj(date):
    """преобразуем date в список обектов dots"""
    dots = []
    for i in range(len(date)):
        dots.append(coord(date[i][0], date[i][1]))
    return dots

def get_system_obj(dots):
    """используя dots, создаём обекты SLAE"""
    systems = []
    for i in range(1, len(dots)):

        x1 = dots[i - 1].x
        x2 = dots[i].x
        y1 = dots[i - 1].y
        y2 = dots[i].y

        arr = [[x1, 1],
               [x2, 1]]
        b = [y1, y2]

        systems.append(system(arr, b))
    return systems

def where_point(x, systems):
    """Определяем какому интервалу пренадлежит X"""
    if x <= systems[0].x2:
        return 0
    for i in range(1, len(systems)):
        if x <= systems[i].x2:
            return i
    if x >= systems[len(systems)-1].x2:
        return len(systems) - 1

def get_y(x, systems):
    """получаем Y по X"""
    s = where_point(x, systems)
    a = systems[s].coeff_a
    b = systems[s].coeff_b
    return a * x + b

def polinom_lag(x, dots):
    """вычисление многочлена L(x)"""
    y_pol = 0
    for i in range(len(dots)):
        y_pol += dots[i].y * basis_polinom(i, x, dots)
    return y_pol

def basis_polinom(i, x, dots):
    """базисный полином Лагранжа l(x)"""
    coeff = 1
    x0 = dots[i].x
    for j in range(len(dots)):
        if j != i:
            xj = dots[j].x
            coeff *= (x - xj) / (x0 - xj)
    return coeff

def creat_image(dots, systems):
    x_pol = np.linspace(-10, 10, 100)
    y_pol = polinom_lag(x_pol, dots)

    x_num = np.linspace(-10, 10, 100)
    y_num = list(map(lambda x: get_y(x, systems), x_num))

    draw_two_plot(x_pol, y_pol, x_num, y_num)
