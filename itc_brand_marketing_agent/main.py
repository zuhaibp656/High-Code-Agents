"""
ITC Brand Marketing AI Agent - Interactive CLI & Runtime Host.
Built with Google ADK for direct hosting in Gemini Enterprise.
Generates IAB-approved display banners (Imagen 3 / Gemini Flash Image) and cinematic video ads (Veo)
using campaign hooks, creative hooks, audience segmentation, and media plans for ITC brands.
Features 4-part sub-prompt decomposition, dynamic IAB resizing, and 13+ standard banner replication.
"""

import asyncio
import json
import os
import sys
import uuid
from typing import Optional, List

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

# Ensure local directories are in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
agent_dir = os.path.join(current_dir, "agent")
if agent_dir not in sys.path:
    sys.path.insert(0, agent_dir)

from agent.agent import root_agent
from agent.tools.brand_knowledge_engine import (
    ITC_BRANDS,
    get_all_itc_brands,
    lookup_brand,
    check_or_create_campaign_brief,
    check_or_create_creative_hooks,
    check_or_create_media_plan
)
from agent.tools.iab_specs_engine import (
    IAB_AD_PORTFOLIO,
    get_all_iab_specs,
    get_iab_sizing_menu_matrix,
    lookup_iab_spec
)
from agent.tools.campaign_engine import build_full_itc_campaign
from agent.tools.genmedia_engine import (
    generate_marketing_image,
    generate_marketing_video,
    replicate_master_to_all_iab_formats,
    synthesize_creative_sub_prompts,
    resize_image_to_iab_format
)
from agent.tools.doc_reader_engine import (
    list_marketing_folders,
    read_marketing_document,
    read_iab_guidelines
)

console = Console()


def display_brand_browser():
    """Renders a rich table of all supported ITC brands."""
    table = Table(
        title="🌟 ITC Limited Brand Portfolio & Creative Profiles",
        header_style="bold magenta",
        show_lines=True
    )
    table.add_column("Brand", style="bold cyan", no_wrap=True)
    table.add_column("Category", style="yellow")
    table.add_column("Key Products", style="white")
    table.add_column("Signature Tagline", style="green")
    table.add_column("Sensory Visual Aesthetic", style="dim")

    for key, b in ITC_BRANDS.items():
        prods = ", ".join([p["name"] for p in b["key_products"][:2]])
        table.add_row(
            b["brand_name"],
            b["category"],
            prods,
            b["taglines"][0],
            b["visual_aesthetic"][:65] + "..."
        )
    console.print(table)


def display_iab_specs_browser():
    """Renders the official IAB New Ad Portfolio specifications."""
    table = Table(
        title="📐 IAB New Ad Portfolio & LEAN Standard Specifications (17 Formats)",
        header_style="bold cyan",
        show_lines=True
    )
    table.add_column("Ad Unit Name", style="bold white")
    table.add_column("Category", style="magenta")
    table.add_column("Fixed Size (px)", style="bold green")
    table.add_column("Aspect Ratio", style="yellow")
    table.add_column("Initial Load Max", style="cyan")
    table.add_column("Subload Max", style="blue")
    table.add_column("Tier", style="red")

    for key, spec in IAB_AD_PORTFOLIO.items():
        table.add_row(
            spec["unit_name"],
            spec["category"],
            spec["fixed_size_px"],
            spec["aspect_ratio"],
            f"{spec['max_initial_k_weight_kb']} kB",
            f"{spec['max_subload_k_weight_kb']} kB" if spec['max_subload_k_weight_kb'] > 0 else "N/A",
            spec.get("tier", "Standard")
        )
    console.print(table)


