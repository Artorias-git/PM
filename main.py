from controllers.vector_controller import vector_control
from controllers.matrix_controller import matrix_control
from controllers.slae_controller import slae_control
from controllers.interpol_controller import interpol_control
from inputers import scal_inputer

print(  "0 - stop \n"
        "1 - vectors \n"
        "2 - matrix\n"
        "3 - SLAE\n"
        "4 - interpol")

while True:
    try:
        print("---------main---------")
        a = scal_inputer("Команда: ")

        if a == 0:
            break
        elif a == 1:
            vector_control()
        elif a == 2:
            matrix_control()
        elif a == 3:
            slae_control()
        elif a == 4:
            interpol_control()

    except:
        print("something wrong...")





