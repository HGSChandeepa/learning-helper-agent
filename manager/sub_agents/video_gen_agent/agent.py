from google.adk.agents import Agent

video_gen_agent = Agent(
    model='gemini-2.0-flash-001',
    name='video_gen_agent',
    description='A helpful assistant for video generation tasks.',
    instruction='Generate videos based on user input.',
)
