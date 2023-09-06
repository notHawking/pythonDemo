#https://www.grund-wissen.de/informatik/python/scipy/sympy.html
import sympy as sy
x = sy.S('x')

a = sy.expand( (x + 2)**5 )
  
print(a)

x1, x2, x3 = sy.symbols("x1 x2 x3")

equations = [
    sy.Eq( 8*x1 + 2*x2 + 3*x3 ,  15 ),
    sy.Eq( 6*x1 - 1*x2 + 7*x3 , -13 ),
    sy.Eq(-4*x1 + 5*x2 - 3*x3 ,  21 ),
]

b = sy.solve(equations)
print(b)