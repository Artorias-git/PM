from matrix.matrix_logic import is_matrix

def scal_inputer(text=""):
    while True:
        try:
            a = int(input(text))
            return a
        except:
            print("Try again")
            continue

# def vector_input(text=""):
#     while True:
#         try:
#             vec = list(map(int, input(text).split()))
#             if len(vec) < 2:
#                 a = 1 / 0
#             return vec
#         except:
#             print("Try again")
#             continue

def vector_input(text=""):
    while True:
        try:
            vec = list(map(int, input(text).split()))
        except:
            print("Try again")
        if len(vec) >= 2:
            return vec
        else:
            print('len error')


def matrix_input():
    print("input matrix")
    arr = []
    n = 0
    while n < 2:
        n = scal_inputer("size AxA of matrix = ")
    i = 0
    while len(arr) != n:
        vec = vector_input(f"строка {i}: ")
        if len(vec) == n:
            arr.append(vec)
            i += 1
        else:
            print("len error")
    return arr


def get_sla_value():
    print("enter matrix A")
    arr = matrix_input()
    print("enter B\n")
    b = []
    while len(arr) != len(b):
        b = vector_input("B = ")
    return arr, b

def input_date_xy():
    date_xy = [[1, 2],
               [3, 4],
               [3.5, 3],
               [6, 7]]
    return date_xy

