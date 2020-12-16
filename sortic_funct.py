import base_funct
import sp_funct
import r_funct
import rr_funct
from termcolor import colored

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
                            print(colored("rb",'yellow'))
                        a, b = sp_funct.pb(a, b)
                        print(colored("pb",'red'))
                    elif a[0] < b[0]:
                        while a[0] < b[0]:
                            b = rr_funct.rrb(b)
                            print(colored("rrb",'white'))
                        a, b = sp_funct.pb(a, b)
                        print(colored("pb",'blue'))
                        b = sp_funct.sb(b)
                        print(colored("sb",'green'))
                elif a[0] < base_funct.f_min(b) or a[0] > base_funct.f_max(b):
                    while b[0] != base_funct.f_max(b):
                        b = rr_funct.rrb(b)
                        print(colored("rrb",'yellow'))
                    a, b = sp_funct.pb(a, b)
                    print(colored("pb",'red'))
                    b = sp_funct.sb(b)
                    print(colored("sb",'white'))

            while b[0] != base_funct.f_min(b):
                b = r_funct.rb(b)
                print(colored("rb",'blue'))
            a, b = b, []
    return a
