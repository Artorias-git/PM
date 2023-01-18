from vector.vector_logic import *
from inputers import scal_inputer, vector_input

def vector_control():
    print("Управление: \n"
          "0 - back in main \n"
          "1 - input two vectors \n"
          "2 - lenght                      3 - summ \n"
          "4 - diff                        5 - scal_mult_vectors \n"
          "6 - mult_scal                   7 - division_scal\n"
          "8 - collinear                   9 - cos_angle\n"
          "10 - angle                      11 - equality\n"
          "12 - direction                  13 - opposite_direction\n"
          "14 - esp_equality               15 - orthogonality\n"
          "16 - change_direction_opposite  17 - normalization\n"
          "18 - proj_a_to_b")

    while True:
        try:
            print("--------vector--------")
            a = scal_inputer("Команда: ")
            if a == 0:
                break

            elif a == 1:
                vec1 = vector_input("Введите через пробел координаты первого вектора: ")
                vec2 = vector_input("Введите через пробел координаты второго вектора: ")

            elif a == 2:
                print(lenght(vec1))
                print(lenght(vec2))

            elif a == 3:
                print(summ(vec1, vec2))

            elif a == 4:
                b = scal_inputer("1) vec1 - vec2\n"
                                 "2) vec2 - vac1")
                if b == 1:
                    print(diff(vec1, vec2))
                else:
                    print(diff(vec2, vec1))

            elif a == 5:
                print(scal_mult_vectors(vec1, vec2))

            elif a == 6:
                print(mult_scal(vec1, scal_inputer("скаляр: ")))

            elif a == 7:
                print(division_scal(vec1, scal_inputer("скаляр: ")))

            elif a == 8:
                print(collinear(vec1, vec2))

            elif a == 9:
                print(cos_angle(vec1, vec2))

            elif a == 10:
                print(angle(vec1, vec2))

            elif a == 11:
                print(equality(vec1, vec2))

            elif a == 12:
                print(direction(vec1, vec2))

            elif a == 13:
                print(opposite_direction(vec1, vec2))

            elif a == 14:
                print(esp_equality(vec1, vec2, input("print ESP, exempla: 1E-10")))

            elif a == 15:
                print(orthogonality(vec1, vec2))

            elif a == 16:
                print(change_direction_opposite(vec1))
                print(change_direction_opposite(vec2))

            elif a == 17:
                print(normalization(vec1))
                print(normalization(vec1))

            elif a == 18:
                print(proj_a_to_b(vec1, vec2))

        except NameError:
            print("Вы не ввели знаения")
        except ValueError:
            print("something wrong...")
