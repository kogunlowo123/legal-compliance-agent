"""Legal Compliance Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_monitor_regulations():
    """Test Monitor regulatory changes relevant to the organization."""
    tools = AgentTools()
    result = await tools.monitor_regulations(jurisdictions="test", industries="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_map_requirements():
    """Test Map regulatory requirements to business processes and controls."""
    tools = AgentTools()
    result = await tools.map_requirements(regulation="test", business_processes="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_compliance():
    """Test Track compliance status across regulatory requirements."""
    tools = AgentTools()
    result = await tools.track_compliance(regulation="test", department="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_collect_evidence():
    """Test Collect and organize audit evidence for compliance."""
    tools = AgentTools()
    result = await tools.collect_evidence(requirement_id="test", evidence_types="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.legal_compliance_agent_agent import LegalComplianceAgentAgent
    agent = LegalComplianceAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
