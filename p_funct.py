def sa(st_a):
    st_a[0], st_a[1] = st_a[1], st_a[0]

def sb(st_b):
    st_b[0], st_b[1] = st_b[1], st_b[0]

def ss(st_a, st_b):
    sa(st_a)
    sb(st_b)


def pa(st_a, st_b):
    if st_b != []:
        c = []
        c.append(st_b[0])
        for i in st_a:
            c.append(i)
        st_a = []
        st_a = c

def pb(st_a, st_b):
    if st_b != []:
        c = []
        c.append(st_a[0])
        for i in st_b:
            c.append(i)
        st_b = []
        st_b = c
