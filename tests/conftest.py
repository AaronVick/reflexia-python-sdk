"""Pytest configuration and shared fixtures."""

import pytest
from unittest.mock import Mock, MagicMock
from typing import Dict, Any

from reflexia import ReflexiaClient


@pytest.fixture
def mock_api_key():
    """Mock API key for testing."""
    return "rk_test_1234567890abcdef"


@pytest.fixture
def client(mock_api_key):
    """Create a ReflexiaClient instance for testing."""
    return ReflexiaClient(api_key=mock_api_key, base_url="https://api.reflexia.io")


@pytest.fixture
def mock_session():
    """Create a mock requests session."""
    session = MagicMock()
    session.headers = {}
    return session


@pytest.fixture
def mock_success_response():
    """Mock successful API response."""
    response = Mock()
    response.ok = True
    response.status_code = 200
    response.json.return_value = {"success": True}
    response.headers = {}
    return response


@pytest.fixture
def mock_error_response():
    """Mock error API response."""
    response = Mock()
    response.ok = False
    response.status_code = 400
    response.text = "Bad Request"
    response.reason = "Bad Request"
    response.json.return_value = {
        "error": {
            "code": "INVALID_REQUEST",
            "message": "Invalid request",
            "details": {},
        },
        "request_id": "req-test-123",
    }
    response.headers = {}
    return response


@pytest.fixture
def mock_register_agent_response():
    """Mock response for register_agent."""
    return {
        "agent_id": "test-agent-1",
        "position": {"x": 42.3, "y": 67.8},
        "session_token": "dGVzdC1zZXNzaW9uLXRva2Vu",
    }


@pytest.fixture
def mock_sense_response():
    """Mock response for sense."""
    return {
        "local_value": 0.65,
        "gradient_x": 0.12,
        "gradient_y": -0.08,
        "gradient_magnitude": 0.144,
        "should_activate": True,
        "activation_priority": 0.72,
        "nearby_agents": [
            {
                "agent_id": "other-agent",
                "agent_type": "researcher",
                "position": {"x": 43.0, "y": 68.0},
                "distance": 1.2,
            }
        ],
    }


@pytest.fixture
def mock_modify_response():
    """Mock response for modify."""
    return {
        "accepted": True,
        "new_local_value": 0.75,
        "field_iteration": 1234,
    }


@pytest.fixture
def mock_consistency_response():
    """Mock response for check_consistency."""
    return {
        "abstained": False,
        "winning_hash": "abc123def456",
        "majority_vote": 0.8,
        "confidence": 0.85,
        "request_id": "req-test-123",
    }


@pytest.fixture
def mock_pattern_store_response():
    """Mock response for store_pattern."""
    return {
        "pattern_id": "pattern-123",
        "is_new": True,
        "occurrence_count": 1,
    }


@pytest.fixture
def mock_pattern_query_response():
    """Mock response for query_patterns."""
    return {
        "patterns": [
            {
                "pattern_id": "pattern-123",
                "outcome_hash": "def456",
                "confidence": 0.9,
                "occurrence_count": 5,
            }
        ],
    }


@pytest.fixture
def mock_aggregate_response():
    """Mock response for aggregate_patterns."""
    return {
        "patterns": [
            {
                "outcome_hash": "def456",
                "avg_confidence": 0.88,
                "tenant_count": 5,
                "total_occurrences": 25,
            }
        ],
        "k_anonymity_met": True,
    }

