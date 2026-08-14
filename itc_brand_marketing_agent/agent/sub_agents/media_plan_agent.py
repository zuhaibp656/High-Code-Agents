"""
Media Planning & Budget Sub-Agent.
Specializes in multi-channel media planning, budget splits, KPI benchmarks,
and exporting spreadsheet reports across YouTube, Meta, GDN, and Quick-Commerce.
"""

from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

vertex_flash_model = Gemini(model_name="gemini-2.5-flash", client_kwargs={"vertexai": True})

from ..tools.doc_reader_engine import (
    read_marketing_document,
    save_marketing_document
)
from ..tools.brand_knowledge_engine import (
    check_or_create_media_plan,
    lookup_brand
)
from ..tools.campaign_engine import (
    build_full_itc_campaign
)

media_plan_agent = Agent(
    name="media_planning_subagent",
    model=vertex_flash_model,
    description="Specializes in checking, extracting, and synthesizing full multi-channel media strategies, channel budget allocations (YouTube, Meta, GDN, Q-Commerce), and KPI metrics for ITC brands.",
    instruction="""
    You are the Media Planning & Budget Sub-Agent for ITC Brand Marketing.
    Your mission:
    1. Check if an existing media plan or historical analytics report exists in `ITC Marketing Files/Media Plan/` or `Historical campaign and channel performance/` using `check_or_create_media_plan(brand_name, budget_inr_lakhs)` or `read_marketing_document`.
    2. Formulate comprehensive multi-channel media plans and format them into clear, beautiful MARKDOWN TABLES:
       - Channel breakdown (YouTube/OTT, Meta/Instagram, Google Display Network, Quick-Commerce Blinkit/Zepto).
       - Format types (16:9 In-stream, 9:16 Reels, IAB Banners, 1:1 Sponsored Tiles).
       - Budget allocation (% and INR Lakhs).
       - Target KPIs (VTR, CTR, ROAS).
       - Target audience persona mapping.
    3. Save the synthesized media plan into `Media Plan/` and export CSV spreadsheets when requested.
    """,
    tools=[
        read_marketing_document,
        save_marketing_document,
        check_or_create_media_plan,
        build_full_itc_campaign,
        lookup_brand
    ]
)
