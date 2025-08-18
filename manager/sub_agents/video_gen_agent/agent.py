from google.adk.agents import Agent, ParallelAgent
from .sub_agents.video_gen_agent_V1.agent import video_gen_sequential_v1
from .sub_agents.video_gen_agent_V2.agent import video_gen_sequential_v2

video_gen_agent = ParallelAgent(
    name='video_gen_agent',
    sub_agents=[
        video_gen_sequential_v1,
        video_gen_sequential_v2
    ],

    description="""
        Generate 2 different educational animations in parallel for the user's requested topic.
    
        Both agents will create animations with:
        - Black/dark background (#1a1a1a)
        - Minimal, professional design
        - Different visual approaches to the same concept
        - Lightweight performance (50-80 frames, 5-8 fps, 100 DPI)
        - Clear educational value

        The parallel execution will produce 2 unique GIF animations simultaneously.
        
        Each agent will focus on different visual storytelling techniques:
        1. **video_gen_sequential_v1**: Emphasizes visual storytelling through narrative-driven animations.
        2. **video_gen_sequential_v2**: Focuses on structure and relationships, using comparative and structural visualization.

        Ensure both animations are engaging, pedagogically effective, and suitable for educational purposes.

        If the task is outside your expertise, return it to the manager agent without attempting execution.
        If uncertain about the topic, ask the user for clarification.
        
        """

)
