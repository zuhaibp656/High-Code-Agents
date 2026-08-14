"""
Creative Director & Sub-Prompt Sub-Agent.
Specializes in generating 4-part sub-prompt decomposition (Hero, Background, Headline, CTA),
audio hooks, visual scroll-stoppers, and ad copy scripts.
"""

from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

vertex_flash_model = Gemini(model_name="gemini-2.5-flash", client_kwargs={"vertexai": True})

from ..tools.doc_reader_engine import (
    read_marketing_document,
    save_marketing_document
)
from ..tools.brand_knowledge_engine import (
    check_or_create_creative_hooks,
    lookup_brand
)
from ..tools.genmedia_engine import (
    synthesize_creative_sub_prompts
)

creative_hook_agent = Agent(
    name="creative_hook_subagent",
    model=vertex_flash_model,
    description="Specializes in checking, extracting, and synthesizing creative hooks, audio scripts, and 4-Part Sub-Prompt Decomposition (Hero, Background, Headline, CTA) for ITC brands.",
    instruction="""
    You are the Creative Director & Sub-Prompt Sub-Agent for ITC Brand Marketing.
    Your mission:
    1. Check if creative scripts or hooks exist in `ITC Marketing Files/Creative Hooks/` using `check_or_create_creative_hooks(brand_name, campaign_theme, core_idea)` or `read_marketing_document`.
    2. Deconstruct any campaign 'Big Idea' or prompt into 4 distinct, high-fidelity sub-prompts using `synthesize_creative_sub_prompts(brand_name, core_prompt)`:
       - **THE HERO (Focal Point)**: Product description, textures, studio lighting, materials, packaging.
       - **BACKGROUND (Environment)**: Atmospheric setting, mood, ambient depth of field.
       - **HEADLINE / COPY**: Punchy advertising tagline.
       - **CTA / INTERACTION**: Sharp conversion trigger.
    3. Generate 4 distinct hook angles: Pattern Interrupt (0.5s visual hook), Emotional/Cultural Connection, Sensory/Product USP, and Quick-Commerce Conversion.
    4. Save the generated hooks to `Creative Hooks/` if not previously present.
    """,
    tools=[
        read_marketing_document,
        save_marketing_document,
        check_or_create_creative_hooks,
        synthesize_creative_sub_prompts,
        lookup_brand
    ]
)
