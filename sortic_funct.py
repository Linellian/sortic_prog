import base_funct
import sp_funct
import r_funct 
import rr_funct


def f_sort(a):
    b = []
    if base_funct.f_len(a) > 2:
        a, b = sp_funct.pb(a, b)
        a, b = sp_funct.pb(a, b)
        if a != []:
            while base_funct.f_len(a) != 0:
                if a[0] > base_funct.f_min(b) and a[0] < base_funct.f_max(b):
                    if a[0] > b[0]:
                        while a[0] > b[0]:
                            b = r_funct.rb(b)
                            print("rb")
                        a, b = sp_funct.pb(a, b)
                        print("pb")
                    elif a[0] < b[0]:
                        while a[0] < b[0]:
                            b = rr_funct.rrb(b)
                            print("rrb")
                        a, b = sp_funct.pb(a, b)
                        print("pb")
                        b = sp_funct.sb(b)
                        print("sb")
                elif a[0] < base_funct.f_min(b) or a[0] > base_funct.f_max(b):
                    while b[0] != base_funct.f_max(b):
                        b = rr_funct.rrb(b)
                        print("rrb")
                    a, b = sp_funct.pb(a, b)
                    print("pb")
                    b = sp_funct.sb(b)
                    print("sb")

            while b[0] != base_funct.f_min(b):
                b = r_funct.rb(b)
                print("rb")
            a, b = b, []
    return a