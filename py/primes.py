from math import *
from time import time

def r(n, r_n):
    if n < 1000:
        value_gcd = gcd(n+1, r_n)
        r_m = r_n + value_gcd
        if value_gcd != 1:
            print(f"r({n+1}) = {r_m}\tgcd({n+1}, {r_n}) = {value_gcd}")
        r(n+1, r_m)
        
def f(n, r_n):
    gcd_list = []
    ans_list = []
    while n < 100000000:
        value_gcd = gcd(n+1, r_n)
        m = n + 1
        r_m = r_n + value_gcd
        #if value_gcd != 1:
        #print(f"f({m}) = {r_m}\tgcd({n+1}, {r_n}) = {value_gcd}")
        ans_list.append(f"f({m}) = {r_m}\tgcd({n+1}, {r_n}) = {value_gcd}")
            #gcd_list.append(value_gcd)
        n = m
        r_n = r_m
    return ans_list

def main():
    r(1,7)
    

if __name__ == "__main__":
    main()

