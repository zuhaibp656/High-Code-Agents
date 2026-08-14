"""
IAB Spec & LEAN Compliance Sub-Agent.
Specializes in verifying ad dimensions, aspect ratios, file weights, and LEAN standards
for all IAB display and video ad units.
Powered by gemini-3.6-flash in us-central1.
"""

import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from tools.iab_specs_engine import get_iab_specs_tool
from google.adk.agents.llm_agent import Agent

iab_compliance_agent = Agent(
    name="iab_compliance_subagent",
    model="gemini-3.5-flash",
    description="Validates ad assets against IAB New Ad Portfolio specifications and LEAN performance principles (file weight, requests, CPU, mute status).",
    instruction="""
    You are the IAB Ad Specifications & Compliance Sub-Agent.
    Powered by gemini-3.6-flash.
    Your mission is to ensure every generated creative strictly complies with IAB standards:
    
    1. Look up ad unit dimensions and limits using `get_iab_specs_tool(unit_or_size)`.
    2. Check the required specs:
       - Fixed dimensions (e.g. 728x90, 300x250, 970x250, 300x600, 1080x1920, 1920x1080)
       - Aspect ratios (e.g. 8:1, 1:1, 4:1, 1:2, 9:16, 16:9)
       - Initial Load Max File Weight (kB)
       - Subload Max File Weight (kB)
       - LEAN Guidelines: Max 10 host-initiated requests, Max 30% CPU load, default audio MUTED, 1px distinct border, IBA AdChoices tag (<5kB).
    3. Provide the exact mapping between IAB unit and Imagen 3 / Veo 2 generation aspect ratios.
    """,
    tools=[get_iab_specs_tool]
)
