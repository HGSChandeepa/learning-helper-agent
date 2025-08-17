from google.adk.agents import LlmAgent
from manager.sub_agents.diagramm_agent.sub_agents.tools.diagram_generator import run_c4_tool

GEMINI_MODEL = "gemini-2.0-flash"

diagram_save_agent = LlmAgent(
    name="diagram_save_agent",
    model=GEMINI_MODEL,
    tools=[run_c4_tool],
    instruction="""
You are a Diagram Execution AI.

Your task is to take valid Python C4 diagram code (from the previous agent) 
and run it to produce an image file.

How to use the tool:
1. Call the `run_c4_diagram` tool with the Python code.
2. Ensure the output includes the path to the generated diagram image.
3. Return a structured response with image path, format, description, and status.

Input Python code:
{c4_diagram_code['diagram_code']}

Output:
Provide a structured response as JSON with the image_path, format, description, and status.
""",
    description="Executes Python C4 diagram code to generate diagram images using the `diagrams` package.",
    output_key="diagram_image_result",
)
