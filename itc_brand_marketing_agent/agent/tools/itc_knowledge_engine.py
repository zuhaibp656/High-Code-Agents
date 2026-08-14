"""
ITC Knowledge Engine - Comprehensive brand intelligence, campaign hooks, creative hooks,
audience segmentation, and historical marketing benchmarks for ITC Limited brands.
"""

from typing import Dict, List, Any, Optional
import json

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

SEASONAL_CAMPAIGN_HOOKS = {
    "festive_diwali": {
        "theme": "Diwali & Festive Gifting Sparkle",
        "angles": [
            {"hook": "Upgrade your festive gifting from ordinary sweets to bespoke single-origin Fabelle artisanal chocolate boxes.", "brand": "fabelle"},
            {"hook": "Bring warmth and blessings home this Diwali with pure Aashirvaad Svasti Ghee sweets and softest rotis.", "brand": "aashirvaad"},
            {"hook": "Turn post-Diwali puja hunger into an indulgent late-night Dark Fantasy chocolate feast.", "brand": "dark_fantasy"},
            {"hook": "Light up the festival with vibrant Engage party fragrances that last all night through card parties.", "brand": "engage"}
        ]
    },
    "cricket_ipl": {
        "theme": "IPL & Live Sports Match-Day Snacking",
        "angles": [
            {"hook": "Every boundary demands an explosive crunch - Grab Bingo! Mad Angles Achaari Masti for the super-over!", "brand": "bingo"},
            {"hook": "4 wickets down? Calm the tension with a quick 5-minute hot bowl of Yippee! Magic Masala noodles.", "brand": "yippee"},
            {"hook": "Hydrate between innings with 100% pure B Natural Alphonso Mango pulp nectar.", "brand": "b_natural"}
        ]
    },
    "monsoon_rainy": {
        "theme": "Monsoon Cravings & Rainy Day Warmth",
        "angles": [
            {"hook": "Raindrops outside, piping hot crispy Aashirvaad Pakodas and golden Rotis inside.", "brand": "aashirvaad"},
            {"hook": "Monsoon evening tea ritual is incomplete without microwave-warmed molten Dark Fantasy Choco Fills.", "brand": "dark_fantasy"},
            {"hook": "Slurp into steaming hot bowl of spicy Yippee! Mood Masala while watching the rain.", "brand": "yippee"}
        ]
    },
    "summer_heat": {
        "theme": "Summer Freshness, Hydration & Rejuvenation",
        "angles": [
            {"hook": "Wash away 40°C summer heat and fatigue with invigorating Fiama Lemongrass shower gel therapy.", "brand": "fiama"},
            {"hook": "Beat the scorching sun with 0% concentrate 100% pure chilled B Natural Pomegranate and Coconut Water.", "brand": "b_natural"},
            {"hook": "Stay pocket-fresh 24 hours against summer sweat with Engage Pocket Perfume.", "brand": "engage"}
        ]
    },
    "back_to_school": {
        "theme": "Back-to-School, College Admissions & Exams",
        "angles": [
            {"hook": "Fastest notes, zero ink smudge - Power your exam preparation with Classmate Pulse & Octane.", "brand": "classmate"},
            {"hook": "Tiffin box champion - Soft Aashirvaad rotis that stay tender till the 1:30 PM lunch bell.", "brand": "aashirvaad"},
            {"hook": "Healthy 4 PM homework study snack with Yippee! Power Up Atta noodles packed with veggies.", "brand": "yippee"}
        ]
    },
    "hygiene_wellness": {
        "theme": "Monsoon Flu, School Hygiene & Daily Protection",
        "angles": [
            {"hook": "Let kids play fearless in the mud - Savlon's no-sting antiseptic heals playground scrapes without tears.", "brand": "savlon"},
            {"hook": "Protect hands before every meal with Savlon Moisture Shield 99.9% germ-kill handwash.", "brand": "savlon"}
        ]
    }
}


def lookup_brand(brand_query: str) -> Dict[str, Any]:
    """Retrieves full brand intelligence for any ITC brand query."""
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


def generate_brand_hooks_data(brand_name: str, campaign_theme: Optional[str] = None) -> Dict[str, Any]:
    """
    Synthesizes campaign hooks, creative angles, sensory triggers, and audience personas for a specific ITC brand.
    """
    brand_data = lookup_brand(brand_name)
    key_theme = campaign_theme.lower() if campaign_theme else "festive_diwali"
    
    # Match seasonal hook
    matched_seasonal = None
    for k, v in SEASONAL_CAMPAIGN_HOOKS.items():
        if k in key_theme or any(word in key_theme for word in k.split("_")):
            matched_seasonal = v
            break
    if not matched_seasonal:
        matched_seasonal = SEASONAL_CAMPAIGN_HOOKS["festive_diwali"]

    return {
        "brand": brand_data["brand_name"],
        "category": brand_data["category"],
        "taglines": brand_data["taglines"],
        "color_palette": brand_data["color_palette"],
        "visual_aesthetic": brand_data["visual_aesthetic"],
        "sensory_triggers": brand_data["sensory_triggers"],
        "products": brand_data["key_products"],
        "target_segments": brand_data["target_segments"],
        "historical_benchmarks": brand_data["historical_benchmarks"],
        "campaign_theme": matched_seasonal["theme"],
        "seasonal_hooks": matched_seasonal["angles"]
    }


def get_itc_brand_profile_tool(brand_name: str, campaign_theme: str = "festive_diwali") -> str:
    """
    Tool to extract rich brand identity, campaign hooks, sensory keywords, audience segments, and benchmarks for ITC brands.
    """
    data = generate_brand_hooks_data(brand_name=brand_name, campaign_theme=campaign_theme)
    return json.dumps(data, indent=2)
