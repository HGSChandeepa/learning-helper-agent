from google.adk.agents import Agent

lesson_images_gen_agent = Agent(
    model='gemini-2.0-flash-001',
    name='lesson_images_gen_agent',
    description='A helpful assistant for generating lesson images.',
    instruction='Generate images for lesson content based on user input.',
)
