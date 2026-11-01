# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Focus Recovery Binaural Beats Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentFocusRecoveryBinauralBeats

mcp = FastMCP("PersonalAgentFocusRecoveryBinauralBeats")
client = PersonalAgentFocusRecoveryBinauralBeats()

@mcp.tool()
def calculate_binaural_entrainment_parameters(
    target_cognitive_state: str = "deep_focus",
    carrier_base_hz: float = 216.0
) -> str:
    """Calculates left/right ear stereo frequencies and ASSR parameters for brainwave entrainment."""
    import json
    return json.dumps(client.calculate_binaural_entrainment_parameters(target_cognitive_state, carrier_base_hz), indent=2)

@mcp.tool()
def schedule_auditory_entrainment_protocol(
    work_block_duration_minutes: float = 90.0,
    fatigue_level: str = "moderate"
) -> str:
    """Generates a phased 3-stage binaural entrainment sequence tailored to work session length."""
    import json
    return json.dumps(client.schedule_auditory_entrainment_protocol(work_block_duration_minutes, fatigue_level), indent=2)

if __name__ == "__main__":
    mcp.run()
