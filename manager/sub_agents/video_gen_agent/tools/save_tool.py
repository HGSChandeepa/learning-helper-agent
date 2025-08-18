from google.adk.tools import FunctionTool
from typing import Optional, Dict, Any
import os
import subprocess
import uuid

VENV_PYTHON = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")  # Windows
# For Linux/Mac: os.path.join(os.getcwd(), ".venv", "bin", "python")

def run_animation_code(code: str, filename: Optional[str] = None) -> Dict[str, Any]:
    """
    Execute matplotlib animation code and generate GIF file.
    
    Args:
        code (str): The Python animation code to execute
        filename (Optional[str]): Custom filename for the output GIF
    
    Returns:
        Dict[str, Any]: Result of code execution and file generation
    """
    print("Running animation code to generate GIF...")

    workdir = os.getcwd()
    animations_folder = os.path.join(workdir, "animations")
    os.makedirs(animations_folder, exist_ok=True)

    # Generate unique filename if not provided
    if filename is None:
        filename = f"animation_{uuid.uuid4().hex[:8]}.gif"
    elif not filename.endswith('.gif'):
        filename += '.gif'

    script_path = os.path.join(workdir, "temp_animation.py")
    output_gif = os.path.join(animations_folder, filename)

    try:
        # Replace default save names in code
        modified_code = code
        for default_name in ['educational_animation.gif', 'animation.gif', 'animation_v1.gif', 'animation_v2.gif']:
            modified_code = modified_code.replace(f'.save("{default_name}"', f'.save("{output_gif}"')

        # Write code to temporary file
        with open(script_path, "w", encoding='utf-8') as f:
            f.write(modified_code)

        env = os.environ.copy()
        env["MPLBACKEND"] = "Agg"

        result = subprocess.run(
            [VENV_PYTHON, script_path],
            check=True,
            env=env,
            cwd=workdir,
            capture_output=True,
            text=True,
            timeout=120
        )

        # Remove temporary script
        if os.path.exists(script_path):
            os.remove(script_path)

        if os.path.exists(output_gif):
            file_size_mb = os.path.getsize(output_gif) / (1024 * 1024)
            return {
                "gif_path": output_gif,
                "filename": filename,
                "file_size_mb": round(file_size_mb, 2),
                "format": "gif",
                "description": f"Animation GIF generated successfully: {filename}",
                "status": "success",
                "stdout": result.stdout or "Animation completed successfully",
                "stderr": result.stderr or None
            }
        else:
            return {
                "gif_path": None,
                "filename": filename,
                "file_size_mb": 0,
                "format": "gif",
                "description": "No GIF file was generated",
                "status": "error",
                "stdout": result.stdout,
                "stderr": result.stderr
            }

    except subprocess.TimeoutExpired:
        return {
            "gif_path": None,
            "filename": filename,
            "file_size_mb": 0,
            "format": "gif",
            "description": "Animation generation timed out (exceeded 2 minutes)",
            "status": "error",
            "stdout": None,
            "stderr": "Timeout error"
        }
    except subprocess.CalledProcessError as e:
        return {
            "gif_path": None,
            "filename": filename,
            "file_size_mb": 0,
            "format": "gif",
            "description": f"Error running animation code: {e}",
            "status": "error",
            "stdout": getattr(e, 'stdout', None),
            "stderr": getattr(e, 'stderr', None)
        }
    except Exception as e:
        return {
            "gif_path": None,
            "filename": filename,
            "file_size_mb": 0,
            "format": "gif",
            "description": f"Unexpected error: {str(e)}",
            "status": "error",
            "stdout": None,
            "stderr": str(e)
        }
    finally:
        if os.path.exists(script_path):
            try:
                os.remove(script_path)
            except:
                pass

# Create the animation execution tool
animation_runner_tool = FunctionTool(
    func=run_animation_code,
)
