#https://www.grund-wissen.de/informatik/python/scipy/sympy.html
import sympy as sy
from sympy import *

x = sy.S('x')

a = sy.expand( (x + 2)**5 )
  
#print(a)

x1, x2, x3 = sy.symbols("x1 x2 x3")

equations = [
    sy.Eq( 8*x1 + 2*x2 + 3*x3 ,  15 ),
    sy.Eq( 6*x1 - 1*x2 + 7*x3 , -13 ),
    sy.Eq(-4*x1 + 5*x2 - 3*x3 ,  21 ),
]

b = sy.solve(equations)
#print(b)

M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(M.det())

x = sy.S('x')
M = Matrix([[x, 3, 0], [x, 9, 2], [0, 2, 1]])
print("Determinant as of x:",M.det())

EigenWertMatrix = Matrix([[-12,-4],[18,5]])
EigenWerte=EigenWertMatrix.eigenvals()
print(EigenWerte)
