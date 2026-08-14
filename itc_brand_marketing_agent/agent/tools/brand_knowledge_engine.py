"""
ITC Brand Intelligence & Dynamic Hook Generation Engine.
Maintains comprehensive brand profiles for 11+ ITC Limited brands and provides automated
checking, extraction, and synthesis for Campaign Briefs, Creative Hooks, and Media Plans.
"""

import os
import json
import re
from typing import Dict, List, Any, Optional

from .doc_reader_engine import (
    ITC_MARKETING_DIR,
    read_marketing_document,
    save_marketing_document,
    list_marketing_folders
)

ITC_BRANDS = {
    "dark_fantasy": {
        "brand_name": "Sunfeast Dark Fantasy",
        "category": "Foods - Indulgent Biscuits & Bakery",
        "parent": "ITC Foods",
        "taglines": [
            "Can't Wait, Won't Wait",
            "Har Dil Ki Fantasy",
            "Din Khatam, Fantasy Shuru",
            "Escape into Pure Molten Choco Indulgence"
        ],
        "brand_pillars": ["Molten Chocolate Indulgence", "Sensory Escape", "Evening Me-Time Ritual", "Premium Craftsmanship"],
        "color_palette": {
            "primary": "#2A1810",       # Rich Dark Cacao
            "secondary": "#D4AF37",     # Molten Gold
            "accent": "#6D3B23",        # Warm Chocolate Cream
            "highlight": "#FFF8E7"      # Vanilla Cream
        },
        "visual_aesthetic": "Cinematic chiaroscuro, slow-motion molten choco core oozing, velvety chocolate textures, warm golden rim lighting, moody premium dark backdrop with amber highlights.",
        "sensory_triggers": ["Molten liquid choco burst", "Crisp outer crust crack", "Aromas of Belgian cocoa", "Silky lingering finish"],
        "key_products": [
            {"name": "Dark Fantasy Choco Fills", "usp": "Crisp cookie crust filled with rich molten liquid choco"},
            {"name": "Dark Fantasy Coffee Fills", "usp": "Arabica coffee essence paired with dark molten chocolate"},
            {"name": "Dark Fantasy Bourbon", "usp": "Rich chocolate biscuit sprinkled with crunchy sugar crystals"},
            {"name": "Dark Fantasy Desserts Choco Lava", "usp": "Warm microwaveable dessert experience at home"}
        ],
        "target_segments": [
            {"segment": "Working Millennials", "demo": "22-38 yrs, Urban Metro/Tier 1", "mindset": "Seeking evening decompression, premium me-time guilt-free treats"},
            {"segment": "Late Night Gen Z Snackers", "demo": "18-24 yrs, College & Early Career", "mindset": "Midnight study/binge companion, viral dessert recipes on reels"},
            {"segment": "Festive Gifting Buyers", "demo": "25-45 yrs, Premium households", "mindset": "Gifting modern indulgent confectionery instead of traditional sweets"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.24%",
            "video_vtr_15s": "48.5%",
            "social_story_ctr": "1.35%",
            "top_converting_hooks": ["Molten chocolate core break in first 0.5s", "Late night 'Din Khatam' narrative", "Microwave 10s warm gooey hack"]
        }
    },
    "aashirvaad": {
        "brand_name": "Aashirvaad",
        "category": "Foods - Staples & Organic Nutrition",
        "parent": "ITC Foods",
        "taglines": [
            "Shuddhata Ka Asli Aashirvaad",
            "Happy Tummies, Healthy Families",
            "Rotiyan Itni Soft Ki Haath Lagao Aur Toot Jaaye",
            "100% Pure Chakki Atta with 0% Maida"
        ],
        "brand_pillars": ["Uncompromised Purity", "Maternal Love & Nourishment", "Traditional Chakki Grinding", "Digestive Wellness"],
        "color_palette": {
            "primary": "#E5A93C",       # Golden Harvest Wheat
            "secondary": "#2E7D32",     # Farm Fresh Emerald
            "accent": "#C62828",        # Traditional Red
            "neutral": "#FFFDF7"        # Natural Cream
        },
        "visual_aesthetic": "Sun-drenched golden wheat fields, rustic earthenware, traditional stone chakki textures, steaming hot fluffy puffed rotis with glistening golden ghee, warm family dining sunlight.",
        "sensory_triggers": ["Aroma of freshly roasted wheat", "Super soft 3-finger roti tear", "Warm puffy steam rising", "Wholesome golden grain texture"],
        "key_products": [
            {"name": "Aashirvaad Shudh Chakki Atta", "usp": "100% whole wheat, traditional 4-step sorting, 0% maida"},
            {"name": "Aashirvaad Select Sharbati Atta", "usp": "100% MP Sharbati wheat, golden grain, stays soft for hours"},
            {"name": "Aashirvaad Svasti Pure Cow Ghee", "usp": "Special slow-cook process for golden granular aroma"},
            {"name": "Aashirvaad Organic Dals & Pulses", "usp": "100% certified organic, chemical-free farm traceability"}
        ],
        "target_segments": [
            {"segment": "Health-Conscious Homemakers", "demo": "28-50 yrs, Tier 1/2/3 pan-India", "mindset": "Committed to family health, zero compromise on grain purity & softness"},
            {"segment": "Fitness & Clean Eating Seekers", "demo": "24-40 yrs, Urban", "mindset": "Focus on high-fiber, gut health, millet superfoods, organic staples"},
            {"segment": "Young Working Couples", "demo": "25-35 yrs, Metros", "mindset": "Quick cooking convenience without sacrificing traditional home taste"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.19%",
            "video_vtr_15s": "42.1%",
            "social_story_ctr": "1.10%",
            "top_converting_hooks": ["Roti staying soft after 6 hours in lunchbox", "100% Whole wheat purity demonstration", "Mother's blessings & happy gut smiles"]
        }
    },
    "bingo": {
        "brand_name": "Bingo!",
        "category": "Foods - Savoury Snacks & Chips",
        "parent": "ITC Foods",
        "taglines": [
            "Har Angle Se Mmm...",
            "Tedhe Medhe - Eat Phir Repeat",
            "Full Flavour, No Boring",
            "Mad Angles, Mad Fun"
        ],
        "brand_pillars": ["Irreverent Humor", "Explosive Crunch & Tang", "Spicy Unpredictability", "Youth Hangout Energy"],
        "color_palette": {
            "primary": "#FFD700",       # Electric Yellow
            "secondary": "#E60000",     # Fire Chili Red
            "accent": "#8A2BE2",        # Pop Purple
            "dark": "#1A1A1A"           # Charcoal Crunch
        },
        "visual_aesthetic": "High-energy pop art visuals, dynamic flying snack triangles with spice powder dust clouds, 3D motion trails, bold typography punchlines, vibrant neon backgrounds.",
        "sensory_triggers": ["Loud dynamic snap crunch", "Tangy spice burst coating the tongue", "Sizzling chili flakes", "Irresistible lick-your-fingers masala"],
        "key_products": [
            {"name": "Bingo! Mad Angles Achaari Masti", "usp": "Unique triangular shape with authentic tangy mango pickle seasoning"},
            {"name": "Bingo! Tedhe Medhe", "usp": "Spindle shape with crunchy multigrain blend and spicy masala twist"},
            {"name": "Bingo! Hashtags", "usp": "Checkerboard lattice chip with extreme crunch and cheddar spicy seasoning"},
            {"name": "Bingo! Original Style Potato Chips", "usp": "Thin, crisp golden potato wafers with sea salt & pepper"}
        ],
        "target_segments": [
            {"segment": "Gen Z College Students & Gamers", "demo": "16-24 yrs, Urban & Tier 1/2", "mindset": "High snacking frequency, streaming, gaming fuel, meme culture affinity"},
            {"segment": "Young Office Gangs", "demo": "22-30 yrs, Tech parks & Co-working", "mindset": "Chai-time breaks, 4 PM hunger busters, group sharing"},
            {"segment": "Cricket & Sports Binge Watchers", "demo": "18-40 yrs, Pan-India", "mindset": "High excitement, match-time crunching companion"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.31%",
            "video_vtr_15s": "52.8%",
            "social_story_ctr": "1.82%",
            "top_converting_hooks": ["Exploding spice triangle in first 0.3s", "Quirky gaming/hostel comedy skit", "Loud ASMR crunch sound sync"]
        }
    },
    "yippee": {
        "brand_name": "Sunfeast Yippee! Noodles",
        "category": "Foods - Instant Noodles & Pastas",
        "parent": "ITC Foods",
        "taglines": [
            "No Lump, No Sticky, Just Long Noodles",
            "Mood Badle Mood Masala Se",
            "Spread The Joy, Slurp The Fun",
            "Long Non-Sticky Fun for Everyone"
        ],
        "brand_pillars": ["Non-Sticky Long Noodles", "Wholesome Veggie Infusion", "Vibrant Playful Energy", "Dual Masala Customization"],
        "color_palette": {
            "primary": "#FF6B00",       # Sunshine Orange
            "secondary": "#E50914",     # Bold Tomato Red
            "accent": "#00A86B",        # Fresh Green Veggie
            "highlight": "#FFEA00"      # Golden Noodle
        },
        "visual_aesthetic": "Appetizing swirling fork twirl lifting steaming long noodles, colorful fresh diced veggies (carrots, peas, corn), glossy rich broth, joyful vibrant kitchen & campus settings.",
        "sensory_triggers": ["Steaming noodle slurp sound", "Rich spicy aroma filling the room", "Tender non-sticky noodle texture", "Colorful veggie bite"],
        "key_products": [
            {"name": "Yippee! Magic Masala Noodles", "usp": "Signature blend of 5 veggies, round block for long unbroken noodles"},
            {"name": "Yippee! Mood Masala Noodles", "usp": "Two masala sachets: Main Masala + Mood Mix to customize spice level"},
            {"name": "Yippee! Power Up Atta Noodles", "usp": "Whole wheat goodness infused with real vegetable nutrients"},
            {"name": "Yippee! Quik Mezze Tricolor Pasta", "usp": "100% suji durum wheat pasta in creamy cheese & tomato sauce"}
        ],
        "target_segments": [
            {"segment": "School & College Youth", "demo": "12-22 yrs, Pan-India", "mindset": "Fun quick meals, after-school snack, creative noodle toppings"},
            {"segment": "Modern Mothers", "demo": "28-42 yrs, Tier 1/2/3", "mindset": "Wants instant noodles with real veggies, non-lumpy easy cooking"},
            {"segment": "Hostelers & Bachelors", "demo": "18-28 yrs, Urban", "mindset": "Midnight lifesaver, simple 5-minute single-pot cooking"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.26%",
            "video_vtr_15s": "46.2%",
            "social_story_ctr": "1.42%",
            "top_converting_hooks": ["Long unbroken noodle fork pull", "Mood Masala spice twist reveal", "Rainy evening hot noodle bowl"]
        }
    },
    "b_natural": {
        "brand_name": "B Natural",
        "category": "Foods - Juices & Beverages",
        "parent": "ITC Foods",
        "taglines": [
            "Real Indian Fruits, 0% Concentrate",
            "Taste the Orchard in Every Sip",
            "Nourished by Indian Farmers, Loved by You",
            "100% Desi Fruit Goodness"
        ],
        "brand_pillars": ["Zero Concentrate Purity", "100% Indian Fruit Sourcing", "Farmer Support & Sustainability", "Orchard Fresh Taste"],
        "color_palette": {
            "primary": "#388E3C",       # Orchard Leaf Green
            "secondary": "#FFB300",     # Alphonso Mango Gold
            "accent": "#D81B60",        # Ruby Pomegranate
            "light": "#E8F5E9"          # Dew White
        },
        "visual_aesthetic": "Lush sunny Indian fruit orchards, dew-kissed juicy fruit halves slicing open, crystal-clear splashing nectar, natural glass bottle refraction, golden morning sunshine.",
        "sensory_triggers": ["Lush fruit slice splash", "Thick pulp texture pouring into glass", "Refreshing condensation beads on glass", "Burst of authentic orchard sweetness"],
        "key_products": [
            {"name": "B Natural Mixed Fruit", "usp": "Crafted from Indian fruit pulps, no added concentrate"},
            {"name": "B Natural Himalayan Apple", "usp": "Crisp sweet apples directly from Himachal orchards"},
            {"name": "B Natural Alphonso Mango", "usp": "Rich Ratnagiri Alphonso pulp for thick authentic nectar"},
            {"name": "B Natural 100% Pomegranate", "usp": "Pure pomegranate juice with zero added sugar or concentrates"}
        ],
        "target_segments": [
            {"segment": "Health & Fitness Enthusiasts", "demo": "22-40 yrs, Urban Metros", "mindset": "Scrutinizes ingredient labels, rejects concentrate-based artificial juices"},
            {"segment": "Family Breakfast Curators", "demo": "30-48 yrs, Tier 1/2", "mindset": "Wholesome morning nutrition for kids and elderly parents"},
            {"segment": "Summer Refreshment Seekers", "demo": "18-35 yrs, Pan-India", "mindset": "Thirst-quenching natural chilled beverages"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.21%",
            "video_vtr_15s": "41.0%",
            "social_story_ctr": "1.25%",
            "top_converting_hooks": ["Fruit sliced in half with juice splash in 0.4s", "Zero concentrate vs concentrate label check", "Indian farmer orchard origin story"]
        }
    },
    "fiama": {
        "brand_name": "Fiama",
        "category": "Personal Care - Shower Gels & Bathing Luxury",
        "parent": "ITC Personal Care",
        "taglines": [
            "Mood Uplifting Showers",
            "Joyful Skin, Happy You",
            "Feel the Radiance, Wash Away the Stress",
            "Botanical Goodness in Every Drop"
        ],
        "brand_pillars": ["Mood Upliftment & Aromatherapy", "Skin Nourishment with Micro-Conditioners", "Joyful Bathing Experience", "Vibrant Jewel Aesthetics"],
        "color_palette": {
            "primary": "#00B4D8",       # Refreshing Aqua
            "secondary": "#7209B7",     # Exotic Berry Violet
            "accent": "#FF70A6",        # Peach Coral Glow
            "glow": "#CCFF33"           # Citrus Energy
        },
        "visual_aesthetic": "Crystalline water droplets, floating exotic botanical petals (lemongrass, bearberry, blackcurrant), translucent jewel-toned gel lathering into rich micro-bubbles, soft diffused spa lighting.",
        "sensory_triggers": ["Aromatic essential oil burst", "Silky soft gel glide on skin", "Effervescent water splash", "Invigorating mood rejuvenation"],
        "key_products": [
            {"name": "Fiama Shower Gel Blackcurrant & Bearberry", "usp": "Mood uplifting aroma with skin conditioning beads"},
            {"name": "Fiama Gel Bathing Bar Lemongrass & Jojoba", "usp": "Clear translucent bar that locks in skin moisture"},
            {"name": "Fiama Happy Naturals Shower Gel", "usp": "97% naturally derived ingredients, dermatologist tested"},
            {"name": "Fiama Handwash Relax & Refresh", "usp": "Gentle cleansing with essential oils and soft foam"}
        ],
        "target_segments": [
            {"segment": "Urban Working Millennials", "demo": "20-35 yrs, Metros & Tier 1", "mindset": "Showers as a stress-relief therapy ritual after grueling workdays"},
            {"segment": "Self-Care & Skincare Enthusiasts", "demo": "18-30 yrs, Urban", "mindset": "Focus on glowing skin, sensory aroma, aesthetic bathroom products"},
            {"segment": "Aspirational Tier 2 Youth", "demo": "18-28 yrs, Tier 2 hubs", "mindset": "Upgrading from standard soaps to modern shower gels"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.28%",
            "video_vtr_15s": "50.4%",
            "social_story_ctr": "1.65%",
            "top_converting_hooks": ["Slow-mo jewel gel drop with micro-bubbles in first 0.5s", "Work stress melting away in refreshing shower", "Aromatherapy mood boost before a night out"]
        }
    },
    "savlon": {
        "brand_name": "Savlon",
        "category": "Personal Care & Hygiene - Antiseptic & Health Care",
        "parent": "ITC Personal Care",
        "taglines": [
            "Chot Pe Dettol Nahi, Savlon Lagao - Na Dukhaye",
            "Savlon Swasth India - Healing Without The Stinging",
            "Tough on Germs, Gentle on Skin",
            "Trusted Protection for Those You Love"
        ],
        "brand_pillars": ["No-Sting Gentle Healing", "99.99% Germ Protection", "Family Compassion & Care", "Innovation for Social Good"],
        "color_palette": {
            "primary": "#005696",       # Medical Trust Blue
            "secondary": "#FFFFFF",     # Clean Pure White
            "accent": "#FF8C00",        # Healing Orange
            "safe": "#009688"           # Gentle Teal
        },
        "visual_aesthetic": "Crisp bright clean lighting, comforting touch of parents tending to playground scrapes, invisible protective shield hologram against bacteria, gentle foam lather.",
        "sensory_triggers": ["Soothing no-sting relief", "Gentle non-drying foam lather", "Clean comforting antiseptic fragrance", "Reassuring warm hug"],
        "key_products": [
            {"name": "Savlon Antiseptic Liquid", "usp": "Clinically proven germ protection that does not sting on minor cuts"},
            {"name": "Savlon Moisture Shield Handwash", "usp": "99.9% germ kill with added moisturizers to protect soft hands"},
            {"name": "Savlon Germ Protection Soap", "usp": "Triple protection against bacteria, sweat odor, and dust"},
            {"name": "Savlon Surface Disinfectant Spray", "usp": "Kills viruses and bacteria on hard and soft surfaces instantly"}
        ],
        "target_segments": [
            {"segment": "Protective Mothers & Caregivers", "demo": "25-45 yrs, Pan-India", "mindset": "Preventing kids from fearing wound treatment, total home hygiene without harsh chemicals"},
            {"segment": "Health & Infection Conscious Families", "demo": "25-60 yrs, Urban & Semi-Urban", "mindset": "Daily handwashing and surface sanitization against seasonal flu"},
            {"segment": "Schools & Sports Academies", "demo": "Institutional & Community", "mindset": "Safe playground first-aid and hygiene training"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.18%",
            "video_vtr_15s": "45.0%",
            "social_story_ctr": "1.15%",
            "top_converting_hooks": ["Child smiling while getting scraped knee treated (no tears)", "Microscopic 99.99% germ shield demonstration", "Mother's gentle touch with handwash"]
        }
    },
    "engage": {
        "brand_name": "Engage",
        "category": "Personal Care - Fragrances & Deodorants",
        "parent": "ITC Personal Care",
        "taglines": [
            "Playful Chemistry",
            "Carry Your Charm in Your Pocket",
            "24-Hour Irresistible Fragrance",
            "Spark the Romance Everywhere"
        ],
        "brand_pillars": ["Playful Romantic Chemistry", "Pocket-Sized Innovation", "Long-Lasting All-Day Scent", "Youthful Charisma"],
        "color_palette": {
            "primary": "#1A1A2E",       # Midnight Navy
            "secondary": "#E94560",     # Romantic Crimson
            "accent": "#0F3460",        # Deep Blue
            "spark": "#FFD700"          # Gold Sparkle
        },
        "visual_aesthetic": "Sleek pocket flacons with magnetic metallic sheen, fine misty spray dispersal catching neon nightclub lights, romantic playful glances between couples in stylish urban settings.",
        "sensory_triggers": ["Crisp citrus & amber mist burst", "Intoxicating woody undertones", "Instant surge of confidence", "Magnetic attraction pull"],
        "key_products": [
            {"name": "Engage Pocket Perfume (Men & Women)", "usp": "Card-thin pocket spray delivering 250 sprays of fine perfume anywhere"},
            {"name": "Engage Cologne Spray", "usp": "Long-lasting fragrance crafted by French perfumers with zero gas"},
            {"name": "Engage 2-in-1 Deodorant (Yin & Yang)", "usp": "Dual fragrance nozzles in one can for custom scent blending"},
            {"name": "Engage L'Amante Luxury Eau De Parfum", "usp": "Premium international fragrance line with Italian bergamot and leather"}
        ],
        "target_segments": [
            {"segment": "Young Dating Couples & Singles", "demo": "18-28 yrs, Urban & Tier 1/2", "mindset": "Dating, parties, evening dates, wanting to smell attractive on the go"},
            {"segment": "College Students & Young Professionals", "demo": "18-26 yrs", "mindset": "Budget-friendly pocket convenience for spontaneous post-work plans"},
            {"segment": "Premium Fragrance Seekers", "demo": "24-35 yrs, Metros", "mindset": "Affordable luxury EDP with long-lasting projection"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.33%",
            "video_vtr_15s": "54.2%",
            "social_story_ctr": "1.90%",
            "top_converting_hooks": ["Quick pocket card spray before stepping into date", "Playful flirtatious eye-contact scene", "Fine mist explosion under neon city lights"]
        }
    },
    "fabelle": {
        "brand_name": "Fabelle Luxury Chocolates",
        "category": "Foods - Ultra-Luxury Confectionery",
        "parent": "ITC Foods",
        "taglines": [
            "Crafted to Perfection, Curated for Connoisseurs",
            "When Chocolate Meets Artistry",
            "Unmatched Single-Origin Indulgence",
            "The Haute Chocolaterie of India"
        ],
        "brand_pillars": ["Artisanal Craftsmanship", "Single-Origin Single-Estate Cacao", "Multi-Sensory Chocolate Sculpting", "Ultra-Luxury Gifting"],
        "color_palette": {
            "primary": "#0D0D0D",       # Obsidian Velvet
            "secondary": "#C5A059",     # Antique Matte Gold
            "accent": "#4A154B",        # Royal Plum
            "pearl": "#F8F5F0"          # Ivory Silk
        },
        "visual_aesthetic": "Bespoke marble chocolaterie ateliers, 24k edible gold leaf flakes floating onto glossy dark ganache spheres, slow ribbons of tempered chocolate, luxury black textured gift boxes with gold embossing.",
        "sensory_triggers": ["Snap of perfectly tempered chocolate shell", "Velvety ganache melting at body temperature", "Single-origin floral notes of Madagascar cacao", "Rich nutty Gianduja paste"],
        "key_products": [
            {"name": "Fabelle Gianduja", "usp": "Recreation of Italian delicacy with creamy Turkish hazelnuts and Ghana cacao"},
            {"name": "Fabelle The Bars Secret - Single Origin Cacao", "usp": "Single-estate chocolate bars sourced from 6 continents"},
            {"name": "Fabelle Elements - Handcrafted Pralines", "usp": "5 handcrafted chocolate pralines inspired by Earth, Air, Water, Fire, Wood"},
            {"name": "Fabelle Master's Selection", "usp": "Bespoke luxury hampers for corporate CXO and elite wedding gifting"}
        ],
        "target_segments": [
            {"segment": "High-Net-Worth Connoisseurs", "demo": "28-55 yrs, Metros, Top 1%", "mindset": "Appreciates haute cuisine, single-origin wines & chocolates, bespoke gifting"},
            {"segment": "Luxury Wedding & Corporate Gifters", "demo": "30-60 yrs, Corporate & Elite", "mindset": "Impressing clients and guests with opulent presentation and exclusivity"},
            {"segment": "Special Occasion Romantics", "demo": "24-40 yrs, Urban", "mindset": "Valentine's Day, Anniversaries, Milestone celebration luxury treats"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.22%",
            "video_vtr_15s": "49.0%",
            "social_story_ctr": "1.50%",
            "top_converting_hooks": ["Chocolatier hand-placing 24k gold leaf on praline in 0.5s", "Ganache spherical shell cracking to reveal molten core", "Unboxing black velvet textured gift hamper"]
        }
    },
    "itc_hotels": {
        "brand_name": "ITC Hotels",
        "category": "Hospitality - Luxury Hotels & Fine Dining",
        "parent": "ITC Hotels",
        "taglines": [
            "Responsible Luxury",
            "Experience Royal Indian Hospitality",
            "Where Cultural Grandeur Meets Sustainable Opulence",
            "Epicurean Journeys: Bukhara, Dum Pukht & Royal Bengal"
        ],
        "brand_pillars": ["Responsible Luxury (LEED Platinum Certified)", "Royal Indian Heritage Architecture", "Legendary Culinary Heritage", "Impeccable Gracious Hospitality"],
        "color_palette": {
            "primary": "#8B0000",       # Royal Crimson
            "secondary": "#DAA520",     # Imperial Gold
            "accent": "#1E3F20",        # Forest Green
            "ivory": "#FAF0E6"          # Linen Ivory
        },
        "visual_aesthetic": "Colossal marble pillars, handcrafted Chola bronze sculptures, ornate Mughal jharokhas, candle-lit royal banquet tables with silver cloches, steaming Bukhara Dal Bukhara simmered for 18 hours.",
        "sensory_triggers": ["Aroma of smoked charcoal kebabs & Dum Pukht biryani", "Cool polished marble underfoot", "Soothing sitar music in grand lobbies", "Silken Egyptian cotton bed sheets"],
        "key_products": [
            {"name": "ITC Grand Chola (Chennai)", "usp": "Southern temple architecture with 600 luxury rooms and 10 iconic dining destinations"},
            {"name": "ITC Maurya & Bukhara (New Delhi)", "usp": "Legendary diplomatic hospitality and world-famous Bukhara tandoori cuisine"},
            {"name": "ITC Royal Bengal & Sonar (Kolkata)", "usp": "Palatial aristocratic Bengal heritage alongside tranquil water lilies"},
            {"name": "Kaya Kalp - The Royal Spa", "usp": "Traditional Ayurvedic therapies and wellness retreats"}
        ],
        "target_segments": [
            {"segment": "Global Business Executives & Diplomats", "demo": "35-65 yrs, Global & Pan-India", "mindset": "Expects world-class security, quiet luxury, seamless executive amenities"},
            {"segment": "Luxury Leisure Travelers & Families", "demo": "30-55 yrs, Affluent", "mindset": "Heritage staycations, experiential culinary dining, bespoke spa retreats"},
            {"segment": "Grand Destination Wedding Hosts", "demo": "40-65 yrs, High Net Worth", "mindset": "Extravagant royal venues, customized master-chef banqueting"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.20%",
            "video_vtr_15s": "47.8%",
            "social_story_ctr": "1.30%",
            "top_converting_hooks": ["Grand aerial drone shot of palatial hotel lit up at night", "Chef plating Dal Bukhara with smoking charcoal in 0.5s", "Bride walking through royal marble corridors"]
        }
    },
    "classmate": {
        "brand_name": "Classmate",
        "category": "Education & Stationery - Notebooks & Writing",
        "parent": "ITC Education & Stationery",
        "taglines": [
            "Because You Are One of a Kind",
            "Joy of Learning, Smoothness in Writing",
            "Smooth Paper for Sharp Minds",
            "Empowering Young Imaginations"
        ],
        "brand_pillars": ["Elemental Chlorine-Free Paper", "Ultra-Smooth Writing Surface", "Interactive Learning Covers", "Student Empowerment"],
        "color_palette": {
            "primary": "#00A896",       # Smart Teal
            "secondary": "#028090",     # Deep Cyan
            "accent": "#F0F3F4",        # Crisp Notebook White
            "highlight": "#FFB703"      # Bright Amber
        },
        "visual_aesthetic": "Sunlit modern classrooms and study desks, sharp macro nib strokes gliding frictionlessly across bright white paper, colorful origami paper crafts, energetic student smiles.",
        "sensory_triggers": ["Smooth effortless glide of pen on page", "Crisp turn of paper page", "Bright clean white paper clarity", "Vibrant cover art"],
        "key_products": [
            {"name": "Classmate Pulse Notebooks", "usp": "Stylish neon covers with 3D tactile finish for college students"},
            {"name": "Classmate Interaktiv", "usp": "Notebooks with origami activities, DIY 3D paper crafts, and STEM puzzles"},
            {"name": "Classmate Octane Gel & Ball Pens", "usp": "Waterproof ink, effortless Japanese tip glide, smudge-free writing"},
            {"name": "Classmate Artist Series Sketchbooks", "usp": "Heavyweight acid-free drawing sheets for watercolors and charcoal"}
        ],
        "target_segments": [
            {"segment": "School & College Students", "demo": "10-22 yrs, Pan-India", "mindset": "Smooth exam notes taking, stylish covers to stand out in class"},
            {"segment": "Competitive Exam Aspirants", "demo": "18-26 yrs (UPSC, JEE, NEET, CA)", "mindset": "Fast tireless writing, non-bleeding paper, reliable high-speed pens"},
            {"segment": "Quality Conscious Parents & Teachers", "demo": "30-50 yrs", "mindset": "Eco-friendly chlorine-free safe paper for kids"}
        ],
        "historical_benchmarks": {
            "display_ctr": "0.25%",
            "video_vtr_15s": "43.5%",
            "social_story_ctr": "1.38%",
            "top_converting_hooks": ["Macro pen nib gliding across smooth paper without ink smudges", "Back-to-school exciting stationery haul unboxing", "Transforming notebook cover into 3D origami robot"]
        }
    }
}


def lookup_brand(brand_query: str) -> Dict[str, Any]:
    """Retrieves brand intelligence for any ITC brand query."""
    q = brand_query.lower().strip()
    for key, data in ITC_BRANDS.items():
        if key in q or data["brand_name"].lower() in q:
            return data
        for prod in data["key_products"]:
            if prod["name"].lower() in q:
                return data
    # Fallback to dark_fantasy if not found
    return ITC_BRANDS["dark_fantasy"]


def get_all_itc_brands() -> List[str]:
    """Returns a list of all supported ITC brand names."""
    return [b["brand_name"] for b in ITC_BRANDS.values()]


def check_or_create_campaign_brief(brand_name: str, campaign_theme: str = "festive_diwali") -> str:
    """
    Checks if a campaign brief exists in 'Campaign Hooks/' for the brand.
    If present, reads and returns it. If not present, dynamically synthesizes and saves
    a comprehensive brand campaign brief into 'Campaign Hooks/'.
    """
    brand_data = lookup_brand(brand_name)
    sanitized_brand = brand_name.lower().replace(" ", "_")
    
    # 1. Search existing files in Campaign Hooks
    campaign_hooks_dir = os.path.join(ITC_MARKETING_DIR, "Campaign Hooks")
    if os.path.exists(campaign_hooks_dir):
        for f in os.listdir(campaign_hooks_dir):
            if sanitized_brand in f.lower() or brand_data["brand_name"].lower().split()[0] in f.lower():
                content = read_marketing_document("Campaign Hooks", f)
                if not content.startswith("Error:"):
                    return f"### [Document Found: {f}]\n\n{content}"

    # 2. Synthesize new campaign brief
    brief = f"""# Campaign Strategy Brief & Audience Insights
## Brand: {brand_data['brand_name']} ({brand_data['category']})
**Parent Company:** {brand_data['parent']} | **Theme:** {campaign_theme.replace('_', ' ').title()}

---

### 1. Executive Summary & Brand Purpose
{brand_data['brand_name']} is an iconic market leader in India, driven by the core values of {', '.join(brand_data['brand_pillars'])}. 
Under the campaign theme **"{campaign_theme.replace('_', ' ').title()}"**, the objective is to drive high-impact emotional resonance, boost brand recall, and trigger immediate digital / retail conversion.

### 2. Core Brand Taglines & Philosophy
- **Primary Tagline:** "{brand_data['taglines'][0]}"
- **Alternate Taglines:** {', '.join([f'"{t}"' for t in brand_data['taglines'][1:]])}

### 3. Key Hero Products & Value Propositions
"""
    for p in brand_data["key_products"]:
        brief += f"- **{p['name']}**: {p['usp']}\n"

    brief += f"""
### 4. Target Audience Profiles & Pain Points
"""
    for s in brand_data["target_segments"]:
        brief += f"- **Segment:** {s['segment']} ({s['demo']})\n  *Mindset & Desires:* {s['mindset']}\n"

    brief += f"""
### 5. Signature Sensory Triggers & Visual Guidelines
- **Sensory Triggers:** {', '.join(brand_data['sensory_triggers'])}
- **Visual Aesthetic:** {brand_data['visual_aesthetic']}
- **Primary Palette:** `{brand_data['color_palette'].get('primary', '#062F62')}` | **Secondary Palette:** `{brand_data['color_palette'].get('secondary', '#D4AF37')}`

### 6. Historical Performance Benchmarks
- **Display Banner CTR:** {brand_data['historical_benchmarks']['display_ctr']}
- **Video View-Through Rate (15s):** {brand_data['historical_benchmarks']['video_vtr_15s']}
- **Social Story CTR:** {brand_data['historical_benchmarks']['social_story_ctr']}
- **Top Historical Converting Angles:** {', '.join(brand_data['historical_benchmarks']['top_converting_hooks'])}
"""
    # Save the synthesized document
    save_filename = f"{sanitized_brand}_campaign_brief.md"
    save_marketing_document("Campaign Hooks", save_filename, brief)
    return f"### [Document Auto-Created & Saved: {save_filename}]\n\n{brief}"


def check_or_create_creative_hooks(brand_name: str, campaign_theme: str = "festive_diwali", core_idea: Optional[str] = None) -> str:
    """
    Checks if creative hooks/scripts exist in 'Creative Hooks/' for the brand.
    If present, reads and returns them. If not present, generates 4 creative hook variations
    and the 4-Part Sub-Prompt Decomposition (Hero, Background, Headline, CTA), and saves them.
    """
    brand_data = lookup_brand(brand_name)
    sanitized_brand = brand_name.lower().replace(" ", "_")
    
    # 1. Search existing files in Creative Hooks
    creative_hooks_dir = os.path.join(ITC_MARKETING_DIR, "Creative Hooks")
    if os.path.exists(creative_hooks_dir):
        for f in os.listdir(creative_hooks_dir):
            if sanitized_brand in f.lower() or brand_data["brand_name"].lower().split()[0] in f.lower():
                content = read_marketing_document("Creative Hooks", f)
                if not content.startswith("Error:"):
                    return f"### [Creative Document Found: {f}]\n\n{content}"

    # 2. Synthesize new creative hooks & 4-part sub-prompts
    idea_text = core_idea if core_idea else f"Experience the pure sensory bliss of {brand_data['brand_name']} {brand_data['key_products'][0]['name']}"
    
    hero_focal = f"Ultra-photorealistic commercial hero shot of {brand_data['brand_name']} {brand_data['key_products'][0]['name']}, showcasing {brand_data['sensory_triggers'][0]} with studio lighting and authentic packaging."
    bg_env = f"Atmospheric lifestyle setting tailored for {campaign_theme.replace('_', ' ').title()}: {idea_text}. Visual aesthetic: {brand_data['visual_aesthetic']}"
    headline_copy = brand_data['taglines'][0]
    cta_action = "Buy Now on Blinkit, Zepto & Leading Stores"

    hooks_doc = f"""# Creative Hooks, Audio Scripts & 4-Part Sub-Prompts
## Brand: {brand_data['brand_name']} | Theme: {campaign_theme.replace('_', ' ').title()}

---

### 🌟 1. Concept Orchestration & 4-Part Sub-Prompt Decomposition
| Component | Creative Specification & Generation Prompt |
| :--- | :--- |
| **🎯 THE HERO (Focal Point)** | {hero_focal} |
| **🌄 BACKGROUND (Environment)** | {bg_env} |
| **✍️ HEADLINE / COPY** | "{headline_copy}" |
| **🚀 CTA / INTERACTION** | "{cta_action}" |

---

### 🎬 2. Multi-Angle Creative Hooks for Digital & Video Ads

1. **⚡ Pattern Interrupt Hook (0.5s Visual Scroll Stopper)**
   - *Visual:* Instant macro explosion / dynamic sensory reveal of {brand_data['sensory_triggers'][0]}.
   - *Audio Voiceover:* "Wait! Before you scroll—experience this!"
   - *Target Placement:* Instagram Reels, YouTube Shorts, Mobile Interstitials.

2. **❤️ Emotional & Cultural Connection Hook**
   - *Visual:* Warm, relatable Indian lifestyle moment ({brand_data['target_segments'][0]['segment']}) decompressing and bonding over {brand_data['brand_name']}.
   - *Audio Voiceover:* "{brand_data['taglines'][1] if len(brand_data['taglines']) > 1 else brand_data['taglines'][0]}"
   - *Target Placement:* Connected TV (Hotstar/JioCinema), YouTube In-Stream 15s.

3. **🔬 Sensory & Product USP Hook**
   - *Visual:* Slow-motion capture demonstrating {brand_data['key_products'][0]['usp']}.
   - *Audio Voiceover:* "Crafted without compromise. {brand_data['brand_pillars'][0]} in every bite/drop."
   - *Target Placement:* Google Display Network 300x250 & 728x90 banners.

4. **🛍️ High-Intent Quick-Commerce Conversion Hook**
   - *Visual:* Dynamic 1:1 product card with 10-minute delivery badge.
   - *Audio Voiceover:* "Craving it right now? Get it delivered to your doorstep in 10 minutes."
   - *Target Placement:* Blinkit, Zepto, Swiggy Instamart In-App Banners.
"""
    save_filename = f"{sanitized_brand}_creative_hooks.md"
    save_marketing_document("Creative Hooks", save_filename, hooks_doc)
    return f"### [Creative Document Auto-Created & Saved: {save_filename}]\n\n{hooks_doc}"


def check_or_create_media_plan(brand_name: str, budget_inr_lakhs: float = 50.0) -> str:
    """
    Checks if a media plan exists in 'Media Plan/' for the brand.
    If present, reads and returns it. If not present, generates a complete multi-channel
    media plan and budget allocation matrix, and saves it.
    """
    brand_data = lookup_brand(brand_name)
    sanitized_brand = brand_name.lower().replace(" ", "_")
    
    # 1. Search existing files in Media Plan
    media_plan_dir = os.path.join(ITC_MARKETING_DIR, "Media Plan")
    if os.path.exists(media_plan_dir):
        for f in os.listdir(media_plan_dir):
            if sanitized_brand in f.lower() or brand_data["brand_name"].lower().split()[0] in f.lower():
                content = read_marketing_document("Media Plan", f)
                if not content.startswith("Error:"):
                    return f"### [Media Plan Document Found: {f}]\n\n{content}"

    # 2. Synthesize new media plan
    b_yt = budget_inr_lakhs * 0.35
    b_meta = budget_inr_lakhs * 0.30
    b_gdn = budget_inr_lakhs * 0.20
    b_qc = budget_inr_lakhs * 0.15

    plan_doc = f"""# Multi-Channel Media Plan & Budget Allocation
## Brand: {brand_data['brand_name']} | Total Budget: ₹{budget_inr_lakhs:.2f} Lakhs

---

### 📊 1. Multi-Channel Budget Allocation & KPI Matrix
| Channel | Ad Format & Asset | Budget Share (%) | Allocated Spend (INR) | Primary Target KPI | Target Audience Segment |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **YouTube & Connected TV** | 16:9 In-Stream Non-Skip (15s) & Bumper (6s) | 35% | ₹{b_yt:.2f} Lakhs | 48% VTR (View-Through Rate) | {brand_data['target_segments'][0]['segment']} |
| **Meta (Instagram & Facebook)** | 9:16 Vertical Video Reels & 1:1 Carousel | 30% | ₹{b_meta:.2f} Lakhs | 1.45% CTR / 2.8x Engagement | {brand_data['target_segments'][1]['segment'] if len(brand_data['target_segments']) > 1 else brand_data['target_segments'][0]['segment']} |
| **Google Display Network (GDN)** | IAB Display Units (300x250, 728x90, 300x600, 970x250) | 20% | ₹{b_gdn:.2f} Lakhs | 0.26% Blended CTR | Contextual & In-Market Shoppers |
| **Quick Commerce (Blinkit/Zepto)** | 1:1 Sponsored Tiles & Category Banners | 15% | ₹{b_qc:.2f} Lakhs | 4.2x ROAS (Return on Ad Spend) | High-Intent 10-Min Shoppers |

---

### 📐 2. IAB Ad Unit Creative Specifications
- **Medium Rectangle (MPU)**: 300x250 (1:1 aspect ratio, <= 150 kB initial load)
- **Leaderboard**: 728x90 (8:1 aspect ratio, <= 150 kB initial load)
- **Half Page**: 300x600 (1:2 aspect ratio, <= 200 kB initial load)
- **Billboard**: 970x250 (4:1 aspect ratio, <= 250 kB initial load)
- **Vertical Reel / Mobile Interstitial**: 1080x1920 (9:16 aspect ratio, <= 300 kB)
- **In-Stream Landscape Video**: 1920x1080 (16:9 aspect ratio, <= 300 kB)

### 3. IAB LEAN Compliance Mandates
1. **Light**: Initial file weight <= 150-250 kB; max initial HTTP requests <= 10.
2. **Encrypted**: All creative assets served strictly over HTTPS.
3. **AdChoices**: Embedded IBA control icon (< 5 kB) in top-right corner.
4. **Non-Invasive**: CPU load <= 30%; audio starts MUTED with user-initiated unmute; 1px solid border applied.
"""
    save_filename = f"{sanitized_brand}_media_plan.md"
    save_marketing_document("Media Plan", save_filename, plan_doc)
    return f"### [Media Plan Auto-Created & Saved: {save_filename}]\n\n{plan_doc}"
