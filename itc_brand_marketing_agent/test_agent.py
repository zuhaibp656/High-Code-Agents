"""
Unit & Integration Test Suite for ITC Brand Marketing Agent.
Validates ADK multi-agent structure, IAB specifications, document reading without embeddings,
dynamic brief/hook auto-creation, GenMedia tools, and end-to-end campaign builder.
"""

import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from agent.agent import root_agent
from agent.sub_agents.campaign_hook_agent import campaign_hook_agent
from agent.sub_agents.creative_hook_agent import creative_hook_agent
from agent.sub_agents.media_plan_agent import media_plan_agent
from agent.sub_agents.genmedia_iab_agent import genmedia_iab_agent

from agent.tools.doc_reader_engine import (
    list_marketing_folders,
    read_marketing_document,
    save_marketing_document,
    read_iab_guidelines
)
from agent.tools.brand_knowledge_engine import (
    ITC_BRANDS,
    lookup_brand,
    get_all_itc_brands,
    check_or_create_campaign_brief,
    check_or_create_creative_hooks,
    check_or_create_media_plan
)
from agent.tools.iab_specs_engine import (
    IAB_AD_PORTFOLIO,
    lookup_iab_spec,
    get_all_iab_specs,
    validate_asset_against_iab_lean,
    get_iab_sizing_menu_matrix
)
from agent.tools.genmedia_engine import (
    generate_marketing_image,
    generate_marketing_video,
    edit_marketing_video,
    resize_image_to_iab_format,
    replicate_master_to_all_iab_formats,
    synthesize_creative_sub_prompts
)
from agent.tools.campaign_engine import (
    build_full_itc_campaign
)


def test_doc_reader_and_file_structure():
    """Verifies that marketing documents can be listed and read directly without embeddings."""
    folders = list_marketing_folders()
    assert "itc_marketing_files" in folders
    assert "iab_formats" in folders

    # Test reading Brand Guidelines markdown
    bg_text = read_marketing_document("Brand Guidelines", "itc_limited_brand_guidelines_2026.md")
    assert "ITC Limited" in bg_text
    assert "062F62" in bg_text  # American Blue brand color

    # Test reading Audience Excel
    aud_text = read_marketing_document("Audience", "itc_customer_segments_demo.xlsx")
    assert "Sunfeast Dark Fantasy" in aud_text or "Packaged Foods" in aud_text

    # Test reading Historical Analytics CSV
    csv_text = read_marketing_document("Historical campaign and channel performance", "itc_campaign_analytics_demo.csv")
    assert "Campaign_ID" in csv_text


def test_itc_knowledge_and_brand_profiles():
    """Verifies all ITC brands are present and have valid profiles."""
    brands = get_all_itc_brands()
    assert len(brands) >= 10
    assert "Sunfeast Dark Fantasy" in brands
    assert "Aashirvaad" in brands
    assert "Bingo!" in brands
    assert "Fiama" in brands
    assert "Savlon" in brands

    # Test lookup
    df = lookup_brand("dark_fantasy")
    assert df["brand_name"] == "Sunfeast Dark Fantasy"
    assert len(df["key_products"]) >= 3
    assert len(df["color_palette"]) >= 3


def test_dynamic_document_check_or_create():
    """Verifies auto-checking and synthesis of campaign briefs, creative hooks, and media plans."""
    # Test Campaign Brief for Dark Fantasy
    brief = check_or_create_campaign_brief("Sunfeast Dark Fantasy", "festive_diwali")
    assert "Sunfeast Dark Fantasy" in brief
    assert "Executive Summary" in brief

    # Test Creative Hooks for Bingo
    hooks = check_or_create_creative_hooks("Bingo!", "cricket_ipl", "Explosive crunch during IPL match")
    assert "Bingo!" in hooks
    assert "Pattern Interrupt Hook" in hooks
    assert "THE HERO" in hooks

    # Test Media Plan for Aashirvaad
    plan = check_or_create_media_plan("Aashirvaad", 50.0)
    assert "Aashirvaad" in plan
    assert "YouTube & Connected TV" in plan


def test_iab_spec_engine_and_13_constraints():
    """Verifies all 17 IAB specifications including the 13 standard banner constraints."""
    specs = get_all_iab_specs()
    assert len(specs) >= 17

    matrix = get_iab_sizing_menu_matrix()
    all_13 = matrix["categories"]["all_13_iab_banners"]
    assert len(all_13) == 13

    # Check Key Formats
    for dim in ["728x90", "468x60", "88x31", "120x60", "120x90", "120x240", "336x280", "125x125", "120x600", "180x150", "234x60", "250x250", "300x250"]:
        spec = lookup_iab_spec(dim)
        assert spec["fixed_size_px"] == dim
        assert spec["max_initial_k_weight_kb"] > 0


def test_sub_prompt_synthesis():
    """Tests 4-part sub-prompt decomposition (Hero, Background, Headline, CTA)."""
    sub = synthesize_creative_sub_prompts(
        brand_name="Sunfeast Dark Fantasy",
        core_prompt="Midnight molten chocolate indulgence while reading late night"
    )
    assert "hero_focal_point" in sub["sub_prompts"]
    assert "background_environment" in sub["sub_prompts"]
    assert "headline_copy" in sub["sub_prompts"]
    assert "cta_interaction" in sub["sub_prompts"]
    assert "Sunfeast Dark Fantasy" in sub["sub_prompts"]["hero_focal_point"]


