import math



def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

##def factorial(n):
##    if n == 1:
##        return 1
##    return n*factorial(n-1)

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans


def r(n):
    if n == 1:
        return 7
    else:
        print(n)
        return r(n-1) + math.gcd(n,r(n-1))


def main():
     print(r(50))


if __name__ == "__main__":
    main()
