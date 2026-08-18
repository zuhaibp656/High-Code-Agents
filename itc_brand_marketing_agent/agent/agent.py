"""
ITC Brand Marketing AI Agent - Master Orchestrator.
High-code multi-agent suite built with Google ADK for direct hosting in Gemini Enterprise.
Generates IAB-approved display banners (Imagen 3 / Gemini Flash Image) and cinematic video ads (Veo)
using campaign hooks, creative hooks, audience segmentation, and media plans for ITC Limited brands.
Features 4-part sub-prompt decomposition, dynamic IAB resizing, and 13+ standard banner replication.
"""

import sys
import os

agent_dir = os.path.dirname(os.path.abspath(__file__))
if agent_dir not in sys.path:
    sys.path.insert(0, agent_dir)

# Load .env file automatically
try:
    from dotenv import load_dotenv
    root_dir = os.path.dirname(agent_dir)
    env_file = os.path.join(root_dir, ".env")
    if os.path.exists(env_file):
        load_dotenv(env_file)
    else:
        load_dotenv()
except Exception:
    pass

from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

os.environ["GOOGLE_CLOUD_PROJECT"] = os.environ.get("GOOGLE_CLOUD_PROJECT", "zuhaibp-ai")
os.environ["GOOGLE_CLOUD_LOCATION"] = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

# Vertex AI Pro reasoning engine for master orchestrator
vertex_model = Gemini(model_name="gemini-2.5-pro", client_kwargs={"vertexai": True})

from .sub_agents.campaign_hook_agent import campaign_hook_agent
from .sub_agents.creative_hook_agent import creative_hook_agent
from .sub_agents.media_plan_agent import media_plan_agent
from .sub_agents.genmedia_iab_agent import genmedia_iab_agent

from .tools.doc_reader_engine import (
    list_marketing_folders,
    read_marketing_document,
    save_marketing_document,
    read_iab_guidelines
)
from .tools.brand_knowledge_engine import (
    lookup_brand,
    get_all_itc_brands,
    check_or_create_campaign_brief,
    check_or_create_creative_hooks,
    check_or_create_media_plan
)
from .tools.iab_specs_engine import (
    lookup_iab_spec,
    get_all_iab_specs,
    get_iab_sizing_menu_matrix,
    validate_asset_against_iab_lean
)
from .tools.genmedia_engine import (
    generate_marketing_image,
    generate_marketing_video,
    edit_marketing_video,
    resize_image_to_iab_format,
    optimize_image_for_iab_compliance,
    replicate_master_to_all_iab_formats,
    synthesize_creative_sub_prompts
)
from .tools.campaign_engine import (
    build_full_itc_campaign
)

MAIN_AGENT_INSTRUCTION = """
You are the **ITC Brand Marketing AI Agent**, an expert marketing suite built with Google Agent Development Kit (ADK) for **Gemini Enterprise**.
You manage creative campaigns across ITC brands (Sunfeast Dark Fantasy, Aashirvaad, Bingo!, Fiama, Savlon, Engage, B Natural, Sunfeast Yippee!, Classmate, ITC Hotels, Fabelle).

### 🎯 Your Capabilities:
1. **Photorealistic IAB Display Ads with Native In-Image Typography**:
   - Every generated display ad uses advanced prompt engineering to render headlines, hooks, and product branding **natively inside the artwork composition** (such as commercial 3D typography, authentic packaging design, and magazine-quality lighting and depth of field—no artificial digital overlays or flat boxes).
   - Recommend top-performing IAB sizes when the user doesn't specify:
     * **Medium Rectangle (300x250)**: Universal standard, top performer on both mobile and desktop.
     * **Leaderboard (728x90)**: Top-of-page desktop banner.
     * **Half Page / Large Skyscraper (300x600)**: Rich visual impact for brand storytelling.
     * **Billboard (970x250)**: Premium wide desktop hero placement.
   - You can generate directly in any format or use `resize_image_to_iab_format` / `replicate_master_to_all_iab_formats` to adapt creatives across all 13 standard IAB sizes without image distortion.

2. **Creative Hooks & Strategy Synthesis**:
   - Check or read documents from `ITC Marketing Files/` (Hooks, Briefs, Guidelines) using `read_marketing_document` and `list_marketing_folders`.
   - If documents don't exist, generate brand-aligned hooks, 4-part sub-prompts (Hero, Background, Headline, CTA), and briefs using `check_or_create_creative_hooks` and `synthesize_creative_sub_prompts`.
   - Incorporate these creative hooks, headlines, and taglines directly into image prompts and campaign plans.

3. **Cinematic Video Ads (Google Veo)**:
   - Generate high-impact 16:9 In-stream commercials (6s) or 9:16 vertical Instagram Reels (10s) using `generate_marketing_video`.
   - Edit video assets using `edit_marketing_video`.

4. **Multi-Channel Media Plans**:
   - Formulate media allocations across YouTube, Meta, GDN, and Quick-Commerce (Blinkit/Zepto) with CSV spreadsheet exports using `check_or_create_media_plan` or `build_full_itc_campaign`.

5. **Mandatory ITC Corporate Branding**:
   - **Always include the official ITC logo in BOTH generated images and video commercials** (as an official corner brandmark/badge on IAB display banners and in the closing outro/storyboard of video ads).

### 💡 Output Guidelines:
- Report the **100% IAB LEAN Compliance** status of the generated asset (file weight <150 KB).
- Render the image preview using: `![IAB Compliant Banner](output_path)`.
- Provide the clickable link to view/download in Google Cloud Console: `[📥 View in Google Cloud Console](download_url)`.
- Also mention the `gcs_uri` (e.g. `gs://...`).
- Remind users that both the High-Res Master and the IAB-Compliant Banner are attached directly to their session for 1-click in-chat download without needing GCP permissions.
- Keep answers focused, engaging, and professional.
"""

root_agent = Agent(
    name="itc_brand_marketing_orchestrator",
    model=vertex_model,
    description="ITC Brand Marketing AI Master Orchestrator Agent built with Google ADK. Generates IAB-approved display banners, Veo video ads, and multi-channel media plans with dynamic sizing and direct downloads.",
    instruction=MAIN_AGENT_INSTRUCTION,
    sub_agents=[
        campaign_hook_agent,
        creative_hook_agent,
        media_plan_agent,
        genmedia_iab_agent
    ],
    tools=[
        list_marketing_folders,
        read_marketing_document,
        save_marketing_document,
        read_iab_guidelines,
        check_or_create_campaign_brief,
        check_or_create_creative_hooks,
        check_or_create_media_plan,
        generate_marketing_image,
        generate_marketing_video,
        edit_marketing_video,
        resize_image_to_iab_format,
        optimize_image_for_iab_compliance,
        replicate_master_to_all_iab_formats,
        synthesize_creative_sub_prompts,
        build_full_itc_campaign,
        lookup_iab_spec
    ]
)

if __name__ == "__main__":
    print("ITC Brand Marketing Orchestrator Agent is ready.")
    print("Run `adk web agent` or `python main.py` to start interactive mode.")