def render_all_iab_cards(batch_result: dict):
    """Renders the interactive IAB format grid matching the Content Nebula UI."""
    brand = batch_result.get("brand", "ITC Brand")
    total = batch_result.get("total_formats_generated", 0)
    subs = batch_result.get("sub_prompts", {})

    console.print(Panel(
        f"[bold cyan]⚡ Generated Master Creative & Replicated Across {total} IAB Ad Formats[/bold cyan]\n"
        f"[bold white]Brand:[/bold white] {brand}\n"
        f"[dim]Decomposed into 4 Sub-Prompts: Hero • Background • Headline • CTA[/dim]",
        border_style="magenta"
    ))

    # Sub-Prompts Preview
    sub_table = Table(title="🧩 Concept Orchestration & Sub-Prompts Decomposition", header_style="bold yellow", show_lines=True)
    sub_table.add_column("Component", style="bold cyan", width=22)
    sub_table.add_column("Synthesized Prompt & Direction", style="white")
    sub_table.add_row("🎯 THE HERO (Focal Point)", subs.get("hero_focal_point", ""))
    sub_table.add_row("🌄 BACKGROUND (Environment)", subs.get("background_environment", ""))
    sub_table.add_row("✍️ HEADLINE / COPY", subs.get("headline_copy", ""))
    sub_table.add_row("🚀 CTA / INTERACTION", subs.get("cta_interaction", ""))
    console.print(sub_table)

    # IAB Formats Grid Table with Interactive Action Buttons
    grid_table = Table(title="📐 Generated IAB Ad Formats & Action Cards", header_style="bold green", show_lines=True)
    grid_table.add_column("Dimension (px)", style="bold yellow", no_wrap=True)
    grid_table.add_column("IAB Ad Unit Name", style="bold white")
    grid_table.add_column("Aspect Ratio", style="cyan")
    grid_table.add_column("File Size (kB)", style="magenta")
    grid_table.add_column("LEAN Compliance", style="green")
    grid_table.add_column("Asset Link", style="dim")
    grid_table.add_column("Interactive Actions", style="bold blue")

    for f in batch_result.get("formats", []):
        grid_table.add_row(
            f["dimension"],
            f["unit_name"],
            f["aspect_ratio"],
            f"{f['file_size_kb']} kB",
            f"✅ {f['compliance_status']}",
            f"{f['filename']}",
            "[bold cyan][💫 Custom Gen][/bold cyan]  [bold yellow][💾 Download][/bold yellow]  [bold magenta][🔄 Resize][/bold magenta]"
        )
    console.print(grid_table)


async def batch_generate_all_iab_formats():
    """Batch generates all 13 standard IAB formats matching the screenshot."""
    console.print("\n[bold cyan]⚡ Batch Generate All IAB Banner Constraints (Content Nebula Mode):[/bold cyan]")
    brand_input = Prompt.ask("Enter ITC Brand (e.g. 'Dark Fantasy', 'Bingo', 'Aashirvaad', 'Fiama', 'Fabelle')", default="Dark Fantasy")
    core_prompt = Prompt.ask("Enter Core Prompt / 'The Big Idea'", default="Molten chocolate cookie breaking open with rich liquid core in an amber glow evening setting")

    console.print("\n[bold yellow]Select IAB Preset Group:[/bold yellow]")
    console.print("  [1] [bold white]⚡ All 13 Standard IAB Banner Constraints[/bold white] (728x90, 468x60, 88x31, 120x60, 120x90, 120x240, 336x280, 125x125, 120x600, 180x150, 234x60, 250x250, 300x250)")
    console.print("  [2] [bold white]🎯 Top Performers Package[/bold white] (300x250, 728x90, 300x600, 970x250)")
    console.print("  [3] [bold white]🎬 Video & Social Formats[/bold white] (16:9 In-stream, 9:16 Reels/Shorts, 1:1 Feed)")

    preset_choice = Prompt.ask("\nEnter choice", choices=["1", "2", "3"], default="1")
    preset_map = {"1": "all_13", "2": "top_performers", "3": "video_formats"}

    console.print(f"\n[cyan]Synthesizing sub-prompts and generating all IAB constraints for [bold]{brand_input}[/bold]...[/cyan]\n")
    batch_res = replicate_master_to_all_iab_formats(brand_name=brand_input, core_prompt=core_prompt, preset=preset_map[preset_choice])
    render_all_iab_cards(batch_res)


