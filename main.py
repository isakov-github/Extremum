# Isakov V.E.

from sympy import *
#from sympy.solvers import solve

constants = [[3.1, 10.3, -2.8, 10.3],[2.1, 8.8, -11.4, -5.6],[1.6, 0.2, -20.8, 38.5]]

def extremum(lst):
    a, b, c, d = lst
    x = Symbol('x')
    f = a*x**3 + b*x**2 + c*x + d
    f_prime = f.diff(x)
    equation = lambdify(x, f_prime)
    print(f_prime)
    x1, x2 = solve(f_prime, x)
    print(f"x1 = {round(x1, 4)}, x2 = {round(x2, 4)}")

for consts in constants:
    extremum(consts)


# import numpy as np
#from matplotlib import pyplot as plt

#x_val = np.arange(-4,1)
#y_val = equation(x_val)
#print(x_val)
#plt.title("Matplotlib demo")
#plt.xlabel("x axis caption")
#plt.ylabel("y axis caption")
#plt.plot(x_val,y_val)
#plt.show()

#print(equation(x1))
#print(equation(x2))
#print(equation(-4))
#print(equation(1))

