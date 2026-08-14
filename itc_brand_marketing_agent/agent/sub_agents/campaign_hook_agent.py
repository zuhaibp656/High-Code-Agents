"""
Campaign Strategy & Audience Sub-Agent.
Specializes in extracting and synthesizing ITC brand identity, festive/seasonal briefs,
audience segmentation, and consumer pain points.
"""

from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

vertex_flash_model = Gemini(model_name="gemini-2.5-flash", client_kwargs={"vertexai": True})

from ..tools.doc_reader_engine import (
    list_marketing_folders,
    read_marketing_document,
    save_marketing_document
)
from ..tools.brand_knowledge_engine import (
    check_or_create_campaign_brief,
    lookup_brand
)

campaign_hook_agent = Agent(
    name="campaign_strategy_subagent",
    model=vertex_flash_model,
    description="Specializes in checking and synthesizing ITC campaign strategy briefs, target audience personas, cultural hooks, and brand guidelines without vector embeddings.",
    instruction="""
    You are the Campaign Strategy & Audience Sub-Agent for ITC Limited.
    Your mission:
    1. Inspect if a Campaign Brief exists for the requested ITC brand using `check_or_create_campaign_brief(brand_name, campaign_theme)` or `read_marketing_document`.
    2. If the document exists in `ITC Marketing Files/Campaign Hooks/`, extract its core insights, target segments, and historical benchmarks.
    3. If the document does not exist, synthesize a complete, professional campaign brief aligned with ITC corporate brand guidelines (2026) and save it to `Campaign Hooks/`.
    4. Return the structured campaign brief, audience segmentation, and key value propositions to the orchestrator.
    """,
    tools=[
        list_marketing_folders,
        read_marketing_document,
        save_marketing_document,
        check_or_create_campaign_brief,
        lookup_brand
    ]
)
