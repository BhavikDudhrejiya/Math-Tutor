import streamlit as st
from streamlit import title
from utils import *

from validation_engine import MathValidation
from sympy import latex
from hint_generator import HintGenerator

st.sidebar.image("logo.png", width=300)
st.sidebar.divider()

equations_book = ["2x + 3 = 11",
                  "5x - 7 = 3x + 9",
                  "4(x-2) = 2(x + 5)",
                  "3(2x + 4) = 18",
                  "7x + 2  = 4x + 20"]


modules = st.sidebar.selectbox("Please the modules", ["Solve for Linear Equation",
                                                      "Solve for Inequalities"])

if modules=="Solve for Linear Equation":
    on_hint_service = st.toggle("Use Hint")

    problem = st.sidebar.selectbox("Please select equation to solve:", equations_book)

    problem_description = "`Solve linear equation in one variable:`".upper()

    if problem is not None:
        st.subheader(problem_description + " " + problem)
        st.divider()
        st.latex(latex(problem))

    if "answer" not in st.session_state.keys():
        st.session_state.answer = []

    steps = st.chat_input("Start solving equation...")

    if "answer" in st.session_state.keys():
        for i in st.session_state.answer:
            st.latex(latex(i))

    if steps is not None:
        st.session_state.answer.append(steps)
        st.latex(latex(steps))

        validator = MathValidation()
        problem_solution = validator.validate_linear_equation(problem=problem)
        step_solution = validator.validate_linear_equation(problem=steps)

        if problem_solution==step_solution and steps.replace(" ","")==f"x={step_solution[0]}":
            st.info("✅ Well done! You've completed the final step of the equation. Feel free to try another problem. ✅")
        elif problem_solution==step_solution and steps.replace(" ","")!=f"x={step_solution[0]}":
            st.success("✅ Excellent! You've correctly solved this step of the equation. Now, move on to the next step. ✅")
        else:
            st.error("❌ It seems there might be an error in your solution step. ❌")

            try:
                last_valid_step = st.session_state.answer[-2]
            except:
                last_valid_step = problem

            if on_hint_service:
                generate_hint = HintGenerator()
                hint = generate_hint.generate_hint(topic="Solve linear equation in one variable",
                                                   problem=problem,
                                                   last_valid_step=last_valid_step,
                                                   answer=problem_solution[0],
                                                   invalid_step=steps)
                with st.expander("💡"):
                    st.info(f"Problem : {problem}")
                    st.info(f"Last valid step : {last_valid_step}")
                    st.info(f"Answer of the problem: {problem_solution[0]}")
                    st.info(f"Invalid step : {steps}")
                    st.success(hint)


    if st.sidebar.button("Clear All"):
        st.session_state.clear()
else:
    pass

# st.text_input("Equation:")