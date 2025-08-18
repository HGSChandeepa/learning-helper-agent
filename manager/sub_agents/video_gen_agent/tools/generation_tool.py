from google.adk.tools import FunctionTool
from typing import Dict, Any
import google.generativeai as genai
import os
import subprocess
import uuid

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def generate_animation_code(prompt: str, approach: str = "process") -> Dict[str, Any]:
    """
    Generate matplotlib animation code from a natural language prompt.
    
    Args:
        prompt (str): The user's request for an educational animation.
        approach (str): Animation approach - "process" or "structure"
    
    Returns:
        Dict[str, Any]: A dictionary containing the generated animation code and metadata.
    """
    print(f"Generating {approach} animation for prompt: {prompt}...")
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-001')
        
        if approach == "process":
            approach_instruction = """
            VISUAL APPROACH: Step-by-Step Process Visualization
            - Emphasize sequential steps and process flow
            - Use linear progression and clear transitions
            - Focus on "how things work" rather than "what they are"
            - Show cause-and-effect relationships
            - Colors: #3498db (blue), #e74c3c (red), #27ae60 (green), #f39c12 (orange)
            """
        else:  # structure
            approach_instruction = """
            VISUAL APPROACH: Comparative and Structural Visualization
            - Emphasize relationships and comparisons
            - Use side-by-side or layered visualizations
            - Focus on "what things are" and their relationships
            - Show multiple perspectives simultaneously
            - Colors: #9b59b6 (purple), #e67e22 (orange), #1abc9c (teal), #f1c40f (yellow)
            """
        
        structured_prompt = f"""
        You are an expert at creating educational matplotlib animations with dark themes.
        
        User request: {prompt}
        
        {approach_instruction}
        
        TECHNICAL REQUIREMENTS:
        - Black background (#1a1a1a)
        - Figure size: (12, 8)
        - Frames: 50-70 (lightweight)
        - FPS: 6
        - DPI: 100
        - White text (#ffffff) for titles
        - Light grey text (#cccccc) for labels
        - Remove all axes and spines
        - Use smooth transitions between phases
        
        CODE TEMPLATE:
        ```python
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation
        import matplotlib.patches as patches
        import numpy as np

        # Dark theme setup
        fig, ax = plt.subplots(figsize=(12, 8), facecolor='#1a1a1a')
        ax.set_facecolor('#1a1a1a')
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        ax.set_title("{{TOPIC_TITLE}}", fontsize=16, color='#ffffff', pad=20, weight='bold')

        # Initialize visual elements (rectangles, circles, arrows, text)
        # Use patches.Rectangle, patches.Circle, patches.FancyArrowPatch
        # Create text elements with appropriate colors

        def animate(frame):
            # Clear previous frame elements if needed
            ax.clear()
            ax.set_facecolor('#1a1a1a')
            ax.set_xlim(0, 12)
            ax.set_ylim(0, 8)
            ax.axis('off')
            ax.set_title("{{TOPIC_TITLE}}", fontsize=16, color='#ffffff', pad=20, weight='bold')
            
            # Phase-based animation logic
            if frame < 15:
                # Phase 1: Introduction
                pass
            elif frame < 35:
                # Phase 2: Main concept building
                pass
            elif frame < 55:
                # Phase 3: Dynamic demonstration
                pass
            else:
                # Phase 4: Summary/complete view
                pass
            
            # Return list of artists for blitting (optional)

        # Create animation
        ani = FuncAnimation(fig, animate, frames=60, interval=167, repeat=True, blit=False)
        
        # Save animation
        ani.save("educational_animation.gif", writer='pillow', fps=6, dpi=100)
        plt.show()
        ```
        
        EXAMPLES BY TOPIC:
        
        JavaScript Functions:
        - Show function definition → parameters → execution → return
        - Use boxes for function blocks, arrows for data flow
        - Animate parameter passing and return values
        
        Python Lists:
        - Show list creation → indexing → methods (append, pop, slice)
        - Use rectangles for list elements, highlight current operations
        
        Sorting Algorithms:
        - Show array elements as bars or rectangles
        - Animate comparisons and swaps with color changes
        - Highlight current positions being compared
        
        Database Queries:
        - Show table structures → query execution → result set
        - Use tables with highlighting for selected rows
        
        Now generate complete, runnable matplotlib animation code for: {prompt}
        
        Make sure the code is complete, properly formatted, and ready to execute.
        """

        response = model.generate_content(structured_prompt)
        code = response.text.strip()
        
        # Clean up the code if it has markdown formatting
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()

        print("===========================Generated animation code================================:")
        print(code)
        print("===========================Generated animation code================================:")

        return {
            "animation_code": code,
            "approach": approach,
            "format": "python",
            "description": f"{approach.capitalize()} animation code for: {prompt}",
            "status": "success"
        }

    except Exception as e:
        print(f"Error generating animation code: {str(e)}")
        return {
            "animation_code": None,
            "approach": approach,
            "format": "python",
            "description": f"Error generating animation code: {str(e)}",
            "status": "error"
        }

# Create the animation code generation tool
animation_generator_tool = FunctionTool(
    func=generate_animation_code,
)