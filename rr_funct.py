import base_funct


def rra(st_a):
    if st_a != []:  
        c = []
        c.append(st_a[-1])
        for i in range(base_funct.f_len(st_a) - 1):
            c.append(st_a[i])
        st_a = c
    return st_a
    

def rrb(st_b):
    if st_b != []: 
        c = []
        c.append(st_b[-1])
        for i in range(base_funct.f_len(st_b) - 1):
            c.append(st_b[i])
        st_b = c
    return st_b
    

def rrr(st_a, st_b):
    if st_a != [] and st_b != []: 
        c_a = []
        c_a.append(st_a[-1])
        for i in range(base_funct.f_len(st_a) - 1):
            c_a.append(st_a[i])
        c_b = []
        c_b.append(st_b[-1])
        for i in range(base_funct.f_len(st_b) - 1):
            c_b.append(st_b[i])
        return c_a, c_b
    else:
        return st_a, st_b
