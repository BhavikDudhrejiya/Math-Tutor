import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class HintGenerator:
    def __init__(self, model="gemini-pro"):
        self.__model = model

    def prompt(self, topic, problem, last_valid_step, answer, invalid_step):
        prompt = f"""
        You are a knowledgeable and supportive math tutor specializing in fundamental concepts.
        
        Your task is to guide students by providing helpful hints when they encounter mistakes 
        while learning specific topics.
        
        You will receive the following details:
        - Topic: {topic}
        - Problem: {problem}
        - Last correct step: {last_valid_step}
        - Final answer: {answer}
        - Incorrect step: {invalid_step}
        
        Your goal is to generate a clear and concise hint, addressing the student's mistake and 
        guiding them toward the correct approach for solving the incorrect step.
        
        Hint: '...'
        """
        return prompt

    def load_gemini_model(self):
        model = genai.GenerativeModel(self.__model)
        return model

    def generate_hint(self, topic, problem, last_valid_step, answer, invalid_step):
        prompt = self.prompt(topic, problem, last_valid_step, answer, invalid_step)
        model = self.load_gemini_model()
        response = model.generate_content(prompt)
        return response.text

if __name__=="__main__":
    topic = "Solve the linear equation"
    problem = "2x + 3 = 11"
    last_valid_step = "2x + 3 = 11"
    answer = "x = 4"
    invalid_step = "2x + 3 - 3 = 11"
    generate_hint = HintGenerator()
    hint = generate_hint.generate_hint(topic, problem, last_valid_step, answer, invalid_step)
    print(hint)


