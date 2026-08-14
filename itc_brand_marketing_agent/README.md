# 🍪 ITC Brand Marketing AI Agent

An autonomous, multi-modal generative marketing suite engineered for **ITC Limited** on the **Google Agent Development Kit (ADK)** and deployed directly to **Google Cloud Vertex AI Agent Engine (Reasoning Engine)** for **Gemini Enterprise**.

---

## 🌟 Executive Summary

The **ITC Brand Marketing AI Agent** empowers brand managers, creative directors, and media planners to plan, generate, resize, and validate omnichannel marketing assets across ITC’s brand portfolio (*Sunfeast Dark Fantasy, Bingo!, Fiama, Aashirvaad, Savlon, Engage, B Natural, Sunfeast Yippee!, Classmate, ITC Hotels, Fabelle*).

### 🚀 Key Capabilities:
- **🎨 Photorealistic Display Advertising**: Generates native in-image 3D commercial typography and brand taglines with zero artificial digital overlays.
- **📐 100% IAB LEAN Compliance**: Automatically validates and optimizes file weight (<150 KB) and aspect ratios across all 13 standard IAB banner units (300x250, 728x90, 300x600, 970x250, etc.) with lossless LANCZOS scaling.
- **🎬 Cinematic Video Commercials (Google Veo)**: Produces broadcast-ready 16:9 in-stream commercial spots (6s) and 9:16 vertical reels (10s) with 3-act storyboards.
- **🎯 Creative Hook & Strategy Synthesis**: Reads brand guidelines/briefs from `ITC Marketing Files/` or synthesizes 4-part sub-prompts (Hero, Background, Headline, CTA).
- **📊 Omnichannel Media Planning**: Computes multi-channel budget allocations across YouTube, Meta, GDN, and Quick-Commerce (Blinkit/Zepto) with automated CSV exports.
- **💾 Dual-Distribution Architecture**: Generates in-chat downloadable session artifacts (0 GCP permissions needed for business users) with Cloud Storage synchronization.

---

## 🏗️ System Architecture

```mermaid
flowchart TB
    subgraph ClientLayer["🖥️ Client Interface Layer"]
        GE["Gemini Enterprise Chat UI"]
        VAP["Vertex AI Agent Engine Playground"]
        CLI["Local ADK Interactive CLI"]
    end

    subgraph AgentEngine["⚡ Vertex AI Reasoning Engine / Agent Engine"]
        ADK["Google ADK Orchestrator\n(Gemini 2.5 Pro / Flash)"]
        ArtServ["ADK Artifact Service\n(In-Chat Direct Download Cards)"]
    end

    subgraph ToolSuite["🛠️ Autonomous Tool Engines"]
        DocTool["📂 Doc Reader Engine\n- list_marketing_folders\n- read_marketing_document\n- save_marketing_document"]
        BrandTool["📚 Brand Knowledge Engine\n- 11 ITC Brand DNAs\n- Sensory Triggers\n- Color Palettes & Logos"]
        GenMediaTool["🎨 GenMedia Engine\n- generate_marketing_image\n- generate_marketing_video\n- edit_marketing_video\n- resize_image_to_iab_format"]
        IABTool["📐 IAB Specs Engine\n- 13 IAB Format Matrices\n- LEAN Weight Validator\n- optimize_image_for_iab"]
        CampaignTool["🚀 Campaign Engine\n- check_or_create_brief\n- check_or_create_hooks\n- build_full_itc_campaign"]
    end

    subgraph FoundationModels["🧠 Foundation Models & APIs"]
        GeminiPro["Gemini 2.5 Pro\n(Prompt Synthesis & Strategy)"]
        GeminiFlashImg["Gemini 2.5 Flash Image / Imagen 3\n(Native Typography & Artwork)"]
        Veo["Google Veo 3.1 Fast\n(Cinematic Commercials)"]
    end

    subgraph StorageLayer["🗄️ Storage & Distribution"]
        GCS["Google Cloud Storage\ngs://itc-brand-marketing-assets-zuhaibp"]
        LocalFS["Local Runtime Container FS\n/app/generated_assets"]
    end

    %% Flow Connections
    ClientLayer -->|User Prompts & Media Requests| ADK
    ADK -->|Reasoning & Tool Selection| ToolSuite
    
    ToolSuite -->|Brand Context| BrandTool
    ToolSuite -->|Brand Docs & Briefs| DocTool
    
    GenMediaTool -->|Art Direction Prompt| GeminiPro
    GeminiPro -->|Photorealistic 3D Typography Prompt| GeminiFlashImg
    GenMediaTool -->|Video Script & Storyboard| Veo
    
    IABTool -->|LEAN Size Optimization (<150KB)| GenMediaTool
    
    GenMediaTool -->|Save Artifacts| ArtServ
    GenMediaTool -->|Sync Assets| GCS
    GenMediaTool -->|Local Cache| LocalFS
    
    ArtServ -->|1-Click Direct Download Attachment| ClientLayer
    GCS -->|Authenticated Console Link| ClientLayer
```

---

## 📂 Repository Structure

