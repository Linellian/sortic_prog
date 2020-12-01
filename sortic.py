import base_funct
import sp_funct
import r_funct 
import rr_funct


a = input()
st_a = []
while a != "!":
    st_a.append(int(a))
    a = input()

# Комментарии с ожидаемыми выводами актуальны для значения
# st_a = [1, 2, 3, 4, 5]
st_b = [1, 2, 3, 4, 5]
st_a, st_b = base_funct.f_sortic(st_a, st_b)
print(st_a, st_b)
