from matrix.matrix_logic import *
from interpol.interpol_logic import *

date = [[1, 2],
        [3, 4],
        [3.5, 3],
        [6, 7]]
dots = get_dots_obj(date)
systems = get_system_obj(dots)

# def transform_b_value(b):
#     res = [[b[0], 0], [b[1], 0]]
#     return res

# def get_approx_system(systems):
#     approx_system = []
#     for i in range(len(systems)):
#         a = get_a_tilda(systems[i].arr)
#         bt = transform_b_value(systems[i].b)
#         b = get_b_tilda(systems[i].arr, bt)
#         approx_system.append(system(a, b))
#     return approx_system

def get_a_tilda(a):
    return multiply_matrix(transposition(a), a)

def get_b_tilda(a, b):
    return get_col_by_index(multiply_matrix(transposition(a), b), 0)

def get_ab_for_approx(date):
    a = []
    b = []
    for i in range(len(date)):
        a.append([date[i][0], 1])
        b.append([date[i][1], 0])
    return a, b

def get_ab_for_2step_approx(date):
    a = []
    b = []
    for i in range(len(date)):
        a.append([date[i][0]**2, date[i][0], 1])
        b.append([date[i][1], 0])
    return a, b

def coeff_for_approx(date):
    a, b = get_ab_for_2step_approx(date)
    a_tilda = get_a_tilda(a)
    b_tilda = get_b_tilda(a, b)
    x = roots_by_revers(a_tilda, b_tilda)
    return x

def get_y_approx(date, x):
    coeffs = coeff_for_approx(date)
    a = coeffs[0]
    b = coeffs[1]
    return a * x + b

def creat_image_approx(systems, date):
    x_line_approx = np.linspace(-5, 10, 100)
    y_line_approx = get_y_approx(date, x_line_approx)

    x_num = np.linspace(-5, 10, 100)
    y_num = list(map(lambda x: get_y(x, systems), x_num))

    draw_two_plot(x_line_approx, y_line_approx, x_num, y_num)

creat_image_approx(systems, date)
