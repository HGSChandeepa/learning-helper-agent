from google.adk.tools import FunctionTool
from typing import Dict, Any
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def generate_c4_diagram(prompt: str) -> Dict[str, Any]:
    """
    Generate a Python C4 diagram (using diagrams package) from a natural language prompt.
    
    Args:
        prompt (str): The user's request for a diagram.
    
    Returns:
        Dict[str, Any]: A dictionary containing the generated diagram code and metadata.
    """
    print(f"Generating C4 diagram for prompt: {prompt}...")
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-001')
        
        structured_prompt = f"""
        You are an assistant that generates Python code for C4 diagrams using the `diagrams` package.
        
        The user request: {prompt}
        
        Follow these rules:
        1. Import necessary classes from `diagrams` and `diagrams.c4` (Person, Container, Database, System, SystemBoundary, Relationship).
        2. Wrap the diagram inside a `with Diagram("...")` context block.
        3. Define components (e.g., Person, Container, Database, System).
        4. Use `Relationship` objects to connect them.
        5. Ensure the code is valid Python and ready to run.
        
        Example:

        from diagrams import Diagram
        from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

        graph_attr = {{
            "splines": "spline",
        }}

        with Diagram("Container diagram for Internet Banking System", direction="TB", graph_attr=graph_attr):
            customer = Person(
                name="Personal Banking Customer", description="A customer of the bank, with personal bank accounts."
            )

            with SystemBoundary("Internet Banking System"):
                webapp = Container(
                    name="Web Application",
                    technology="Java and Spring MVC",
                    description="Delivers the static content and the Internet banking SPA.",
                )

                api = Container(
                    name="API Application",
                    technology="Java and Spring MVC",
                    description="Provides Internet banking functionality via JSON/HTTPS API.",
                )

                database = Database(
                    name="Database",
                    technology="Oracle",
                    description="Stores user info and banking data.",
                )

            customer >> Relationship("Uses") >> webapp
            webapp >> Relationship("Calls API") >> api
            api >> Relationship("Reads/Writes") >> database

        Now, generate the diagram code for: {prompt}
        """

        response = model.generate_content(structured_prompt)

        code = response.text.strip()

        return {
            "diagram_code": code,
            "format": "python",
            "description": f"C4 diagram code for: {prompt}",
            "status": "success"
        }

    except Exception as e:

        print(f"Error generating C4 diagram: {str(e)}")
        # Return an error response if generation fails
        return {
            "diagram_code": None,
            "format": "python",
            "description": f"Error generating C4 diagram: {str(e)}",
            "status": "error"
        }

# Create the C4 diagram tool
c4_diagram_tool = FunctionTool(
    func=generate_c4_diagram,
)
