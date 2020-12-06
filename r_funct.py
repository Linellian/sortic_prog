import base_funct


def ra(st_a):
    if st_a != []:
        p_c = st_a[0]
        l_c = []
        for i in range(1, base_funct.f_len(st_a)):
            l_c.append(st_a[i])
        l_c.append(p_c)
        print("ra")
        st_a = l_c
    return st_a

def rb(st_b):
    if st_b != []:
        p_c = st_b[0]
        l_c = []
        for i in range(1, base_funct.f_len(st_b)):
            l_c.append(st_b[i])
        l_c.append(p_c)
        print("rb")
        st_b = l_c
    return st_b

def rr(st_a, st_b):
    if st_a != [] and st_b != []:
        p_ca = st_a[0]
        l_ca = []
        for i in range(1, base_funct.f_len(st_a)):
            l_ca.append(st_a[i])
        l_ca.append(p_ca)
        p_cb = st_b[0]
        l_cb = []
        for i in range(1, base_funct.f_len(st_b)):
            l_cb.append(st_b[i])
        l_cb.append(p_cb)
        print("rr")
        return l_ca, l_cb
    else:
        return st_a, st_b
