from matrix.matrix_logic import *
from inputers import scal_inputer, matrix_input

def matrix_control():
    print("Управление: \n"
          "0 - back in main \n"
          "1 - input matrix 1 \n"
          "2 - input matrix 2 \n"
          "21 - choose default matrix      3 - addition \n"
          "4 - difference                  5 - transposition \n"
          "6 - multiply_by_scal            7 - multiply_matrix\n"
          "8 - get_row_by_index            9 - get_col_by_index\n"
          "10 - swap_row                   11 - multiply_row_by_scal\n"
          "12 - addition_mul_row           13 - difference_mul_row\n")

    while True:
        try:
            print("--------matrix--------")
            a = scal_inputer("Команда: ")
            if a == 0:
                break

            elif a == 1:
                mat1 = matrix_input()
                mat = mat1
                printer(mat1)

            elif a == 2:
                mat2 = matrix_input()
                printer(mat2)

            elif a == 21:
                print("choose default matrix")
                b = scal_inputer("matrix number (1 or 2)")
                if b == 1:
                    pass
                elif b == 2:
                    mat = mat2
                else:
                    print("wrong b")

            elif a == 3:
                printer(addition(mat1, mat2))

            elif a == 4:
                printer(difference(mat1, mat2))

            elif a == 5:
                printer(transposition(mat))

            elif a == 6:
                scal = scal_inputer("enter scal: ")
                printer(multiply_by_scal(mat, scal))

            elif a == 7:
                printer(multiply_matrix(mat1, mat2))

            elif a == 8:
                idx = scal_inputer("enter index: ")
                print(get_row_by_index(mat, idx))

            elif a == 9:
                idx = scal_inputer("enter index: ")
                print(get_col_by_index(mat, idx))

            elif a == 10:
                idx1 = scal_inputer("enter index1: ")
                idx2 = scal_inputer("enter index2: ")
                printer(swap_row(mat, idx1, idx2))

            elif a == 11:
                idx = scal_inputer("enter index: ")
                scal = scal_inputer("enter scal: ")
                printer(multiply_row_by_scal(mat, idx, scal))

            elif a == 12:
                idx1 = scal_inputer("enter index1: ")
                idx2 = scal_inputer("enter index2: ")
                scal = scal_inputer("enter scal: ")
                printer(addition_mul_row(mat, idx1, idx2, scal))

            elif a == 13:
                idx1 = scal_inputer("enter index1: ")
                idx2 = scal_inputer("enter index2: ")
                scal = scal_inputer("enter scal: ")
                print(difference_mul_row(mat, idx1, idx2, scal))

        except NameError:
            print("Вы не ввели знаения")
        except ValueError:
            print("something wrong...")