async def interactive_size_resizer():
    """Provides interactive size selection and dynamic asset resizing."""
    console.print("\n[bold cyan]🔄 Interactive IAB Size Selector & Resizing Tool:[/bold cyan]")
    brand_input = Prompt.ask("Enter ITC Brand", default="Dark Fantasy")
    core_prompt = Prompt.ask("Enter Creative Concept / Big Idea", default="Molten dark chocolate cookie with gold dust sparkles")

    console.print("\n[bold yellow]Select Target IAB Size to Generate / Resize:[/bold yellow]")
    specs = get_all_iab_specs()
    for idx, s in enumerate(specs, 1):
        console.print(f"  [{idx:2d}] [bold white]{s['fixed_size_px']:10s}[/bold white] — {s['unit_name']} ({s['category']})")

    size_choice = Prompt.ask("\nEnter option number (1-17)", default="1")
    try:
        s_idx = int(size_choice) - 1
        target_spec = specs[s_idx] if 0 <= s_idx < len(specs) else specs[0]
    except ValueError:
        target_spec = specs[0]

    console.print(f"\n[cyan]Generating & Adapting creative to [bold]{target_spec['fixed_size_px']}[/bold] ({target_spec['unit_name']})...[/cyan]")
    res = generate_marketing_image(
        prompt=core_prompt,
        output_filename=f"interactive_{target_spec['fixed_size_px']}.png",
        brand_name=brand_input,
        iab_unit_name=target_spec["fixed_size_px"]
    )

    console.print(Panel(
        f"[bold green]Asset Generated & Adapted Successfully![/bold green]\n"
        f"• Brand: {res['brand']}\n"
        f"• Dimension: {res['dimension']} ({res['aspect_ratio']})\n"
        f"• Initial File Weight: {res['file_size_kb']} kB (Max Allowed: {res['iab_compliance']['max_allowed_kb']} kB)\n"
        f"• IAB LEAN Status: ✅ {res['iab_compliance']['status']}\n"
        f"• File Path: {res['output_path']}\n"
        f"• GCS URI: {res['gcs_uri']}\n\n"
        f"[bold cyan]Interactive Action Options:[/bold cyan]\n"
        f"  [1] [bold white]💫 Custom Gen (Refine Prompt)[/bold white]\n"
        f"  [2] [bold white]💾 Download PNG Asset[/bold white]\n"
        f"  [3] [bold white]🔄 Adapt to Another IAB Size[/bold white]\n"
        f"  [4] [bold white]⚡ Replicate to All 13 IAB Sizes[/bold white]",
        title=f"IAB Card: {target_spec['fixed_size_px']} {target_spec['unit_name']}",
        border_style="green"
    ))


