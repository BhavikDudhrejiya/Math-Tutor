import re
import streamlit as st

def add_multiplication_sign(equation_str):
    # Insert * between a number and a variable (e.g., '2x' -> '2*x')
    equation_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation_str)
    equation_str = re.sub(r'(\d)\(', r'\1*(', equation_str)
    return equation_str

def text_config(size=5, title="", aligmement="center", color="green"):
    return st.markdown(f"<{size} style='text-align: {aligmement}; color: {color};'>{title}</h1>", unsafe_allow_html=True)
