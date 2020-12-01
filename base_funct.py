import sp_funct
import r_funct 
import rr_funct


def f_len(el):
    count = 0
    for i in el:
        i = i
        count += 1
    return count


def f_cond(el):
    if f_len(el) >= 2:
        return True
    else:
        return False


def f_del_first(el):
    ter = []
    for i in range(1, f_len(el)):
        ter.append(el[i])
    return ter

def f_sortic(st_a, st_b):
    sp_funct.sa(st_a, st_b) # [2, 1, 3, 4, 5] [1, 2, 3, 4]
    sp_funct.sb(st_b, st_a) # [2, 1, 3, 4, 5] [2, 1, 3, 4]
    sp_funct.ss(st_a, st_b) # [1, 2, 3, 4, 5] [1, 2, 3, 4]
    st_a, st_b = sp_funct.pa(st_a, st_b) # [1, 1, 2, 3, 4, 5] [2, 3, 4]
    st_a, st_b = sp_funct.pb(st_a, st_b) # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
    st_a = r_funct.ra(st_a) # [2, 3, 4, 5, 1] [1, 2, 3, 4, 5]
    st_b = r_funct.rb(st_b) # [2, 3, 4, 5, 1] [2, 3, 4, 5, 1]
    st_a, st_b = r_funct.rr(st_a, st_b) # [3, 4, 5, 1, 2] [3, 4, 5, 1, 2]
    st_a = rr_funct.rra(st_a) # [2, 3, 4, 5, 1] [3, 4, 5, 1, 2]
    st_b = rr_funct.rrb(st_b) # [2, 3, 4, 5, 1] [2, 3, 4, 5, 1]
    st_a, st_b = rr_funct.rrr(st_a, st_b) # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
    return st_a, st_b
    