async def quick_campaign_builder():
    """Guides user through interactive campaign creation."""
    console.print("\n[bold cyan]Select an ITC Brand:[/bold cyan]")
    brands = get_all_itc_brands()
    for idx, b in enumerate(brands, 1):
        console.print(f"  [{idx:2d}] {b}")

    brand_choice = Prompt.ask("\nEnter brand number or name", default="1")
    try:
        b_idx = int(brand_choice) - 1
        brand_name = brands[b_idx] if 0 <= b_idx < len(brands) else brands[0]
    except ValueError:
        brand_name = brand_choice

    theme = Prompt.ask("Enter Campaign Theme (e.g. 'festive_diwali', 'cricket_ipl', 'monsoon_rainy', 'summer_heat')", default="festive_diwali")
    budget = float(Prompt.ask("Enter Total Budget in INR Lakhs (e.g. 50.0)", default="50.0"))

    console.print(f"\n[cyan]Building complete multi-channel campaign for [bold]{brand_name}[/bold]...[/cyan]\n")
    plan = build_full_itc_campaign(
        brand_name=brand_name,
        campaign_theme=theme,
        budget_inr_lakhs=budget
    )

    console.print(Panel(
        f"[bold green]✨ Campaign Successfully Generated![/bold green]\n"
        f"• Brand: {plan['brand']} ({plan['category']})\n"
        f"• Theme: {plan['theme']}\n"
        f"• Total Budget: {plan['total_budget']}\n"
        f"• CSV Report Exported: {plan['csv_report_path']}\n"
        f"• Download Link: {plan['csv_download_url']}",
        title="Campaign Summary",
        border_style="green"
    ))

    # Render Sub-Prompts
    sub_table = Table(title="🧩 4-Part Sub-Prompts", header_style="bold yellow", show_lines=True)
    sub_table.add_column("Component", style="bold cyan")
    sub_table.add_column("Direction", style="white")
    for k, v in plan["sub_prompts"].items():
        sub_table.add_row(k.replace('_', ' ').title(), v)
    console.print(sub_table)

    # Render Media Plan Table
    plan_table = Table(title="📊 Multi-Channel Media Plan & Budget Allocation", header_style="bold magenta", show_lines=True)
    plan_table.add_column("Channel", style="bold white")
    plan_table.add_column("Ad Format", style="yellow")
    plan_table.add_column("Share (%)", style="cyan")
    plan_table.add_column("Spend (INR)", style="green")
    plan_table.add_column("Target KPI", style="magenta")
    plan_table.add_column("Audience Segment", style="dim")

    for row in plan["media_plan"]:
        plan_table.add_row(
            row["channel"],
            row["format"],
            row["budget_share"],
            row["budget_inr"],
            row["target_kpi"],
            row["audience"]
        )
    console.print(plan_table)


async def main_cli():
    """Main Interactive CLI Loop."""
    console.print(Panel(
        "[bold cyan]🌟 ITC Brand Marketing AI Agent — CLI & Runtime Host[/bold cyan]\n"
        "[white]Powered by Google ADK • Gemini Enterprise • Google Imagen 3 • Google Veo (Region: us-central1)[/white]\n"
        "[dim]Direct document inspection & generation without vector embeddings • High-speed IAB resizing & GCS storage[/dim]",
        border_style="cyan"
    ))

    while True:
        console.print("\n[bold yellow]Main Menu:[/bold yellow]")
        console.print("  [1] [bold white]🚀 Build Full Multi-Channel Campaign[/bold white] (Brief + Hooks + Banners + Video + Media Plan)")
        console.print("  [2] [bold white]⚡ Batch Replicate to All 13 IAB Banner Constraints[/bold white] (Content Nebula Sizing Grid)")
        console.print("  [3] [bold white]🔄 Interactive IAB Size Selector & Resizer[/bold white]")
        console.print("  [4] [bold white]🌟 Browse ITC Brands Portfolio (11 Brands)[/bold white]")
        console.print("  [5] [bold white]📐 Browse IAB New Ad Portfolio & LEAN Specs (17 Formats)[/bold white]")
        console.print("  [6] [bold white]📁 Browse ITC Marketing Documents & Folders[/bold white]")
        console.print("  [0] [bold red]Exit[/bold red]")

        choice = Prompt.ask("\nEnter option", default="1")

        if choice == "1":
            await quick_campaign_builder()
        elif choice == "2":
            await batch_generate_all_iab_formats()
        elif choice == "3":
            await interactive_size_resizer()
        elif choice == "4":
            display_brand_browser()
        elif choice == "5":
            display_iab_specs_browser()
        elif choice == "6":
            folders = list_marketing_folders()
            console.print(json.dumps(folders, indent=2))
        elif choice == "0":
            console.print("[bold green]Goodbye![/bold green]")
            break
        else:
            console.print("[red]Invalid selection. Try again.[/red]")


if __name__ == "__main__":
    asyncio.run(main_cli())
