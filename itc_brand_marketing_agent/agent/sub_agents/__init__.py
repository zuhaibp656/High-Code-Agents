"""
Sub-Agents Package for ITC Brand Marketing AI Agent.
"""

from .campaign_hook_agent import campaign_hook_agent
from .creative_hook_agent import creative_hook_agent
from .media_plan_agent import media_plan_agent
from .genmedia_iab_agent import genmedia_iab_agent

# Backwards compatible aliases
brand_hook_agent = campaign_hook_agent
iab_compliance_agent = genmedia_iab_agent
creative_gen_agent = genmedia_iab_agent

__all__ = [
    "campaign_hook_agent",
    "creative_hook_agent",
    "media_plan_agent",
    "genmedia_iab_agent",
    "brand_hook_agent",
    "iab_compliance_agent",
    "creative_gen_agent"
]
