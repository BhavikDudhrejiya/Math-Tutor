import streamlit as st
from utils import *

from validation_engine import MathValidation
from sympy import latex
from hint_generator import HintGenerator

st.sidebar.image("logo2.png", width=300)
st.sidebar.divider()

equations_book = ["2x + 3 = 11",
                  "5x - 7 = 3x + 9",
                  "4(x-2) = 2(x + 5)",
                  "3(2x + 4) = 18",
                  "7x + 2  = 4x + 20",
                  "3x + 5 - 20 = 0",
                  "3x - 7 = 2",
                  "3x - 2 = 2(x - 6)",
                  "(4x - 7)/5 + 1 = -2",
                  "2x + 3(x + 4) = 422"]


modules = st.sidebar.selectbox("**Please the modules:**", ["Solve for Linear Equation",
                                                           "Solve for Inequalities"])

if modules=="Solve for Linear Equation":
    on_hint_service = st.toggle("**Use AI Hint**")

    problem = st.sidebar.selectbox("**Please select equation to solve:**", equations_book)

    model_choice = st.sidebar.radio("**AI Model:**", ["Gemini", "Ollama"], index=1, horizontal=True)

    problem_description = "Solve linear equation in one variable"
    page_title(title=problem_description, color="yellow", size="h2")

    if problem is not None:
        page_title(title=problem, color="#40E0D0")
        st.divider()
        st.latex(latex_converter(problem))

    if "answer" not in st.session_state.keys():
        st.session_state.answer = []

    steps = st.chat_input("Start solving equation...")

    if "answer" in st.session_state.keys():
        for i in st.session_state.answer:
            st.latex(latex_converter(i))

    if steps is not None:
        validator = MathValidation()
        problem_solution = validator.validate_linear_equation(problem=problem)
        step_solution = validator.validate_linear_equation(problem=steps)

        if problem_solution==step_solution and steps.replace(" ","")==f"x={step_solution[0]}":
            st.session_state.answer.append(steps)
            st.latex(latex_converter(steps))
            st.info("✅ Well done! You've completed the final step of the equation. Feel free to try another problem. ✅")
        elif problem_solution==step_solution and steps.replace(" ","")!=f"x={step_solution[0]}":
            st.session_state.answer.append(steps)
            st.latex(latex_converter(steps))
            st.success("✅ Excellent! You've correctly solved this step of the equation. Now, move on to the next step. ✅")
        else:
            st.latex(latex_converter(steps))
            st.error(f"❌ There appears to be an issue with your solution step: {steps} ❌. Please provide the correct step.")

            try:
                last_valid_step = st.session_state.answer[-1]
            except:
                last_valid_step = problem

            if on_hint_service:
                generate_hint = HintGenerator()
                if model_choice == "Ollama":
                    hint = generate_hint.generate_hint_ollama(topic="Solve linear equation in one variable",
                                                       problem=problem,
                                                       last_valid_step=last_valid_step,
                                                       answer=problem_solution[0],
                                                       invalid_step=steps)
                else:
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