"""
Comprehensive Campaign Planner for ITC Brand Marketing.
Synthesizes Campaign Hooks, Creative Angles, Target Audiences, Media Plans,
IAB specifications, and executes Imagen 3 & Veo 2 asset generation into an end-to-end plan.
"""

import os
import json
import time
from typing import Dict, List, Any, Optional

from tools.itc_knowledge_engine import lookup_brand, generate_brand_hooks_data
from tools.iab_specs_engine import lookup_iab_spec, IAB_AD_PORTFOLIO
from tools.imagen_veo_engine import generate_imagen_banner, generate_veo_video_ad


def build_full_itc_campaign(
    brand_name: str,
    campaign_objective: str = "Brand Awareness & Festive Sales",
    campaign_theme: str = "festive_diwali",
    primary_channels: Optional[List[str]] = None,
    budget_inr_lakhs: float = 50.0
) -> Dict[str, Any]:
    """
    Creates an end-to-end multi-channel marketing campaign for any ITC brand.
    Generates hooks, audience persona strategies, media budget split, IAB banner creatives (Imagen 3),
    and cinematic video storyboards (Veo 2).
    """
    brand_data = lookup_brand(brand_name)
    hooks_data = generate_brand_hooks_data(brand_name, campaign_theme)
    
    if not primary_channels:
        primary_channels = ["Google Display Network (GDN)", "Meta (Instagram/Facebook)", "YouTube & Connected TV", "Quick-Commerce (Blinkit/Zepto)"]
        
    # Standard IAB units to generate
    selected_iab_units = [
        "medium_rectangle",     # 300x250
        "leaderboard",          # 728x90
        "half_page",            # 300x600
        "billboard"             # 970x250
    ]
    
    # 1. Generate Imagen 3 Banners
    generated_banners = []
    for unit_key in selected_iab_units:
        spec = IAB_AD_PORTFOLIO[unit_key]
        creative_prompt = f"Indulgent appetizing visual of {brand_data['brand_name']} {brand_data['key_products'][0]['name']}, showcasing {brand_data['sensory_triggers'][0]} during {hooks_data['campaign_theme']}"
        banner_res = generate_imagen_banner(brand_name=brand_name, prompt=creative_prompt, iab_unit_name=unit_key)
        generated_banners.append(banner_res)
        
    # 2. Generate Veo 2 Video Ads (16:9 In-Stream + 9:16 Reel/Short)
    video_16_9 = generate_veo_video_ad(
        brand_name=brand_name,
        prompt=f"Cinematic {hooks_data['campaign_theme']} commercial featuring {brand_data['brand_name']}",
        format_type="landscape_16_9",
        duration_seconds=6
    )
    
    video_9_16 = generate_veo_video_ad(
        brand_name=brand_name,
        prompt=f"Vertical high-energy reel with {brand_data['sensory_triggers'][0]} and explosive sound hook",
        format_type="portrait_9_16",
        duration_seconds=10
    )
    
    # 3. Media Budget Allocation Matrix
    media_plan = [
        {
            "channel": "YouTube & OTT (Hotstar / JioCinema)",
            "format": "16:9 Non-Skip (15s) & Bumper Ads (6s)",
            "veo_asset": video_16_9["filename"],
            "budget_share_pct": "35%",
            "budget_inr": f"₹{budget_inr_lakhs * 0.35:.2f} Lakhs",
            "target_metric": "48% VTR (View-Through Rate)",
            "audience": hooks_data["target_segments"][0]["segment"]
        },
        {
            "channel": "Meta (Instagram Reels & Stories)",
            "format": "9:16 Vertical Video & 1:1 Carousel",
            "veo_asset": video_9_16["filename"],
            "budget_share_pct": "30%",
            "budget_inr": f"₹{budget_inr_lakhs * 0.30:.2f} Lakhs",
            "target_metric": "1.45% CTR (Click-Through Rate)",
            "audience": hooks_data["target_segments"][1]["segment"] if len(hooks_data["target_segments"]) > 1 else hooks_data["target_segments"][0]["segment"]
        },
        {
            "channel": "Google Display Network & Programmatic",
            "format": "IAB Fixed Units (300x250, 728x90, 300x600, 970x250)",
            "imagen_assets": [b["filename"] for b in generated_banners],
            "budget_share_pct": "20%",
            "budget_inr": f"₹{budget_inr_lakhs * 0.20:.2f} Lakhs",
            "target_metric": "0.26% Blended CTR",
            "audience": "Broad Pan-India Contextual & In-Market"
        },
        {
            "channel": "Quick Commerce & Retail Media (Blinkit, Zepto, Swiggy Instamart)",
            "format": "1:1 Product Tiles & 4:1 Category Banners",
            "budget_share_pct": "15%",
            "budget_inr": f"₹{budget_inr_lakhs * 0.15:.2f} Lakhs",
            "target_metric": "4.2x ROAS (Return On Ad Spend)",
            "audience": "High-Intent 10-Minute Grocery Shoppers"
        }
    ]
    
    csv_rows = [
        ["Channel", "Ad Format", "Budget Share (%)", "Budget (INR)", "Target KPI", "Target Segment"],
        *[[m["channel"], m["format"], m["budget_share_pct"], m["budget_inr"], m["target_metric"], m["audience"]] for m in media_plan]
    ]
    csv_content = "\n".join([",".join([f'"{c}"' for c in row]) for row in csv_rows])
    
    timestamp = int(time.time())
    sanitized_brand = brand_name.lower().replace(" ", "_")
    csv_filename = f"{sanitized_brand}_media_plan_{timestamp}.csv"
    
    from tools.imagen_veo_engine import ASSETS_DIR, upload_asset_to_gcs, GCS_BUCKET_NAME
    reports_dir = os.path.join(ASSETS_DIR, "reports")
    os.makedirs(reports_dir, exist_ok=True)
    csv_filepath = os.path.join(reports_dir, csv_filename)
    
    with open(csv_filepath, "w", encoding="utf-8") as f:
        f.write(csv_content)
        
    gcs_csv_url = upload_asset_to_gcs(csv_filepath, "reports")
    clean_csv_link = gcs_csv_url if gcs_csv_url else f"https://console.cloud.google.com/storage/browser/{GCS_BUCKET_NAME}/reports?project=zuhaibp-ai"

    return {
        "status": "CAMPAIGN_GENERATED",
        "brand": brand_data["brand_name"],
        "category": brand_data["category"],
        "campaign_objective": campaign_objective,
        "campaign_theme": hooks_data["campaign_theme"],
        "total_budget": f"₹{budget_inr_lakhs:.2f} Lakhs",
        "brand_pillars": brand_data["brand_pillars"],
        "taglines": brand_data["taglines"],
        "color_palette": brand_data["color_palette"],
        "campaign_hooks": hooks_data["seasonal_hooks"],
        "target_segments": hooks_data["target_segments"],
        "historical_benchmarks": brand_data["historical_benchmarks"],
        "generated_banners_imagen": generated_banners,
        "generated_videos_veo": [video_16_9, video_9_16],
        "media_plan": media_plan,
        "download_csv_url": clean_csv_link
    }


