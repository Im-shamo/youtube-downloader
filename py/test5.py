import math
import cmath
import random


def Solve_Quadratic(a, b, c): #this returns [root_1, root_2, vortex_x, vortex_y, discriminan]. In ax^2+bx+c=0 form
    #this is in ax^2+bx+c=0 form
    #a = float(input("Enter x^2 coefficient: "))
    #b = float(input("Enter x coefficient: "))
    #c = float(input("Enter constant: "))
    
    #b^2-4ac
    discriminant = b*b - 4*a*c
    vortex_x = -b/(2*a)
    vortex_y = a * vortex_x**2 + b * vortex_x + c
    
    if discriminant >= 0:
        root_1 = vortex_x + math.sqrt(discriminant)/(2*a)
        root_2 = vortex_x - math.sqrt(discriminant)/(2*a)
     
    else:
        root_1 = vortex_x + cmath.sqrt(discriminant)/(2*a)
        root_2 = vortex_x - cmath.sqrt(discriminant)/(2*a)
    
    ans = [root_1, root_2, vortex_x, vortex_y, discriminant]
    return ans
    pass

def Solve_Quadratic_2(a, b, c): #this returns [root_1, root_2]. In ax^2+bx+c=0 form
    vortex_x = -b/(2*a)
    m = math.sqrt(b*b - 4*a*c)/(2*a)
    roots=[vortex_x+m, vortex_x-m]
    return roots

def Equation_solving(a, b, c, d, e, f): #solve two variables in two equations using the method of elimination. In the form of ax+by=c and dx+ey=f
    
    x = (c*e - f*b)/(a*e - d*b)
    y = (c - a*x)/b
    print(x)
    print(y)
   
def Equation_solving_2(a, b, c, d, e, f): #solve two variables in two equations. In the form of ax+by=c and dx+ey=f
    #in the from x = Ay + C
    C = c/a
    A = -b/a
    
    #in the form of d(Ay + C) + ey = f
    y = (f- C*d)/(d*A +e)
    x = (c - b*y)/a
    
    print(x)
    print(y)

def Equation_solving_3(a, b, c, d, e, f): #solves ax + by = c and dx^2 + ey^2=f
    #in the from x = Ay + C
    C = c/a
    A = -b/a
    
    #if math.isclose(C, int(C)) and math.isclose(A, int(A)):
        #C = int(C)
        #A = int(A)
    #print("A = " + str(A) + " C = " + str(C))
    
    #in the form d(Ay + C)^2 + ey^2=f
    y = Solve_Quadratic(d*A*A+e, 2*A*C*d, -f)
    
    #print(d*A*A+e, 2*A*C*d, -f)
    
    #for root_1
    x_1 = (-b/a)*y[0] + c/a
    x_2 = A*y[1] + C
    
    print(str(x_1) +","+ str(y[0]))
    print(str(x_2) +","+ str(y[1]))
    print(y)

def Equation_solving_4(a, b, c, d, e, f, g): #solves ax + by = c and dx^2 + fx + g = 0
    #in the from x = Ay + C
    C = c/a
    A = -b/a
    
    
    
Equation_solving_3(1, -1, -1, 1, 1, 25)


 