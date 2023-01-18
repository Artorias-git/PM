from interpol.interpol_logic import *
from inputers import scal_inputer, input_date_xy

def interpol_control():
    print("Управление: \n"
          "0 - back in main \n"
          "1 - input_date_xy \n"
          "2 - get_y \n"
          "3 - creat_image\n")

    while True:
        try:
            print("---------interpol---------")
            a = scal_inputer("Команда: ")
            if a == 0:
                break

            elif a == 1:
                date = input_date_xy()
                dots = get_dots_obj(date)
                systems = get_system_obj(dots)

            elif a == 2:
                x = scal_inputer("print x: ")
                print(get_y(x, systems))

            elif a == 3:
                creat_image(dots, systems)

        except NameError:
            print("Вы не ввели знаения")
        except ValueError:
            print("something wrong in slae_p...")