from google.adk.agents import Agent

question_and_answer_agent = Agent(
    model='gemini-2.0-flash-001',
    name='question_and_answer_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
