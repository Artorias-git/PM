
EPS = 1E-10

def is_scalar_almost_equal(a, b, eps=EPS):
    return abs(a - b) <= eps

def is_vector_almost_equal(a, b, eps=EPS):
    same = [is_scalar_almost_equal(av,bv,eps) for av, bv, in zip(a, b)]
    return False not in same

def is_matrix_almost_equal(a, b, eps=EPS):
    same = [is_vector_almost_equal(av,bv,eps) for av, bv, in zip(a, b)]
    return False not in same

