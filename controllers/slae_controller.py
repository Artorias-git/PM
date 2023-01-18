from slae_p.slae_logic import *
from inputers import get_sla_value, scal_inputer
from matrix.matrix_logic import printer

def slae_control():
    print("Управление: \n"
          "0 - back in main \n"
          "1 - get_sla_value \n"
          "2 - roots\n"
          "3 - revers_matrix\n"
          "4 - roots (by revers_matrix)\n")

    while True:
        try:
            print("---------slae_p---------")
            a = scal_inputer("Команда: ")
            if a == 0:
                break

            elif a == 1:
                arr, b = get_sla_value()

            elif a == 2:
                print(roots(arr, b))

            elif a == 3:
                printer(revers(arr))

            elif a == 4:
                print(roots_by_revers(arr, b))

        except NameError:
            print("Вы не ввели знаения")
        except ValueError:
            print("something wrong in slae_p...")

