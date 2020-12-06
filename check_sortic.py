import base_funct
import sp_funct
import r_funct 
import rr_funct


ch_b = [1, 2, 3, 4, 5]

a = input()
ch_a = []
while a != "!":
    ch_a.append(int(a))
    a = input()

f = input()
st_f = []
while f != "*":
    st_f.append(f)
    f = input()

for i in st_f:
    if i == "sa":
        sp_funct.sa(ch_a, ch_b)
    if i == "sb":
        sp_funct.sb(ch_b, ch_a)
    if i == "ss":
        sp_funct.ss(ch_a, ch_b)
    if i == "pa":
        ch_a, ch_b = sp_funct.pa(ch_a, ch_b)
    if i == "pb":
        st_a, st_b = sp_funct.pb(ch_a, ch_b)
    if i == "ra":
        ch_a = r_funct.ra(ch_a)
    if i == "rb":
        ch_b = r_funct.rb(ch_b)
    if i == "rr":
        ch_a, ch_b = r_funct.rr(ch_a, ch_b)
    if i == "rra":
        ch_a = rr_funct.rra(ch_a)
    if i == "rrb":
        ch_b = rr_funct.rrb(ch_b)
    if i == "rrr":
        ch_a, ch_b = rr_funct.rrr(ch_a, ch_b)


st_a, st_b = base_funct.f_sortic(ch_a, ch_b)
if st_a == ch_a and st_b == ch_b:
    print("OK")
else:
    print("KO")
