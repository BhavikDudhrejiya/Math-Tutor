import streamlit as st

import sympy as sp
from streamlit import latex

from utils import *

class MathValidation:

    def validate_linear_equation(self,problem):
        try:
            if "=" not in problem:
                x = sp.symbols("x")
                sympy_readable_problem = add_multiplication_sign(problem)
                eq = sp.sympify(sympy_readable_problem)
                solution = sp.solve(eq,x)
                return solution
            else:
                x = sp.symbols("x")
                sympy_readable_problem = add_multiplication_sign(problem)
                lhs = sympy_readable_problem.split("=")[0].strip()
                rhs = sympy_readable_problem.split("=")[1].strip()
                eq = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
                solution = sp.solve(eq, x)
                return solution
        except:
            # st.error("❌ It seems there might be an error in your solution step. ❌")
            pass

if __name__=="__main__":
    problem = "5*x - 7 - 5"
    sol = MathValidation()
    print(sol.validate_linear_equation(problem))
