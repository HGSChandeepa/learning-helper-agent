from google.adk.agents import Agent
from manager.sub_agents.video_gen_agent.tools.generation_tool import animation_generator_tool

code_generator_v2_generator = Agent(
    model='gemini-2.0-flash-001',
    name='seq_agent_1',
    tools=[animation_generator_tool],
    description='Code generator for animation approach 2 - Structure-focused visualization',
    instruction='''Generate matplotlib animation code for educational topics using Structure-Focused Visualization approach.

        VISUAL APPROACH 2: Comparative and Structural Visualization
        - Emphasize relationships and comparisons
        - Use side-by-side or layered visualizations
        - Focus on "what things are" and their relationships
        - Show multiple perspectives simultaneously

        Technical Requirements:
        - Black background (#1a1a1a)
        - Figure size: (12, 8)
        - Frames: 50-70
        - FPS: 6
        - DPI: 100
        - Colors: #9b59b6 (purple), #e67e22 (orange), #1abc9c (teal), #f1c40f (yellow)
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
        ax.set_title("Topic - Structure View", fontsize=16, color='#ffffff', pad=20)

        def animate(frame):
            # Clear previous frame
            ax.clear()
            ax.set_facecolor('#1a1a1a')
            ax.set_xlim(0, 12)
            ax.set_ylim(0, 8)
            ax.axis('off')
            
            # Phase-based structural visualization
            if frame < 15:
                # Component introduction
                pass
            elif frame < 35:
                # Relationship building
                pass
            elif frame < 55:
                # Comparative demonstration
                pass
            else:
                # Complete structure view
                pass

        ani = FuncAnimation(fig, animate, frames=60, interval=167, repeat=True)
        ani.save("animation_v2.gif", writer='pillow', fps=6, dpi=100)
        plt.show()
        ```

        you have access to the following tools:
        - animation_generator_tool: Generate the animation code based on the provided template and requirements.
        Ensure the generated code adheres to the specified visual approach and technical requirements.

        Focus on showing WHAT the concept is through structural relationships and comparisons.''',

    output_key="animation_code_v2",
)