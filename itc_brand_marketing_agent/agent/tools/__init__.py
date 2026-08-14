"""
ITC Brand Marketing AI Agent Tools Package.
Exposes clean, typed Python tools for ADK Orchestrator and Sub-Agents.
"""

from .doc_reader_engine import (
    list_marketing_folders,
    read_marketing_document,
    save_marketing_document,
    read_iab_guidelines,
    ITC_MARKETING_DIR,
    IAB_FORMATS_DIR,
    GENERATED_ASSETS_DIR
)

from .brand_knowledge_engine import (
    lookup_brand,
    get_all_itc_brands,
    check_or_create_campaign_brief,
    check_or_create_creative_hooks,
    check_or_create_media_plan,
    ITC_BRANDS
)

from .iab_specs_engine import (
    lookup_iab_spec,
    get_all_iab_specs,
    get_iab_sizing_menu_matrix,
    validate_asset_against_iab_lean,
    IAB_AD_PORTFOLIO
)

from .genmedia_engine import (
    generate_marketing_image,
    generate_marketing_video,
    edit_marketing_video,
    resize_image_to_iab_format,
    replicate_master_to_all_iab_formats,
    synthesize_creative_sub_prompts
)

from .campaign_engine import (
    build_full_itc_campaign
)

__all__ = [
    "list_marketing_folders",
    "read_marketing_document",
    "save_marketing_document",
    "read_iab_guidelines",
    "lookup_brand",
    "get_all_itc_brands",
    "check_or_create_campaign_brief",
    "check_or_create_creative_hooks",
    "check_or_create_media_plan",
    "lookup_iab_spec",
    "get_all_iab_specs",
    "get_iab_sizing_menu_matrix",
    "validate_asset_against_iab_lean",
    "generate_marketing_image",
    "generate_marketing_video",
    "edit_marketing_video",
    "resize_image_to_iab_format",
    "replicate_master_to_all_iab_formats",
    "synthesize_creative_sub_prompts",
    "build_full_itc_campaign",
    "ITC_BRANDS",
    "IAB_AD_PORTFOLIO"
]
