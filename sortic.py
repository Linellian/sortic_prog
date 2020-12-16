import sortic_funct


el_a = input()
a = []
while el_a != "!":
    a.append(int(el_a))
    el_a = input()

# a = [2, 1, 3]

a = sortic_funct.f_sort(a)
