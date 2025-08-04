from google.adk.agents import Agent
from manager.sub_agents.diagramm_agent.tools.diagramm_tools import diagram_tool


diagramm_agent = Agent(
    model='gemini-2.0-flash-001',
    name='diagramm_agent',
    description='A helpful assistant for diagram generation tasks.',
    instruction=
    '''
        You are a diagram generation expert. When receiving a request, analyze it carefully and generate an appropriate text-based diagram that best represents the requested information. The diagrams can include ASCII art, flow charts, or any other text-based visual representation.

        you have the following tools available:
        - generate_diagram: Use this tool to create a text-based diagram based on user input
    ''',
    tools=[diagram_tool]
)
