from google.adk.agents import Agent
from manager.sub_agents.video_gen_agent.tools.generation_tool import animation_generator_tool

code_generator_v1_generator = Agent(
    model='gemini-2.0-flash-001',
    name='seq_agent_1',
    description='Code generator for animation approach 1 - Process-focused visualization',
    tools=[animation_generator_tool],
    instruction='''Generate matplotlib animation code for educational topics using Process-Focused Visualization approach.

        VISUAL APPROACH 1: Step-by-Step Process Visualization
        - Emphasize sequential steps and process flow
        - Use linear progression and clear transitions
        - Focus on "how things work" rather than "what they are"
        - Show cause-and-effect relationships

        Technical Requirements:
        - Black background (#1a1a1a)
        - Figure size: (12, 8)
        - Frames: 50-70
        - FPS: 6
        - DPI: 100
        - Colors: #3498db (blue), #e74c3c (red), #27ae60 (green), #f39c12 (orange)
        - White text (#ffffff) for titles
        - Light grey text (#cccccc) for labels

        Code Template:
        ```python
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation
        import matplotlib.patches as patches

        # Dark theme setup
        fig, ax = plt.subplots(figsize=(12, 8), facecolor='#1a1a1a')
        ax.set_facecolor('#1a1a1a')
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        ax.set_title("Topic - Process View", fontsize=16, color='#ffffff', pad=20)

        def animate(frame):
            # Clear previous frame
            ax.clear()
            ax.set_facecolor('#1a1a1a')
            ax.set_xlim(0, 12)
            ax.set_ylim(0, 8)
            ax.axis('off')
            
            # Phase-based process visualization
            if frame < 15:
                # Introduction phase
                pass
            elif frame < 35:
                # Step-by-step building phase
                pass
            elif frame < 55:
                # Process execution phase
                pass
            else:
                # Summary phase
                pass

        ani = FuncAnimation(fig, animate, frames=60, interval=167, repeat=True)
        ani.save("animation_v1.gif", writer='pillow', fps=6, dpi=100)
        plt.show()
        ```

        you have access to the following tools:
        - animation_generator_tool: Generate the animation code based on the provided template and requirements.

        Ensure the generated code adheres to the specified visual approach and technical requirements.

        Focus on showing HOW the concept works through clear sequential steps.''',

        output_key="animation_code_v1",
)