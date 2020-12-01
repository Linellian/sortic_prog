import base_funct
import sp_funct
import r_funct 
import rr_funct


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


a = input()
st_a = []
while a != "!":
    st_a.append(int(a))
    a = input()

# Комментарии с ожидаемыми выводами актуальны для значения
# st_a = [1, 2, 3, 4, 5]
st_b = [1, 2, 3, 4, 5]
st_a, st_b = f_sortic(st_a, st_b)
print(st_a, st_b)
