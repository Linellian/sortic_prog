def f_num_split(el):
    c = ""
    lst = []
    for i in el:
        if i == " " and c:
            lst.append(int(c))
            c = ""
        else:
            c += i
    if c:
        lst.append(int(c))
    return lst

def f_split(el):
    c = ""
    lst = []
    for i in el:
        if i == " " and c:
            lst.append(c)
            c = ""
        else:
            c += i
    if c:
        lst.append(c)
    return lst