```text
itc_brand_marketing_agent/
├── agent/
│   ├── agent.py                      # Main ADK Agent Orchestrator & Instructions
│   ├── __init__.py
│   └── tools/
│       ├── brand_knowledge_engine.py # Brand profiles, taglines, hex colors, and sensory hooks
│       ├── campaign_engine.py        # Briefs, media budgets, and multi-channel campaign runner
│       ├── doc_reader_engine.py      # PDF, TXT, and Markdown knowledge file ingestion
│       ├── genmedia_engine.py        # Imagen 3, Gemini Flash Image, Veo 3.1, and IAB optimizer
│       └── iab_specs_engine.py       # Official 13-unit IAB sizing matrix and LEAN validators
├── IAB Formats/                      # Standard IAB dimension specifications
├── ITC Marketing/                    # Brand guidelines, product images, and ITC logo assets
├── generated_assets/                 # Output storage for images, videos, and media plan CSVs
│   ├── images/
│   ├── videos/
│   └── reports/
├── deploy.sh                         # Cloud deployment script to Vertex AI Agent Engine
├── main.py                           # Local interactive runner
├── requirements.txt                  # Python runtime dependencies
└── README.md                         # Project documentation
```

---

## 🛠️ Tool Suite Specifications

| Tool Name | Engine | Functionality |
|---|---|---|
| `generate_marketing_image` | GenMedia | Generates photorealistic IAB ads with native 3D typography and IAB LEAN compression (<150 KB). |
| `generate_marketing_video` | GenMedia / Veo | Produces 16:9 (6s) commercial spots or 9:16 (10s) reels with 3-act storyboards. |
| `resize_image_to_iab_format` | GenMedia / PIL | Adapts existing master art to any IAB dimension using lossless LANCZOS scaling without stretching. |
| `optimize_image_for_iab_compliance`| IAB Specs | Compresses any high-res banner to guarantee strict IAB LEAN payload limits. |
| `replicate_master_to_all_iab_formats`| GenMedia | Replicates master art across all 13 standard IAB ad units in a single invocation. |
| `check_or_create_creative_hooks` | Campaign | Ingests or synthesizes brand hooks (Pattern Interrupt, Hook, Benefit, CTA). |
| `check_or_create_media_plan` | Campaign | Allocates campaign budget across YouTube, Meta, GDN, and Quick-Commerce with CSV export. |
| `build_full_itc_campaign` | Campaign | End-to-end orchestrator: brief + hooks + multi-size banners + video ad + budget CSV. |

---

## 📐 IAB Display Ad Formats Supported

| IAB Unit Name | Dimensions (px) | Aspect Ratio | Max Initial Load | Key Placement |
|---|---|---|---|---|
| **Medium Rectangle** | 300x250 | 1.2:1 (6:5) | 150 KB | Desktop & Mobile Universal Standard |
| **Leaderboard** | 728x90 | 8.09:1 | 150 KB | Desktop Top Header |
| **Half Page / Skyscraper** | 300x600 | 1:2 (9:16) | 200 KB | Brand Storytelling & Rich Media |
| **Billboard** | 970x250 | 3.88:1 | 250 KB | Desktop Hero Placement |
| **Mobile Leaderboard** | 320x50 | 6.4:1 | 50 KB | Mobile In-App / Sticky Footer |
| **Wide Skyscraper** | 160x600 | 1:3.75 | 150 KB | Desktop Sidebar Navigation |
| **Large Rectangle** | 336x280 | 1.2:1 | 150 KB | High-Impact Editorial Placements |

---

## 🚀 Deployment & Usage

### 1. Local Environment Setup
```bash
# Clone and navigate to repository
cd itc_brand_marketing_agent

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION
```

### 2. Run Locally in CLI Mode
```bash
python main.py
```

### 3. Deploy to Vertex AI Agent Engine / Reasoning Engine
```bash
./deploy.sh
```
*Or deploy using Google ADK CLI directly:*
```bash
adk deploy agent_engine \
  --project="YOUR_PROJECT_ID" \
  --region="us-central1" \
  --agent_engine_id="YOUR_REASONING_ENGINE_ID" \
  --session_service_uri="agentengine://projects/YOUR_PROJECT_ID/locations/us-central1/reasoningEngines/YOUR_REASONING_ENGINE_ID" \
  --artifact_service_uri="memory://" \
  --display_name="ITC Brand Marketing AI Agent" \
  agent
```

---

## 🌟 Sample Prompt Gallery

### 1. Photorealistic IAB Display Ad with Native Typography
> *"Generate a 300x250 Medium Rectangle commercial ad for Bingo! Mad Angles featuring a crispy bowl of chips with friends laughing in the background, with the headline 'CRUNCH KA PUNCH' rendered natively into the artwork with golden cinematic lighting."*

### 2. Multi-Size IAB Adaptation
> *"Take the generated Sunfeast Dark Fantasy creative and resize it into a 728x90 Leaderboard and a 300x600 Half Page banner."*

### 3. Cinematic Commercial Video (Google Veo)
> *"Generate a 16:9 cinematic commercial video ad for Sunfeast Dark Fantasy Choco Fills showcasing the cookie breaking open in slow motion with rich molten chocolate flowing out."*

### 4. Full Omnichannel Campaign Plan
> *"Build a complete ₹50 Lakhs festive campaign for Aashirvaad Sharbati Atta including campaign brief, creative hooks, top IAB banners, a video ad, and a multi-channel media budget plan."*

---

## 📄 License & Compliance

- **Framework**: Google Agent Development Kit (ADK)
- **Standards**: Interactive Advertising Bureau (IAB) Standard Ad Unit Portfolio & LEAN Guidelines
- **Target Platform**: Google Cloud Vertex AI & Gemini Enterprise
