import base_funct


def sa(st_a, st_b):
    if base_funct.f_cond(st_b):
        st_a[0], st_a[1] = st_a[1], st_a[0]

def sb(st_b, st_a):
    if base_funct.f_cond(st_b):
        st_b[0], st_b[1] = st_b[1], st_b[0]

def ss(st_a, st_b):
    if base_funct.f_cond(st_a) and base_funct.f_cond(st_b):
        sa(st_a, st_b)
        sb(st_b, st_a)


def pa(st_a, st_b):
    if st_b != []:
        c = []
        c.append(st_b[0])
        for i in st_a:
            c.append(i)
    return c, base_funct.f_del_first(st_b)

def pb(st_a, st_b):
    if st_a != []:
        c = []
        c.append(st_a[0])
        for i in st_b:
            c.append(i)
    return base_funct.f_del_first(st_a), c
