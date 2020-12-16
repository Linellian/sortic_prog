import sp_funct
import r_funct 
import rr_funct
import ch_sortic_funct
import input_funct


a = input_funct.f_num_split(input())

f = input_funct.f_split(input())

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
if a == ch_a:
    print("OK")
else:
    print("KO")
