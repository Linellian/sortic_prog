import base_funct


def rra(st_a):
    c = []
    c.append(st_a[-1])
    for i in range(base_funct.f_len(st_a) - 1):
        c.append(st_a[i])
    return c

def rrb(st_b):
    c = []
    c.append(st_b[-1])
    for i in range(base_funct.f_len(st_b) - 1):
        c.append(st_b[i])
    return c

def rrr(st_a, st_b):
    a = rra(st_a)
    b = rrb(st_b)
    return a, b