def test_genmedia_image_and_video():
    """Tests GenMedia image generation, Veo video ads, and PIL resizing."""
    img_res = generate_marketing_image(
        prompt="A luxury bottle of Fiama body wash with micro-bubbles in a spa",
        output_filename="test_fiama_300x250.png",
        brand_name="Fiama",
        iab_unit_name="300x250"
    )
    assert img_res["status"] == "SUCCESS"
    assert img_res["dimension"] == "300x250"
    assert os.path.exists(img_res["output_path"])

    # Test Image Resizing to 728x90
    resize_res = resize_image_to_iab_format(
        image_filename="test_fiama_300x250.png",
        width=728,
        height=90,
        output_filename="test_fiama_728x90.png"
    )
    assert resize_res["status"] == "SUCCESS"
    assert resize_res["dimension"] == "728x90"
    assert os.path.exists(resize_res["output_path"])

    # Test Video Generation
    vid_res = generate_marketing_video(
        prompt="High energy reel with explosive crunch",
        output_filename="test_bingo_video.mp4",
        brand_name="Bingo!",
        format_type="portrait_9_16",
        duration_seconds=10
    )
    assert vid_res["status"] == "SUCCESS"
    assert vid_res["aspect_ratio"] == "9:16"
    assert len(vid_res["storyboard"]) == 3


def test_batch_replication_across_all_13_iab_sizes():
    """Tests replicating a master creative across all 13 standard IAB banner constraints."""
    batch_res = replicate_master_to_all_iab_formats(
        brand_name="Sunfeast Dark Fantasy",
        core_prompt="Molten dark chocolate cookie break in evening setting",
        preset="all_13"
    )
    assert batch_res["status"] == "BATCH_REPLICATION_SUCCESS"
    assert batch_res["total_formats_generated"] == 13
    assert len(batch_res["formats"]) == 13

    for f in batch_res["formats"]:
        assert "dimension" in f
        assert f["compliance_status"] == "COMPLIANT"
        assert os.path.exists(f["output_path"])


def test_campaign_planner_end_to_end():
    """Tests the full multi-channel campaign generation pipeline."""
    plan = build_full_itc_campaign(
        brand_name="Aashirvaad",
        campaign_theme="festive_diwali",
        budget_inr_lakhs=40.0
    )
    assert plan["status"] == "CAMPAIGN_SUCCESS"
    assert plan["brand"] == "Aashirvaad"
    assert len(plan["generated_banners"]) == 4
    assert len(plan["generated_videos"]) == 2
    assert len(plan["media_plan"]) == 4
    assert "₹40.00 Lakhs" in plan["total_budget"]
    assert os.path.exists(plan["csv_report_path"])


def test_adk_agent_architecture():
    """Verifies that root_agent and all 4 sub_agents conform to Google ADK specifications."""
    assert "itc_brand_marketing_orchestrator" in root_agent.name
    assert len(root_agent.sub_agents) == 4
    assert len(root_agent.tools) >= 10

    sub_names = [sa.name for sa in root_agent.sub_agents]
    assert "campaign_strategy_subagent" in sub_names
    assert "creative_hook_subagent" in sub_names
    assert "media_planning_subagent" in sub_names
    assert "genmedia_iab_subagent" in sub_names


def test_m365_connector_engine():
    """Verifies Microsoft 365 SharePoint, Teams, and Outlook connector functions."""
    from agent.tools.m365_connector_engine import (
        search_enterprise_sharepoint_knowledge,
        teams_post_campaign_preview,
        outlook_send_campaign_summary,
        check_available_connectors
    )

    # 1. Test Connector Availability Inspection
    conn_status = check_available_connectors()
    assert conn_status["status"] == "SUCCESS"
    assert "connectors" in conn_status
    assert "sharepoint_onedrive_datastore" in conn_status["connectors"]

    # 2. Test SharePoint Search / Fallback
    sp_res = search_enterprise_sharepoint_knowledge("Dark Fantasy indulgence guidelines")
    assert sp_res["query"] == "Dark Fantasy indulgence guidelines"
    assert sp_res["results_count"] >= 1

    # 3. Test Teams Campaign Card Formatting
    teams_res = teams_post_campaign_preview(
        brand_name="Sunfeast Dark Fantasy",
        campaign_theme="festive_indulgence",
        headline="Pure Choco Indulgence",
        banner_download_urls=["https://storage.cloud.google.com/test/banner.png"],
        video_download_url="https://storage.cloud.google.com/test/video.mp4",
        media_plan_csv_url="https://storage.cloud.google.com/test/plan.csv"
    )
    assert teams_res["status"] in ["SIMULATED_SUCCESS", "DELIVERED"]

    # 4. Test Outlook Dispatch Summary
    outlook_res = outlook_send_campaign_summary(
        recipient_email="brandmanager@itc.in",
        brand_name="Sunfeast Dark Fantasy",
        campaign_theme="festive_indulgence",
        summary_text="Omnichannel Diwali Campaign Assets Ready."
    )
    assert outlook_res["status"] == "PREPARED"
    assert outlook_res["recipient"] == "brandmanager@itc.in"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