from google.adk.tools.tool_context import ToolContext
from google.genai import types

async def execute_campaign_planner_tool(
    brand_name: str,
    campaign_objective: str = "Festive Brand Awareness & Immediate Q-Commerce Conversion",
    campaign_theme: str = "festive_diwali",
    budget_inr_lakhs: float = 50.0,
    tool_context: Optional[ToolContext] = None
) -> str:
    """
    Main tool to plan, generate, and assemble an end-to-end IAB-compliant marketing campaign for ITC brands, and save CSV media plan to runtime artifact storage.
    """
    plan = build_full_itc_campaign(
        brand_name=brand_name,
        campaign_objective=campaign_objective,
        campaign_theme=campaign_theme,
        budget_inr_lakhs=budget_inr_lakhs
    )
    
    if tool_context:
        try:
            csv_rows = [
                ["Channel", "Ad Format", "Budget Share (%)", "Budget (INR)", "Target KPI", "Target Segment"],
                *[[m["channel"], m["format"], m["budget_share_pct"], m["budget_inr"], m["target_metric"], m["audience"]] for m in plan.get("media_plan", [])]
            ]
            csv_content = "\n".join([",".join([f'"{c}"' for c in row]) for row in csv_rows])
            sanitized_brand = brand_name.lower().replace(" ", "_")
            csv_filename = f"{sanitized_brand}_media_plan.csv"
            part = types.Part.from_bytes(data=csv_content.encode("utf-8"), mime_type="text/csv")
            version = await tool_context.save_artifact(filename=csv_filename, artifact=part)
            plan["csv_artifact_saved"] = True
            plan["csv_artifact_version"] = version
            plan["runtime_artifact_filename"] = csv_filename
        except Exception as e:
            plan["csv_artifact_notice"] = str(e)
            
    return json.dumps(plan, indent=2)
