"""
Campaign Orchestration & End-to-End Execution Engine for ITC Brand Marketing.
Synthesizes Campaign Briefs, Creative Hooks, Media Plans, IAB Display Banners, and Veo Video Ads.
"""

import os
import json
import time
from typing import Dict, List, Any, Optional

from .doc_reader_engine import GENERATED_ASSETS_DIR
from .brand_knowledge_engine import (
    lookup_brand,
    check_or_create_campaign_brief,
    check_or_create_creative_hooks,
    check_or_create_media_plan
)
from .iab_specs_engine import lookup_iab_spec, IAB_AD_PORTFOLIO
from .genmedia_engine import (
    generate_marketing_image,
    generate_marketing_video,
    synthesize_creative_sub_prompts,
    _upload_to_gcs,
    GCS_BUCKET_NAME
)

REPORTS_DIR = os.path.join(GENERATED_ASSETS_DIR, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)


def build_full_itc_campaign(
    brand_name: str,
    campaign_objective: str = "Festive Brand Awareness & Immediate Q-Commerce Conversion",
    campaign_theme: str = "festive_diwali",
    budget_inr_lakhs: float = 50.0
) -> Dict[str, Any]:
    """
    Builds a complete end-to-end multi-channel marketing campaign for any ITC brand:
    1. Checks/Synthesizes Campaign Brief
    2. Checks/Synthesizes Creative Hooks & 4-Part Sub-Prompts
    3. Generates Top-Performing IAB Display Banners (300x250, 728x90, 300x600, 970x250)
    4. Generates Veo 16:9 In-Stream & 9:16 Vertical Video Ads
    5. Formulates Multi-Channel Media Budget & Exports CSV Spreadsheet
    """
    brand_data = lookup_brand(brand_name)
    sanitized_brand = brand_name.lower().replace(" ", "_")
    timestamp = int(time.time())

    # 1. Document Extraction / Creation
    brief_content = check_or_create_campaign_brief(brand_name, campaign_theme)
    hooks_content = check_or_create_creative_hooks(brand_name, campaign_theme)
    media_plan_content = check_or_create_media_plan(brand_name, budget_inr_lakhs)

    # 2. Deconstruct Sub-Prompts
    sub_prompts_obj = synthesize_creative_sub_prompts(
        brand_name=brand_name,
        core_prompt=f"Sensory celebration of {brand_data['brand_name']} during {campaign_theme.replace('_', ' ').title()}"
    )

    # 3. Generate Top-Performing IAB Banners efficiently
    top_units = ["medium_rectangle", "leaderboard", "half_page", "billboard"]
    generated_banners = []
    
    # Generate master banner
    master_spec = IAB_AD_PORTFOLIO["medium_rectangle"]
    master_fn = f"{sanitized_brand}_300x250_{timestamp}.png"
    master_prompt = f"Commercial ad visual of {brand_data['brand_name']} {brand_data['key_products'][0]['name']}, showcasing {brand_data['sensory_triggers'][0]}."
    master_res = generate_marketing_image(
        prompt=master_prompt,
        output_filename=master_fn,
        brand_name=brand_name,
        iab_unit_name="medium_rectangle"
    )
    generated_banners.append(master_res)
    master_path = master_res["output_path"]

    from PIL import Image, ImageOps
    from .doc_reader_engine import GENERATED_ASSETS_DIR
    images_dir = os.path.join(GENERATED_ASSETS_DIR, "images")

    for unit_key in ["leaderboard", "half_page", "billboard"]:
        spec = IAB_AD_PORTFOLIO[unit_key]
        fn = f"{sanitized_brand}_{spec['fixed_size_px']}_{timestamp}.png"
        out_path = os.path.join(images_dir, fn)
        if os.path.exists(master_path):
            with Image.open(master_path) as img:
                resized = ImageOps.fit(img, (spec["width"], spec["height"]), Image.Resampling.LANCZOS)
                resized.save(out_path, format="PNG")
        else:
            from .genmedia_engine import render_fallback_png_banner
            render_fallback_png_banner(brand_data, spec, master_prompt, out_path)

        file_size_kb = os.path.getsize(out_path) / 1024.0 if os.path.exists(out_path) else 45.0
        gcs_uri, console_url = _upload_to_gcs(out_path, f"images/{fn}")
        generated_banners.append({
            "status": "SUCCESS",
            "brand": brand_data["brand_name"],
            "dimension": spec["fixed_size_px"],
            "aspect_ratio": spec["aspect_ratio"],
            "output_path": out_path,
            "output_filename": fn,
            "gcs_uri": gcs_uri,
            "download_url": console_url,
            "file_size_kb": round(file_size_kb, 2)
        })

    # 4. Generate Veo Video Ads (16:9 In-Stream + 9:16 Vertical Reel)
    video_16_9_fn = f"{sanitized_brand}_veo_16x9_{timestamp}.mp4"
    video_16_9 = generate_marketing_video(
        prompt=f"Cinematic {campaign_theme.replace('_', ' ')} commercial featuring {brand_data['brand_name']}",
        output_filename=video_16_9_fn,
        brand_name=brand_name,
        format_type="landscape_16_9",
        duration_seconds=6
    )

    video_9_16_fn = f"{sanitized_brand}_veo_9x16_{timestamp}.mp4"
    video_9_16 = generate_marketing_video(
        prompt=f"Vertical high-energy reel showcasing {brand_data['sensory_triggers'][0]} with 0.5s visual hook",
        output_filename=video_9_16_fn,
        brand_name=brand_name,
        format_type="portrait_9_16",
        duration_seconds=10
    )

    # 5. Media Budget Allocation
    b_yt = budget_inr_lakhs * 0.35
    b_meta = budget_inr_lakhs * 0.30
    b_gdn = budget_inr_lakhs * 0.20
    b_qc = budget_inr_lakhs * 0.15

    media_plan_table = [
        {
            "channel": "YouTube & Connected TV",
            "format": "16:9 In-Stream Non-Skip (15s) & Bumper (6s)",
            "asset": video_16_9["output_filename"],
            "budget_share": "35%",
            "budget_inr": f"₹{b_yt:.2f} Lakhs",
            "target_kpi": "48% VTR (View-Through Rate)",
            "audience": brand_data["target_segments"][0]["segment"]
        },
        {
            "channel": "Meta (Instagram Reels & Stories)",
            "format": "9:16 Vertical Video & 1:1 Carousel",
            "asset": video_9_16["output_filename"],
            "budget_share": "30%",
            "budget_inr": f"₹{b_meta:.2f} Lakhs",
            "target_kpi": "1.45% CTR / 2.8x Engagement",
            "audience": brand_data["target_segments"][1]["segment"] if len(brand_data["target_segments"]) > 1 else brand_data["target_segments"][0]["segment"]
        },
        {
            "channel": "Google Display Network & Programmatic",
            "format": "IAB Display Units (300x250, 728x90, 300x600, 970x250)",
            "asset": f"{len(generated_banners)} IAB Display Creatives",
            "budget_share": "20%",
            "budget_inr": f"₹{b_gdn:.2f} Lakhs",
            "target_kpi": "0.26% Blended CTR",
            "audience": "Broad Pan-India Contextual & In-Market"
        },
        {
            "channel": "Quick Commerce (Blinkit, Zepto, Instamart)",
            "format": "1:1 Sponsored Product Tiles & 4:1 Category Banners",
            "asset": "Retail Media Display Units",
            "budget_share": "15%",
            "budget_inr": f"₹{b_qc:.2f} Lakhs",
            "target_kpi": "4.2x ROAS (Return on Ad Spend)",
            "audience": "High-Intent 10-Min Shoppers"
        }
    ]

    # Save CSV Report
    csv_rows = [
        ["Channel", "Ad Format", "Creative Asset", "Budget Share (%)", "Allocated Spend (INR)", "Target KPI", "Audience Segment"],
        *[[m["channel"], m["format"], m["asset"], m["budget_share"], m["budget_inr"], m["target_kpi"], m["audience"]] for m in media_plan_table]
    ]
    csv_content = "\n".join([",".join([f'"{c}"' for c in row]) for row in csv_rows])
    csv_filename = f"{sanitized_brand}_media_plan_{timestamp}.csv"
    csv_filepath = os.path.join(REPORTS_DIR, csv_filename)
    with open(csv_filepath, "w", encoding="utf-8") as f:
        f.write(csv_content)

    gcs_csv_uri, console_csv_url = _upload_to_gcs(csv_filepath, f"reports/{csv_filename}")

    return {
        "status": "CAMPAIGN_SUCCESS",
        "brand": brand_data["brand_name"],
        "category": brand_data["category"],
        "objective": campaign_objective,
        "theme": campaign_theme.replace("_", " ").title(),
        "total_budget": f"₹{budget_inr_lakhs:.2f} Lakhs",
        "sub_prompts": sub_prompts_obj["sub_prompts"],
        "campaign_brief_summary": brief_content[:500] + "...",
        "creative_hooks_summary": hooks_content[:500] + "...",
        "generated_banners": generated_banners,
        "generated_videos": [video_16_9, video_9_16],
        "media_plan": media_plan_table,
        "csv_report_path": csv_filepath,
        "csv_download_url": console_csv_url,
        "gcs_csv_uri": gcs_csv_uri
    }
