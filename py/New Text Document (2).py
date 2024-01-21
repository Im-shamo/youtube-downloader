from math import *

def circle_pt(r,x):
    return round(sqrt(r**2-x**2))

def main():
    r = 5
    shape = ""
    for x in range(r, 0, -1):
        shape += "."*circle_pt(r,x) + "\n"
        
    shape = shape[0:-1]*2
        
    print(shape)
        
    













if __name__ == "__main__":
    main()