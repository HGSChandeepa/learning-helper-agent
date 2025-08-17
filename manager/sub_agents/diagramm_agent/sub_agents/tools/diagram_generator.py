import os
import subprocess
import uuid
from google.adk.tools import FunctionTool
from typing import Dict, Any

# Path to your .venv Python executable
VENV_PYTHON = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")  # Windows
# For Linux/Mac: os.path.join(os.getcwd(), ".venv", "bin", "python")

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

def run_c4_diagram(code: str) -> Dict[str, Any]:
    print("Running C4 diagram code to generate image...")

    # Current working directory
    workdir = os.getcwd()
    print(f"Using working directory: {workdir}")

    # Ensure diagrams folder exists
    diagrams_folder = os.path.join(workdir, "diagrams")
    os.makedirs(diagrams_folder, exist_ok=True)

    # Paths for script and output image
    script_path = os.path.join(workdir, "diagram.py")
    output_file = os.path.join(diagrams_folder, f"diagram_{uuid.uuid4().hex}.png")

    try:
        # Write the Python diagram code to diagram.py
        with open(script_path, "w") as f:
            f.write(code)

        # Environment variables for the diagrams package
        env = os.environ.copy()
        env["DIAGRAMS_OUTPUT_FORMAT"] = "png"
        env["DIAGRAMS_OUTPUT_FILENAME"] = output_file

        # Run the Python script using .venv Python
        subprocess.run(
            [VENV_PYTHON, script_path],
            check=True,
            env=env,
            cwd=workdir
        )

        if os.path.exists(output_file):
            return {
                "image_path": output_file,
                "format": "png",
                "description": "Diagram image generated successfully",
                "status": "success"
            }
        else:
            return {
                "image_path": None,
                "format": "png",
                "description": "No image file was generated",
                "status": "error"
            }

    except subprocess.CalledProcessError as e:
        return {
            "image_path": None,
            "format": "png",
            "description": f"Error running diagram code: {e}",
            "status": "error"
        }
    except Exception as e:
        return {
            "image_path": None,
            "format": "png",
            "description": f"Unexpected error: {str(e)}",
            "status": "error"
        }

# Create the runner tool
run_c4_tool = FunctionTool(func=run_c4_diagram)
