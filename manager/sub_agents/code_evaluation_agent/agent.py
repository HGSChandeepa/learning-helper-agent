from google.adk.agents import Agent

code_evaluation_agent = Agent(
    model='gemini-2.0-flash-001',
    name='code_evaluation_agent',
    description='A helpful assistant for code evaluation tasks.',
    instruction='Evaluate code snippets and provide feedback.',
)
