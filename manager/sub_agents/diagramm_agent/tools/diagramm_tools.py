from google.adk.tools import FunctionTool
from typing import Dict, Any
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def generate_text_diagram(prompt: str) -> Dict[str, Any]:

    print(f"Generating diagram for prompt: {prompt}...")
    """
    Generate a text-based diagram based on the user's prompt using Gemini.
    
    Args:
        prompt (str): The user's request for a diagram
        
    Returns:
        Dict[str, Any]: A dictionary containing the generated diagram and any additional information
    """
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.0-flash-001')
        
        # Create a structured prompt that guides the model to generate diagrams
        structured_prompt = f"""
        Please create a text-based diagram based on the following request: {prompt}
        
        Follow these guidelines:
        1. Use ASCII characters or Unicode box-drawing characters for the diagram
        2. Keep the diagram clear and well-structured
        3. Include labels and necessary explanations
        4. Ensure the diagram fits within a reasonable width (max 80 characters)
        5. Add a brief description of what the diagram represents
        
        Format the response as a diagram followed by a description.
        """
        
        # Generate the response
        response = model.generate_content(structured_prompt)
        
        # Extract the diagram and description from the response
        result = response.text.strip().split('\n\n')
        diagram = result[0]
        description = result[1] if len(result) > 1 else "No description provided"
        
        return {
            "diagram": diagram,
            "format": "text",
            "description": description,
            "status": "success"
        }
        
    except Exception as e:
        return {
            "diagram": None,
            "format": "text",
            "description": f"Error generating diagram: {str(e)}",
            "status": "error"
        }

# Create the diagram generation tool
diagram_tool = FunctionTool(
    func=generate_text_diagram,
)


