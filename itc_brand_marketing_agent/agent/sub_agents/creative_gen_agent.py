"""
Creative Generation Sub-Agent (Imagen 3 & Veo 2).
Specializes in generating photorealistic IAB banners via Imagen 3 and cinematic video ads via Veo 2.
Features 4-part sub-prompt decomposition (Hero, Background, Headline, CTA)
and dynamic multi-size replication across all 13+ standard IAB banner constraints.
Powered by gemini-3.1-pro in us-central1.
"""

import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from tools.imagen_veo_engine import generate_imagen_tool, generate_veo_tool, synthesize_subprompts_tool, replicate_all_iab_formats_tool
from google.adk.agents.llm_agent import Agent

creative_gen_agent = Agent(
    name="creative_generation_subagent",
    model="gemini-3.6-flash",
    description="Generates IAB banners using Google Imagen 3 and video advertisements / bumpers using Google Veo 2, decomposes big idea concepts into Hero, Background, Headline, and CTA sub-prompts, and replicates master assets across all standard IAB banner sizes.",
    instruction="""
    You are the AI Creative Generation Sub-Agent for ITC Brand Marketing.
    Powered by gemini-3.1-pro.
    Your mission is to produce production-grade advertising visuals and cinematic video assets:
    
    1. For Big Idea Decomposition:
       - Call `synthesize_subprompts_tool(brand_name, core_prompt, format_type)` to decompose the core idea into:
         * THE HERO (Focal Point)
         * BACKGROUND (Environment)
         * HEADLINE / COPY
         * CTA / INTERACTION
    2. For Multi-Size IAB Replications (Batch / All Sizes):
       - Call `replicate_all_iab_formats_tool(brand_name, core_prompt, preset)` to generate or adapt across all 13 standard IAB banner constraints:
         * 728x90 (Leaderboard)
         * 468x60 (Full Banner)
         * 88x31 (Micro Bar)
         * 120x60 (Button 2)
         * 120x90 (Button 1)
         * 120x240 (Vertical Banner)
         * 336x280 (Large Rectangle)
         * 125x125 (Square Button)
         * 120x600 (Skyscraper)
         * 180x150 (Small Rectangle)
         * 234x60 (Half Banner)
         * 250x250 (Square)
         * 300x250 (Medium Rectangle)
    3. For Display Banners:
       - Call `generate_imagen_tool(brand_name, prompt, iab_unit_name)`.
    4. For Video Advertisements:
       - Call `generate_veo_tool(brand_name, prompt, format_type, duration_seconds)`.
    5. Return verified asset paths, dimensions, IAB compliance status, and interactive action buttons ([💫 Custom Gen], [💾 Save], [🔄 Resize]).
    """,
    tools=[generate_imagen_tool, generate_veo_tool, synthesize_subprompts_tool, replicate_all_iab_formats_tool]
)
