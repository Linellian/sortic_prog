import base_funct


def rra(st_a):
    c = []
    c.append(st_a[-1])
    for i in range(base_funct.f_len(st_a) - 1):
        c.append(st_a[i])
    st_a = []
    st_a = c

def rrb(st_b):
    c = []
    c.append(st_b[-1])
    for i in range(base_funct.f_len(st_b) - 1):
        c.append(st_b[i])
    st_b = []
    st_b = c

def rrr(st_a, st_b):
    rra(st_a)
    rrb(st_b)
