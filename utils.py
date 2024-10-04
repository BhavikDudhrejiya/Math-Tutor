import re
import streamlit as st
import sympy as sp

def add_multiplication_sign(equation_str):
    # Insert * between a number and a variable (e.g., '2x' -> '2*x')
    equation_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation_str)
    equation_str = re.sub(r'(\d)\(', r'\1*(', equation_str)
    return equation_str


def text_config(size, title, aligmement, color):
    return st.markdown(f"<{size} style='text-align: {aligmement}; color: {color};'>{title}</h1>",
                       unsafe_allow_html=True)

def page_title(title, size="h3", color="red"):
    return text_config(size=size, title=title.upper(), aligmement="center", color=color)

def latex_converter(eq):
    if "=" in eq:
        eq = re.sub(r'={1,}', '==', eq)
        eq = add_multiplication_sign(eq)
        # eq = eq.replace('=', '==')
        eq = sp.sympify(eq, evaluate=False)
        latex_equation = sp.latex(eq)
        return latex_equation
    else:
        eq = add_multiplication_sign(eq)
        eq = eq.replace("^", "**")
        eq = sp.sympify(eq)
        latex_equation = sp.latex(eq)
        return latex_equation

latex_eq = latex_converter("1/2x + 5")
print(latex_eq)