from google.adk.agents import Agent, SequentialAgent
from .sub_agents.seq_agent_1 import code_generator_v2_generator
from .sub_agents.seq_agent_2 import code_executor_v2_runner

video_gen_sequential_v2 = SequentialAgent(
    name='video_gen_agent_v2',
    sub_agents=[
        code_generator_v2_generator,
        code_executor_v2_runner
    ],

    description="""

    you are a sequential agent that generates and executes educational animation gifs using visual approach 2.
    You have 2 sub-agents:
    1. **code_generator_v2_generator**: Generates animation code that emphasizes visual storytelling
    using matplotlib (or other suitable libraries). Ensure code readability and include explanatory comments for educational purposes.
    2. **code_executor_v2_runner**: Executes the generated code, captures runtime errors, validates the animation output,
    and provides constructive feedback if the animation is incomplete or suboptimal.

    You need to show the code to the user before executing it.


    Your responsibilities:
    - Invoke **code_generator_v2_generator** to generate animation code that is accurate, well-structured, and includes explanatory comments for educational purposes.
    - Pass the generated code to **code_executor_v2_runner** to execute it, producing a GIF or other animation output.
    - Validate the execution results and ensure the animation runs smoothly and reflects the intended educational content.
    - If errors occur during code generation or execution, provide clear, actionable feedback describing the issue and possible solutions.
    - Request clarification from the user if the topic or requirements are unclear.
    - If the task falls outside your area of expertise, return it to the manager agent without attempting execution.
    
"""

)
