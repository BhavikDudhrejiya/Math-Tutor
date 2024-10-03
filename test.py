import sympy as sp
from utils import *

problem = "2*x + 3 = 11"

x = sp.symbols("x")
# sympy_readable_problem = add_multiplication_sign(problem)
eq = sp.sympify(problem)
solution = sp.solve(eq, x)
print(eq)