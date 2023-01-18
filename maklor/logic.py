import matplotlib.pyplot as plt
import numpy as np
from interpol.my_plot import draw_one_plot

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def cos_mak(x, coeff):
    y_cos = 0
    for n in range(coeff):
        if n == 0:
            y_cos += 1
        else:
            y_cos += ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
    return y_cos

def creat_plot(function):
    i = 60
    x_p = np.linspace(-10, 10, 1000)
    y_p = list(map(lambda x: function(x, i), x_p))
    draw_one_plot(x_p, y_p)

creat_plot(cos_mak)