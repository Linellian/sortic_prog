import base_funct


def sa(st_a):
    if base_funct.f_len(st_a) >= 2:
        st_a[0], st_a[1] = st_a[1], st_a[0]
    return st_a

def sb(st_b):
    if base_funct.f_len(st_b) >= 2:
        st_b[0], st_b[1] = st_b[1], st_b[0]
    return st_b

def ss(st_a, st_b):
    if base_funct.f_len(st_a) >= 2 and base_funct.f_len(st_b) >= 2:
        st_a[0], st_a[1] = st_a[1], st_a[0]
        st_b[0], st_b[1] = st_b[1], st_b[0]
    return st_a, st_b
    

def pa(st_a, st_b):
    if base_funct.f_len(st_b) != 0:
        c = [st_b[0]]
        for i in range(base_funct.f_len(st_a)):
            c.append(st_a[i])
        st_a = c
        st_b = base_funct.f_del_first(st_b)
    return st_a, st_b

def pb(st_a, st_b):
    if base_funct.f_len(st_a) != 0:
        c = [st_a[0]]
        for i in range(base_funct.f_len(st_b)):
            c.append(st_b[i])
        st_b = c
        st_a = base_funct.f_del_first(st_a)
    return st_a, st_b
