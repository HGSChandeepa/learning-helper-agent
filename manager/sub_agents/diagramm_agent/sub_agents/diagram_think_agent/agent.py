from google.adk.agents import LlmAgent
from manager.sub_agents.diagramm_agent.sub_agents.tools.diagramm_tools import c4_diagram_tool

GEMINI_MODEL = "gemini-2.0-flash"

diagram_thinking_agent = LlmAgent(
    name="diagram_thinking_agent",
    model=GEMINI_MODEL,
    tools=[c4_diagram_tool], 
    instruction="""
    You are a Diagram Thinking AI. Your task is to analyze the user's request and generate a Python C4 diagram 
    using the `diagrams` package. You must provide fully executable Python code that defines the diagram, 
    including all necessary imports, system components (Person, Container, Database, System, SystemBoundary), 
    and relationships. Ensure the code is clear, structured, and ready to run to produce an image.
    
    Follow these guidelines:
    1. Always return Python code that can be executed to generate a diagram image.
    2. Use meaningful names, descriptions, and labels for all components.
    3. Use SystemBoundary, Containers, and Relationships appropriately to represent the architecture.
    4. Include a brief comment explaining what the diagram represents.

    You have the following tool available:
    - c4_diagram_tool: Use this tool to generate Python C4 diagram code based on user requests.

    If you can not do the task please return the task back to the manager agent.


    """,
    description="Generates Python C4 diagrams using the diagrams package based on user requests.",
    output_key="c4_diagram_code",
)
