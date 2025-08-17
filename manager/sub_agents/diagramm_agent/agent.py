from google.adk.agents import SequentialAgent
from manager.sub_agents.diagramm_agent.sub_agents.diagram_think_agent.agent import diagram_thinking_agent
from manager.sub_agents.diagramm_agent.sub_agents.diagram_save_agent.agent import diagram_save_agent

diagram_pipeline_agent = SequentialAgent(
    name="diagram_pipeline_agent",
    sub_agents=[diagram_thinking_agent, diagram_save_agent],
    description="""
    This agent manages the diagram generation workflow in sequence:
    1. Calls diagram_thinking_agent to analyze the user's request and generate executable Python C4 diagram code.
    2. Passes the generated code to diagram_save_agent to run the code and produce a diagram image.
    The final output includes the image path and a description of the diagram.
    """,
)
