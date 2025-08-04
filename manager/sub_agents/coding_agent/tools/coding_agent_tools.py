import requests
import json
from typing import Dict, Any
from google.adk.tools import FunctionTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class CodingAssistant:
    def __init__(self):
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
            
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": os.getenv('SITE_URL', 'https://study-helper-agent.com'),
            "X-Title": os.getenv('SITE_NAME', 'Study Helper Agent')
        }

    def generate_code(self, prompt: str, context: str = "") -> Dict[str, Any]:
        """
        Generate code based on the user's prompt using Qwen Coder model.
        
        Args:
            prompt (str): The user's coding request
            context (str): Additional context or requirements
            
        Returns:
            Dict[str, Any]: A dictionary containing the generated code and explanation
        """
        try:
            # Create a structured message that guides the model
            messages = [
                {
                    "role": "system",
                    "content": """You are an expert programming assistant. When generating code:
                    1. First analyze the requirements thoroughly
                    2. Consider edge cases and potential issues
                    3. Write clean, efficient, and well-documented code
                    4. Include helpful comments explaining complex logic
                    5. Follow best practices and design patterns
                    """
                },
                {
                    "role": "user",
                    "content": f"""Task: {prompt}
                    Additional Context: {context}
                    
                    Please provide:
                    1. Complete code implementation
                    2. Brief explanation of the approach
                    3. Any important notes or considerations
                    """
                }
            ]

            # Make the API request
            response = requests.post(
                url=self.base_url,
                headers=self.headers,
                data=json.dumps({
                    "model": "qwen/qwen3-coder:free",
                    "messages": messages
                })
            )

            # Parse the response
            result = response.json()
            if 'choices' in result:
                generated_content = result['choices'][0]['message']['content']
                
                # Split content into code and explanation
                sections = generated_content.split('\n\n')
                code = ""
                explanation = ""
                
                for section in sections:
                    if section.strip().startswith('```'):
                        code = section.strip('`').strip()
                    else:
                        explanation += section + '\n'

                return {
                    "code": code,
                    "explanation": explanation.strip(),
                    "status": "success"
                }
            else:
                raise Exception("Invalid response format from API")

        except Exception as e:
            return {
                "code": "",
                "explanation": f"Error generating code: {str(e)}",
                "status": "error"
            }

# Initialize the coding assistant
coding_assistant = CodingAssistant()

# Create the coding tool
coding_tool = FunctionTool(
    func=coding_assistant.generate_code
)
