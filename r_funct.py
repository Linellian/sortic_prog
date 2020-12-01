import base_funct


def ra(st_a):
    p_c = st_a[0]
    l_c = []
    for i in range(1, base_funct.f_len(st_a)):
        l_c.append(st_a[i])
    l_c.append(p_c)
    return l_c


def rb(st_b):
    p_c = st_b[0]
    l_c = []
    for i in range(1, base_funct.f_len(st_b)):
        l_c.append(st_b[i])
    l_c.append(p_c)
    return l_c

def rr(st_a, st_b):
    a = ra(st_a)
    b = rb(st_b)
    return a, b
