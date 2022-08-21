from sympy.parsing.sympy_parser import parse_expr
from sympy import *
EPSILON = 0.0001
x= symbols('x')

""" Use these if you directly want to run """
#x0 = -20 
#z= 10
#eqn= "(x**3) - (x**2) + 2"
eqn = input("Enter Equation:- ")
x0 = int(input("Enter Initial Value Assumed :- "))
z= int(input("Enter total number of ilterations:- "))
expr =  parse_expr(eqn)
expr_dash = expr.diff(x)

def func(y): 
    return expr.subs(x,y)

def derivFunc( y ): 
    return expr_dash.subs(x,y)

print("EPSILON = {}".format(EPSILON))
print("f(x)=")
print(expr)
print("f'(x)=")
print(expr_dash)
def newtonRaphson(s, x ): 
    for m in range(s):
        F = func(x)
        dF = derivFunc(x)
        print("xi+1 = xi - F/df=")
        print("xi+1 = {0} - {1}/{2}".format(Float(x),Float(F),Float(dF)))
        h = F / dF 
        x = x - h 
        print("={}".format(Float(x)))

        if(derivFunc(x) !=0 and abs(func(x)) >= EPSILON):
            print(m , "Illteration x ==%.10f"% x  , sep=" ")
            print("")
        elif(abs(func(x)) <= EPSILON ):
            print("Accuracy more than {} closing program".format(EPSILON))
            break;
        elif(derivFunc(x) ==0):
            print("Derivative is 0 Closing Program")
            break;

newtonRaphson(z,x0)
