import math
import add_def as s

def copy1d(vec, do_copy=True):
    if do_copy:
        return vec[:]
    return vec

def lenght(vec1):
    vec_len = 0
    for i in range(len(vec1)):
        vec_len += vec1[i] * vec1[i]
    return math.sqrt(vec_len)

def summ(vec1, vec2):
    vec_summ = []
    for i in range(len(vec1)):
        vec_summ.append(vec1[i] + vec2[i])
    return vec_summ

def diff(vec1, vec2):
    vec_diff = []
    for i in range(len(vec1)):
        vec_diff.append(vec1[i] - vec2[i])
    return vec_diff

def scal_mult_vectors(vec1, vec2):
    scal = 0
    for i in range(len(vec1)):
        scal += vec1[i] * vec2[i]
    return scal

def mult_scal(vec, scal, do_copy=True):
    a = copy1d(vec, do_copy)
    for i in range(len(vec)):
        a[i] = a[i]*scal
    return a

def division_scal(vec, scal):
    a = []
    for i in range(len(vec)):
        a.append(vec[i]/scal)
    return a

def collinear(vec1, vec2):
    return s.is_scalar_almost_equal(1, abs(cos_angle(vec1, vec2)))

def cos_angle(vec1, vec2):
    a = lenght(vec1) if lenght(vec1) != 0 else 1
    b = lenght(vec2) if lenght(vec2) != 0 else 1
    vec0 = [1, 1] if vec1 == [0, 0] else vec1
    CosA = scal_mult_vectors(vec0, vec2)/(a*b)
    return CosA

def angle(vec1, vec2):
    a = math.acos(cos_angle(vec1, vec2))
    return a * 57.3

def equality(vec1, vec2):
    for i in range(len(vec1)):
        if vec1[i] != vec2[i]:
            return False
    return True

def direction(vec1, vec2):
    if equality(vec1, vec2):
        return True
    return cos_angle(vec1, vec2) == 1

def opposite_direction(vec1, vec2):
    return cos_angle(vec1, vec2) == -1

def esp_equality(vec1, vec2, esp=1E-10):
    for i in range(len(vec1)):
        if abs(vec1[i] - vec2[i]) > esp:
            return False
    return True

def orthogonality(vec1, vec2):
    return cos_angle(vec1, vec2) == 0

def change_direction_opposite(vec, do_copy=True):
    a = copy1d(vec, do_copy)
    for i in range(len(a)):
        a[i] = a[i] * -1
    return a

def normalization(vec):
    if (all(x == 0 for x in vec)):
        raise ValueError("Нормировать можно только ненулевые векторы")
    return division_scal(vec, lenght(vec))

def proj_a_to_b(vec1, vec2):
    if len(vec1) == len(vec2):
        if (abs(cos_angle(vec1, vec2) - 0) <= 1E-10):
            return 0
        proj = scal_mult_vectors(vec1,vec2) / lenght(vec2)
        return proj
