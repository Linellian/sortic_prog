def f_len(el):
    count = 0
    for i in el:
        count += 1
    return count


def f_cond(el):
    if f_len(el) >= 2:
        return True
    else:
        return False




def f_print():
    global st_a
    global st_b
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




def sa():
    st_a[0], st_a[1] = st_a[1], st_a[0]
    print(st_a)

def sb():
    st_b[0], st_b[1] = st_b[1], st_b[0]
    print(st_b)


def ss():
    sa()
    sb()




def pa():
    global st_a
    global st_b
    if st_b != []:
        c = []
        c.append(st_b[0])
        for i in st_a:
            c.append(i)
        st_a = []
        st_a = c
        print(st_a)

def pb():
    global st_a
    global st_b
    if st_b != []:
        c = []
        c.append(st_a[0])
        for i in st_b:
            c.append(i)
        st_b = []
        st_b = c
        print(st_b)




def ra():
    global st_a
    p_c = st_a[0]
    l_c = []
    for i in range(1, f_len(st_a)):
        l_c.append(st_a[i])
    st_a = []
    st_a = l_c
    st_a.append(p_c)
    print(st_a)

def rb():
    global st_b
    p_c = st_b[0]
    l_c = []
    for i in range(1, f_len(st_b)):
        l_c.append(st_b[i])
    st_b = []
    st_b = l_c
    st_b.append(p_c)
    print(st_b)

def rr():
    ra()
    rb()



def rra():
    global st_a
    c = []
    c.append(st_a[-1])
    for i in range(f_len(st_a) - 1):
        c.append(st_a[i])
    st_a = []
    st_a = c
    print(st_a)

def rrb():
    global st_b
    c = []
    c.append(st_b[-1])
    for i in range(f_len(st_b) - 1):
        c.append(st_b[i])
    st_b = []
    st_b = c
    print(st_b)

def rrr():
    rra()
    rrb()
