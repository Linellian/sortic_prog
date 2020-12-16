import sp_funct
import r_funct 
import rr_funct
import ch_sortic_funct



el_a = input()
a = []
while el_a != "!":
    a.append(int(el_a))
    el_a = input()

el_f = input()
f = []
while el_f != "*":
    f.append(el_f)
    el_f = input()

ch_a = a
ch_b = []

for i in f:
    if i == "sa":
        ch_a = sp_funct.sa(ch_a)
    if i == "sb":
        ch_b = sp_funct.sb(ch_b)
    if i == "ss":
        ch_a, ch_b = sp_funct.ss(ch_a, ch_b)
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


a = ch_sortic_funct.f_sort(a)
print(a, ch_a)
if a == ch_a:
    print("OK")
else:
    print("KO")
