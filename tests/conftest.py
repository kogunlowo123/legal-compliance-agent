"""Test configuration for Legal Compliance Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "legal-compliance-agent", "category": "Legal"}
