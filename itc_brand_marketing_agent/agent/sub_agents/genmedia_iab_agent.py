"""
GenMedia & IAB Compliance Sub-Agent.
Specializes in generating photorealistic IAB banners (Imagen 3 / Gemini Flash Image),
cinematic video ads (Veo 2 / Veo 3.1), video editing (Gemini Omni), dynamic IAB resizing (ImageOps.fit),
and batch replication across all 13 standard IAB formats.
"""

from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

vertex_flash_model = Gemini(model_name="gemini-2.5-flash", client_kwargs={"vertexai": True})

from ..tools.doc_reader_engine import (
    read_iab_guidelines
)
from ..tools.iab_specs_engine import (
    lookup_iab_spec,
    get_all_iab_specs,
    validate_asset_against_iab_lean
)
from ..tools.genmedia_engine import (
    generate_marketing_image,
    generate_marketing_video,
    edit_marketing_video,
    resize_image_to_iab_format,
    replicate_master_to_all_iab_formats
)

genmedia_iab_agent = Agent(
    name="genmedia_iab_subagent",
    model=vertex_flash_model,
    description="Specializes in generating photorealistic IAB banners, cinematic video ads, video editing, dynamic IAB resizing, and multi-format batch replication across all 13 standard IAB banner constraints.",
    instruction="""
    You are the GenMedia & IAB Compliance Sub-Agent for ITC Brand Marketing.
    Your mission:
    1. For Image Generation: Call `generate_marketing_image(prompt, output_filename, reference_image_path, brand_name, iab_unit_name)`.
    2. For Video Generation: Call `generate_marketing_video(prompt, output_filename, brand_name, format_type, duration_seconds)`.
    3. For Video Editing: Call `edit_marketing_video(video_filename, edit_prompt, output_filename)`.
    4. For Dynamic IAB Resizing: Call `resize_image_to_iab_format(image_filename, width, height, output_filename)`.
    5. For Batch Multi-Size Replication: Call `replicate_master_to_all_iab_formats(brand_name, core_prompt, preset)`.
    6. For IAB LEAN Verification: Verify file weights, aspect ratios, and 1px solid border requirements using `read_iab_guidelines()` and `lookup_iab_spec()`.
    7. Always provide the local file path, GCS URL, and markdown visual preview syntax using the public HTTPS download URL: `![Asset Title](download_url)`.
    """,
    tools=[
        generate_marketing_image,
        generate_marketing_video,
        edit_marketing_video,
        resize_image_to_iab_format,
        replicate_master_to_all_iab_formats,
        read_iab_guidelines,
        lookup_iab_spec
    ]
)
