import sp_funct
import r_funct 
import rr_funct


def f_len(st):
    c = 0
    if st != []:
        for i in st:
            i = i
            c += 1
    return c

def f_cond(el):
    if f_len(el) >= 2:
        return True
    else:
        return False

# def str_input():
#     a = input()
#     lst = []
#     c = ""
#     for i in range(f_len(a) + 1):
#         if a[i] != " ":
#              c += a[i]
#         else:
#             lst.append(int(c))
#             c = ""
#     return lst

def f_del_first(el):
    ter = []
    for i in range(1, f_len(el)):
        ter.append(el[i])
    return ter


def f_max(el):
    ma = 0
    if el != []:
        for i in el:
            if i > ma:
                ma = i
        return ma
    else:
        return 0

def f_min(el):
    mi = 999
    if el != []:
        for i in el:
            if i < mi:
                mi = i
        return mi
    else:
        return 0
