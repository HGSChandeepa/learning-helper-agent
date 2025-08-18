from google.adk.agents import Agent

# import sub agents
from manager.sub_agents.code_evaluation_agent.agent import code_evaluation_agent
from manager.sub_agents.diagramm_agent.agent import diagram_pipeline_agent
from manager.sub_agents.lesson_images_gen_agent.agent import lesson_images_gen_agent
from manager.sub_agents.question_and_answer_agent.agent import question_and_answer_agent
from manager.sub_agents.video_gen_agent.agent import video_gen_agent
from manager.sub_agents.coding_agent.agent import coding_agent


#   root agent
root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A Manager agent that coordinates sub-agents for various tasks.',
    instruction=
    """
    You are a root agent that manages sub-agents for different tasks.And you have the following sub-agents:
    - code_evaluation_agent: Evaluates code snippets and provides feedback.
    - diagram_pipeline_agent: Generates diagrams based on user input and save them.
    - lesson_images_gen_agent: Generates images for lesson content based on user input.
    - question_and_answer_agent: Generates multiple-choice programming questions based on user-provided topics.
    - video_gen_agent: Generates gifs from the ser-provided topics.These gifs are very informative.

    You can delegate tasks to these sub-agents based on user requests and provide the results back to the user.
    Please ensure that each sub-agent is used for its intended purpose and provide clear instructions to them.
    If a task does not fit any of the sub-agents, you can handle it directly.
    Always strive to provide accurate and helpful responses to user queries.    

    """,
    sub_agents=[
        code_evaluation_agent,
        diagram_pipeline_agent,
        lesson_images_gen_agent,
        question_and_answer_agent,
        video_gen_agent,
        coding_agent
    
    ],
)
