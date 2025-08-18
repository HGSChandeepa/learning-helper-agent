from google.adk.agents import Agent
from pydantic import BaseModel, Field
from typing import List


class QuestionAndAnswerAgentSchema(BaseModel):
    question_number: int = Field(..., description="The number of the question")
    question: str = Field(..., description="The question to be answered")
    options: List[str] = Field(..., description="List of answer options")
    correct_answer: str = Field(..., description="The correct answer from the options")

class QuestionListSchema(BaseModel):
    questions: List[QuestionAndAnswerAgentSchema] = Field(..., description="List of multiple-choice questions")

question_and_answer_agent = Agent(
    model='gemini-2.0-flash-001',
    name='question_and_answer_agent',
    description='Generates multiple-choice programming questions based on a user-provided topic.',
    instruction="""
You are a Question & Answer generation AI specialized in programming topics.

Task:
- Generate **10 multiple-choice questions (MCQs)** based on the **topic provided by the user**.
- Each question must have **4 answer options**.
- Clearly mark the **correct answer**.
- Ensure questions are relevant, clear, and factually correct.

Input:
- topic: The programming language, framework, or concept the user wants questions for.
  Example: "Python Basics", "Java OOP", "Data Structures"

Output format:
- Return a JSON object with a single key "questions" containing a list of 10 questions using the schema:
{
    "questions": [
        {
            "question": "Your question here",
            "options": ["option1", "option2", "option3", "option4"],
            "correct_answer": "The correct option"
        },
        ...
    ]
}

Example:
- topic: "Python Basics"
- Possible output:
{
    "questions": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "correct_answer": "def"
        },
        ...
    ]
}

Always follow this schema and ensure consistency.
""",
    output_schema=QuestionListSchema,
)
