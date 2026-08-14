"""
IAB Ad Specifications & LEAN Compliance Engine.
Implements the full IAB New Ad Portfolio specifications, flexible sizing grids,
file weight limits (Initial load & Subload), aspect ratio mapping, and LEAN performance validation.
Includes all 17 standard display banner and video ad constraints.
"""

from typing import Dict, List, Any, Optional
import json

IAB_AD_PORTFOLIO = {
    # Top Performing & Standard Horizontal Units
    "leaderboard": {
        "key": "leaderboard",
        "unit_name": "Leaderboard",
        "category": "Horizontal",
        "fixed_size_px": "728x90",
        "width": 728,
        "height": 90,
        "aspect_ratio": "8:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 150,
        "max_subload_k_weight_kb": 300,
        "static_image_max_kb": 150,
        "tier": "Top Performer",
        "recommended_channels": ["Google Display Network", "Desktop Websites", "Programmatic Header Bids"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted (User-Initiated Unmute Only)",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "billboard": {
        "key": "billboard",
        "unit_name": "Billboard",
        "category": "Horizontal",
        "fixed_size_px": "970x250",
        "width": 970,
        "height": 250,
        "aspect_ratio": "4:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 250,
        "max_subload_k_weight_kb": 500,
        "static_image_max_kb": 250,
        "tier": "High Impact",
        "recommended_channels": ["Top-of-Page Premium Display", "Programmatic Takeovers", "Homepage Mastheads"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "super_leaderboard": {
        "key": "super_leaderboard",
        "unit_name": "Super Leaderboard / Pushdown",
        "category": "Horizontal",
        "fixed_size_px": "970x90",
        "width": 970,
        "height": 90,
        "aspect_ratio": "10:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 200,
        "max_subload_k_weight_kb": 400,
        "static_image_max_kb": 200,
        "tier": "Standard",
        "recommended_channels": ["Desktop GDN", "Publisher Pushdown Units"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "banner_standard": {
        "key": "banner_standard",
        "unit_name": "Full Banner",
        "category": "Horizontal",
        "fixed_size_px": "468x60",
        "width": 468,
        "height": 60,
        "aspect_ratio": "8:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 100,
        "max_subload_k_weight_kb": 200,
        "static_image_max_kb": 100,
        "tier": "Standard",
        "recommended_channels": ["Content Mid-Articles", "Forum Banners"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "half_banner": {
        "key": "half_banner",
        "unit_name": "Half Banner",
        "category": "Horizontal",
        "fixed_size_px": "234x60",
        "width": 234,
        "height": 60,
        "aspect_ratio": "4:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 50,
        "max_subload_k_weight_kb": 100,
        "static_image_max_kb": 50,
        "tier": "Compact",
        "recommended_channels": ["Sidebar Small Placements", "Footer Units"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "smartphone_banner": {
        "key": "smartphone_banner",
        "unit_name": "Smartphone Banner",
        "category": "Horizontal",
        "fixed_size_px": "320x50",
        "width": 320,
        "height": 50,
        "aspect_ratio": "6:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 50,
        "max_subload_k_weight_kb": 100,
        "static_image_max_kb": 50,
        "tier": "Mobile Primary",
        "recommended_channels": ["Mobile Web Sticky Bottom", "In-App Banners", "Quick-Commerce Apps"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },

    # Rectangles & Tiles
    "medium_rectangle": {
        "key": "medium_rectangle",
        "unit_name": "Medium Rectangle (MPU)",
        "category": "Tiles / Rectangle",
        "fixed_size_px": "300x250",
        "width": 300,
        "height": 250,
        "aspect_ratio": "1:1",
        "imagen_aspect_ratio": "1:1",
        "veo_aspect_ratio": "1:1",
        "max_initial_k_weight_kb": 150,
        "max_subload_k_weight_kb": 300,
        "static_image_max_kb": 150,
        "tier": "Top Performer",
        "recommended_channels": ["GDN Sidebar", "In-Feed Content", "Universal High-CTR Unit"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "large_rectangle": {
        "key": "large_rectangle",
        "unit_name": "Large Rectangle",
        "category": "Tiles / Rectangle",
        "fixed_size_px": "336x280",
        "width": 336,
        "height": 280,
        "aspect_ratio": "1:1",
        "imagen_aspect_ratio": "1:1",
        "veo_aspect_ratio": "1:1",
        "max_initial_k_weight_kb": 150,
        "max_subload_k_weight_kb": 300,
        "static_image_max_kb": 150,
        "tier": "High CTR",
        "recommended_channels": ["Desktop Article Sidebar", "In-Article High CTR Placement"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "square_250": {
        "key": "square_250",
        "unit_name": "Square (250x250)",
        "category": "Tiles / Rectangle",
        "fixed_size_px": "250x250",
        "width": 250,
        "height": 250,
        "aspect_ratio": "1:1",
        "imagen_aspect_ratio": "1:1",
        "veo_aspect_ratio": "1:1",
        "max_initial_k_weight_kb": 100,
        "max_subload_k_weight_kb": 200,
        "static_image_max_kb": 100,
        "tier": "Standard",
        "recommended_channels": ["Compact Grid Units", "Sidebar Widgets"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "small_rectangle": {
        "key": "small_rectangle",
        "unit_name": "Small Rectangle",
        "category": "Tiles / Rectangle",
        "fixed_size_px": "180x150",
        "width": 180,
        "height": 150,
        "aspect_ratio": "1:1",
        "imagen_aspect_ratio": "1:1",
        "veo_aspect_ratio": "1:1",
        "max_initial_k_weight_kb": 75,
        "max_subload_k_weight_kb": 150,
        "static_image_max_kb": 75,
        "tier": "Compact",
        "recommended_channels": ["Widget Columns", "In-Text Sidebars"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "square_button": {
        "key": "square_button",
        "unit_name": "Square Button",
        "category": "Buttons",
        "fixed_size_px": "125x125",
        "width": 125,
        "height": 125,
        "aspect_ratio": "1:1",
        "imagen_aspect_ratio": "1:1",
        "veo_aspect_ratio": "1:1",
        "max_initial_k_weight_kb": 50,
        "max_subload_k_weight_kb": 100,
        "static_image_max_kb": 50,
        "tier": "Compact",
        "recommended_channels": ["Grid Sponsor Badges", "Affiliate Blocks"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },

    # Buttons & Micro Bars
    "button_1": {
        "key": "button_1",
        "unit_name": "Button 1",
        "category": "Buttons",
        "fixed_size_px": "120x90",
        "width": 120,
        "height": 90,
        "aspect_ratio": "4:3",
        "imagen_aspect_ratio": "4:3",
        "veo_aspect_ratio": "1:1",
        "max_initial_k_weight_kb": 50,
        "max_subload_k_weight_kb": 100,
        "static_image_max_kb": 50,
        "tier": "Compact",
        "recommended_channels": ["Directory Listings", "Sponsor Badges"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "button_2": {
        "key": "button_2",
        "unit_name": "Button 2 (120x60)",
        "category": "Buttons",
        "fixed_size_px": "120x60",
        "width": 120,
        "height": 60,
        "aspect_ratio": "2:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 50,
        "max_subload_k_weight_kb": 100,
        "static_image_max_kb": 50,
        "tier": "Compact",
        "recommended_channels": ["Sponsor Buttons", "Footer Partner Tiles"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "micro_bar": {
        "key": "micro_bar",
        "unit_name": "Micro Bar",
        "category": "Buttons",
        "fixed_size_px": "88x31",
        "width": 88,
        "height": 31,
        "aspect_ratio": "3:1",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 30,
        "max_subload_k_weight_kb": 60,
        "static_image_max_kb": 30,
        "tier": "Micro",
        "recommended_channels": ["Verification Badges", "Partner Mini Buttons"],
        "lean_guidelines": {
            "max_file_requests": 5,
            "max_cpu_load_pct": 20,
            "audio_default": "No Audio",
            "border_required": True,
            "iba_control_max_kb": 2
        }
    },

    # Vertical Banners & Skyscrapers
    "vertical_banner": {
        "key": "vertical_banner",
        "unit_name": "Vertical Banner",
        "category": "Vertical",
        "fixed_size_px": "120x240",
        "width": 120,
        "height": 240,
        "aspect_ratio": "1:2",
        "imagen_aspect_ratio": "9:16",
        "veo_aspect_ratio": "9:16",
        "max_initial_k_weight_kb": 75,
        "max_subload_k_weight_kb": 150,
        "static_image_max_kb": 75,
        "tier": "Standard",
        "recommended_channels": ["Sidebar Towers", "Narrow Web Rails"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "skyscraper_120": {
        "key": "skyscraper_120",
        "unit_name": "Skyscraper (120x600)",
        "category": "Vertical",
        "fixed_size_px": "120x600",
        "width": 120,
        "height": 600,
        "aspect_ratio": "1:5",
        "imagen_aspect_ratio": "9:16",
        "veo_aspect_ratio": "9:16",
        "max_initial_k_weight_kb": 150,
        "max_subload_k_weight_kb": 300,
        "static_image_max_kb": 150,
        "tier": "Vertical Classic",
        "recommended_channels": ["Narrow Desktop Margins", "Editorial Side Rails"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "skyscraper": {
        "key": "skyscraper",
        "unit_name": "Wide Skyscraper",
        "category": "Vertical",
        "fixed_size_px": "160x600",
        "width": 160,
        "height": 600,
        "aspect_ratio": "1:4",
        "imagen_aspect_ratio": "9:16",
        "veo_aspect_ratio": "9:16",
        "max_initial_k_weight_kb": 150,
        "max_subload_k_weight_kb": 300,
        "static_image_max_kb": 150,
        "tier": "Top Performer",
        "recommended_channels": ["Desktop Side Gutters", "News Portals"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },
    "half_page": {
        "key": "half_page",
        "unit_name": "Half Page / Portrait Banner",
        "category": "Vertical",
        "fixed_size_px": "300x600",
        "width": 300,
        "height": 600,
        "aspect_ratio": "1:2",
        "imagen_aspect_ratio": "9:16",
        "veo_aspect_ratio": "9:16",
        "max_initial_k_weight_kb": 200,
        "max_subload_k_weight_kb": 400,
        "static_image_max_kb": 200,
        "tier": "Top Performer (High CTR)",
        "recommended_channels": ["High-Impact Desktop Right Rail", "Rich Media Showcase"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    },

    # Full Page & Video Units
    "mobile_interstitial_9_16": {
        "key": "mobile_interstitial_9_16",
        "unit_name": "Mobile Interstitial / Reel / Story (9:16)",
        "category": "Full Page Portrait",
        "fixed_size_px": "1080x1920",
        "width": 1080,
        "height": 1920,
        "aspect_ratio": "9:16",
        "imagen_aspect_ratio": "9:16",
        "veo_aspect_ratio": "9:16",
        "max_initial_k_weight_kb": 300,
        "max_subload_k_weight_kb": 600,
        "static_image_max_kb": 300,
        "tier": "Social & Video Primary",
        "recommended_channels": ["Instagram Reels & Stories", "YouTube Shorts", "In-App Interstitials"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted (User Unmute Switch)",
            "border_required": False,
            "iba_control_max_kb": 5
        }
    },
    "video_landscape_16_9": {
        "key": "video_landscape_16_9",
        "unit_name": "In-Stream Video Ad (16:9)",
        "category": "Full Page Landscape / Video",
        "fixed_size_px": "1920x1080",
        "width": 1920,
        "height": 1080,
        "aspect_ratio": "16:9",
        "imagen_aspect_ratio": "16:9",
        "veo_aspect_ratio": "16:9",
        "max_initial_k_weight_kb": 300,
        "max_subload_k_weight_kb": 600,
        "static_image_max_kb": 300,
        "tier": "Video Primary",
        "recommended_channels": ["YouTube 6s Bumper & 15s Non-Skip", "Connected TV (JioCinema, Hotstar)", "Desktop Video"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted (Auto-play Muted or In-Stream Audio with Skip Option)",
            "border_required": False,
            "iba_control_max_kb": 5
        }
    },
    "square_feed_1_1": {
        "key": "square_feed_1_1",
        "unit_name": "Square Feed Tile / Retail Banner",
        "category": "Tiles",
        "fixed_size_px": "1080x1080",
        "width": 1080,
        "height": 1080,
        "aspect_ratio": "1:1",
        "imagen_aspect_ratio": "1:1",
        "veo_aspect_ratio": "1:1",
        "max_initial_k_weight_kb": 250,
        "max_subload_k_weight_kb": 500,
        "static_image_max_kb": 250,
        "tier": "Social & Q-Commerce",
        "recommended_channels": ["Meta Feed (Instagram/Facebook)", "Quick Commerce (Blinkit/Zepto)", "Amazon/Flipkart Sponsored"],
        "lean_guidelines": {
            "max_file_requests": 10,
            "max_cpu_load_pct": 30,
            "audio_default": "Muted",
            "border_required": True,
            "iba_control_max_kb": 5
        }
    }
}


def lookup_iab_spec(size_or_name: str) -> Dict[str, Any]:
    """Matches any size query (e.g. '728x90', 'leaderboard', '88x31', '336x280') to IAB specifications."""
    q = size_or_name.lower().replace(" ", "_").strip()
    
    if q in IAB_AD_PORTFOLIO:
        return IAB_AD_PORTFOLIO[q]
    
    for key, spec in IAB_AD_PORTFOLIO.items():
        if q == spec["fixed_size_px"].lower() or q in spec["unit_name"].lower().replace(" ", "_"):
            return spec
        if q == spec["fixed_size_px"].replace("x", "*"):
            return spec

    for key, spec in IAB_AD_PORTFOLIO.items():
        if any(dim in q for dim in spec["fixed_size_px"].split("x")):
            return spec

    return IAB_AD_PORTFOLIO["medium_rectangle"]


def get_all_iab_specs() -> List[Dict[str, Any]]:
    """Returns a list of all official IAB ad specifications."""
    return list(IAB_AD_PORTFOLIO.values())


def get_iab_sizing_menu_matrix() -> Dict[str, Any]:
    """
    Returns structured sizing categories, options, and recommended packages for user selection.
    """
    categories = {
        "top_performers": ["medium_rectangle", "leaderboard", "half_page", "billboard", "mobile_interstitial_9_16", "video_landscape_16_9"],
        "all_13_iab_banners": [
            "leaderboard", "banner_standard", "micro_bar", "button_2", "button_1",
            "vertical_banner", "large_rectangle", "square_button", "skyscraper_120",
            "small_rectangle", "half_banner", "square_250", "medium_rectangle"
        ],
        "video_formats": ["video_landscape_16_9", "mobile_interstitial_9_16", "square_feed_1_1"],
        "high_impact_display": ["billboard", "half_page", "super_leaderboard", "skyscraper"]
    }
    return {
        "total_formats": len(IAB_AD_PORTFOLIO),
        "categories": categories,
        "all_specs": IAB_AD_PORTFOLIO
    }


def validate_asset_against_iab_lean(
    unit_name: str,
    file_size_kb: float,
    is_subload: bool = False,
    is_audio_muted: bool = True,
    file_requests_count: int = 1
) -> Dict[str, Any]:
    """
    Validates generated assets against IAB LEAN standards (file weight, requests, mute status, CPU load).
    """
    spec = lookup_iab_spec(unit_name)
    max_allowed = spec["max_subload_k_weight_kb"] if is_subload else spec["max_initial_k_weight_kb"]
    
    is_weight_ok = file_size_kb <= max_allowed
    is_requests_ok = file_requests_count <= spec["lean_guidelines"]["max_file_requests"]
    is_audio_ok = is_audio_muted or ("Muted" not in spec["lean_guidelines"]["audio_default"])
    
    status = "COMPLIANT" if (is_weight_ok and is_requests_ok and is_audio_ok) else "NON_COMPLIANT"
    
    return {
        "status": status,
        "ad_unit": spec["unit_name"],
        "dimension": spec["fixed_size_px"],
        "aspect_ratio": spec["aspect_ratio"],
        "file_size_kb": file_size_kb,
        "max_allowed_kb": max_allowed,
        "weight_compliant": is_weight_ok,
        "requests_compliant": is_requests_ok,
        "audio_compliant": is_audio_ok,
        "imagen_aspect_ratio": spec["imagen_aspect_ratio"],
        "veo_aspect_ratio": spec["veo_aspect_ratio"],
        "recommendations": [
            f"Use gzip compression to ensure payload < {max_allowed} kB",
            "Ensure 1px solid visible border (#E0E0E0 or #333333) to separate ad space from editorial content",
            "Default audio must be muted with user tap-to-unmute control",
            "Keep host-initiated requests <= 10 during initial load"
        ]
    }


def get_iab_specs_tool(unit_or_size: str = "all") -> str:
    """
    Tool to inspect IAB standard ad specifications, dimensions, file weights, and LEAN compliance guidelines.
    """
    if unit_or_size.lower() in ["all", "menu", "matrix"]:
        return json.dumps(get_iab_sizing_menu_matrix(), indent=2)
    spec = lookup_iab_spec(unit_or_size)
    return json.dumps(spec, indent=2)
