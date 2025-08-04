from google.adk.tools import FunctionTool
from typing import Dict, Any
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def code_evaluation_tool(code: str) -> Dict[str, Any]:
    """
    Evaluate the provided code, identify issues, and suggest improvements.
    
    Args:
        code (str): The code to be evaluated
        
    Returns:
        Dict[str, Any]: A dictionary containing the analysis results, issues found, and corrected code
    """
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.0-flash-001')
        
        # Create a structured prompt for code evaluation
        structured_prompt = f"""
        Analyze the following code and provide a detailed evaluation:

        ```
        {code}
        ```

        Please provide your response in the following format:

        1. ISSUES
        - List each issue found in point form
        - Include code style issues
        - Include potential bugs
        - Include performance concerns
        - Include security concerns if any

        2. EXPLANATION
        Provide a brief explanation of why each issue is important

        3. CORRECTED CODE
        ```
        [Provide the corrected version of the code here]
        ```

        Ensure the response is structured exactly as specified above with clear separation between sections.
        """
        
        # Generate the response
        response = model.generate_content(structured_prompt)
        
        # Extract sections from the response
        sections = response.text.strip().split('\n\n')
        
        # Parse the response sections
        issues = []
        explanation = ""
        corrected_code = ""
        
        current_section = ""
        for section in sections:
            if section.startswith("1. ISSUES"):
                current_section = "issues"
                continue
            elif section.startswith("2. EXPLANATION"):
                current_section = "explanation"
                continue
            elif section.startswith("3. CORRECTED CODE"):
                current_section = "code"
                continue
                
            if current_section == "issues":
                issues.extend([issue.strip('- ') for issue in section.split('\n') if issue.strip().startswith('-')])
            elif current_section == "explanation":
                explanation = section
            elif current_section == "code":
                corrected_code = section.strip('`')
        
        return {
            "issues": issues,
            "explanation": explanation,
            "corrected_code": corrected_code,
            "status": "success"
        }
        
    except Exception as e:
        return {
            "issues": [],
            "explanation": f"Error analyzing code: {str(e)}",
            "corrected_code": "",
            "status": "error"
        }

# Create the code evaluation tool
code_evaluation_tool = FunctionTool(
 func=code_evaluation_tool,
)   


