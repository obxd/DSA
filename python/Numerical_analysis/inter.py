# Lagrange Interpolation

import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
import textwrap
# Reading number of unknowns
n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))


# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))


def Lagrange (Lx, Ly):
    X=symbols('X')
    if  len(Lx)!= len(Ly):
        print ("ERROR")
        return 1
    y=0
    for k in range ( len(Lx) ):
        t=1
        print("L%d="%k)
        for j in range ( len(Lx) ):
            if j != k:
                print("(%s"%(X-Lx[j]), end=" / " )
                print((Lx[k]-Lx[j]), end=") ")
                t=t* ( (X-Lx[j]) /(Lx[k]-Lx[j]) )
        print("\n=%s"%t)
        print("------------")
        y+= t*Ly[k]
    return y

ans = Lagrange(x,y)
print('P=')
print(textwrap.fill(str(ans),80))
print('==============================')
print('P=')
print(simplify(ans))
print('==============================')
print()

# matrix method
init_printing(use_unicode=True)
Aarr =[]
Barr =[]
M = []
for i in range(len(x)):
    M.append([])
    for j in range(n):
        Aarr.append(x[i]**j)
        M[i].append(Aarr[-1])
    Barr.append(y[i])
    M[i].append(y[i])
print(Aarr)
print(M)            
A = Matrix(np.array(Aarr).reshape(-1, int(np.sqrt(len(Aarr)))))
B = Matrix(np.array(Barr).reshape(-1,1))


Ainv = A**-1

print("Ainv is:")
pprint(Ainv)

xi = []
for i in range(n):
    xi.append("x%d"%i)
sym = symbols(' '.join(xi))

M = Matrix(M)
pprint(M) 

system = A, b = M[:, :-1], M[:, -1]
X = linsolve(system)


print('==============================')
print("X is")
pprint(X)
print('==============================')
print()



def NewtonInterpolation  (Lx, Ly):
    X=symbols('X')
    if  len(Lx)!= len(Ly):
        print ("ERROR")
        return 1

    print("p0 = %s"%Ly[0])
    print("------------")

    p = []
    p.append(Float(Ly[0]))

    for k in range (1, len(Ly) ):
        mul_p = 1
        mul_ck =  1
        mulc_print = []
        mulp_print = []
        for j in range(len(p)):
            mulp_print.append(X - Lx[j])
            mulc_print.append(Lx[k] - Lx[j])
            mul_p = mul_p * (X - Lx[j])   
            mul_ck = mul_ck * (Lx[k] - Lx[j])   
        print("\nitter%d"%k) 
        print("ck = ",end="")
        print( "ck = {0} - {1} /".format(Ly[k],p[k-1].subs(X,Lx[k])), end="")
        for toPrint in mulc_print:
            print("(",toPrint,end=") ")
        print()
        ck = (Ly[k] - p[k-1].subs(X,Lx[k]) ) / mul_ck
        print("ck= ", ck)
        
        print("p{0} = {1} + {2} * ".format(k,p[k-1],ck),end="")
        for toPrint in mulp_print:
            print("(",toPrint,end=") ")
        print()
        tmp =  p[k-1] + ck * mul_p
        print(tmp)
        p.append(tmp  )
    return p

ans = NewtonInterpolation(x,y)[n-1]
print('P=')
print(textwrap.fill(str(ans),80))
print('==============================')
print('P=')
print(simplify(ans))
print('==============================')
