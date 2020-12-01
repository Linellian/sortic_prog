def f_print(st_a, st_b):
    if f_len(st_a) > f_len(st_b):
        for i in range(f_len(st_b)):
            print(st_a[i], st_b[i])
        for i in range(-(f_len(st_a) - f_len(st_b)), 0):
            print(st_a[i])
        print("")
        print("_  _")
        print("a  b")
    elif f_len(st_a) < f_len(st_b):
        for i in range(f_len(st_a)):
           print(st_a[i], st_b[i])
        for i in range(-(f_len(st_b) - f_len(st_a)), 0):
            print(" ", st_b[i])
        print("")
        print("_  _")
        print("a  b")
    elif f_len(st_a) == f_len(st_b):
        for i in range(f_len(st_b)):
            print(st_a[i], st_b[i])
        print("")
        print("_  _")
        print("a  b")