from sympy import Symbol, Function, pi, I

x = Symbol('x')
s = Symbol('s')

def L(s, x):
    return (x**s - 1) / (x - 1)

L_function = Function('L')(s)

print(L_function)
# Output: L(s)

print(L_function.subs({s: 2*pi*I/log(2)}))
# Output: L(2*I*pi/log(2))
