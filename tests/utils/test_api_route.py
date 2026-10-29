"""API Route client configuration contracts."""

from hyperextract.utils.client import create_llm


def test_create_llm_api_route(monkeypatch):
    """The named preset selects the API Route endpoint and provider key."""
    monkeypatch.setenv("OPENAI_API_KEY", "openai-test")
    monkeypatch.setenv("API_ROUTE_API_KEY", "route-test")
    llm = create_llm("api-route")
    assert llm.model_name == "gpt-6.1-sol"
    assert llm.openai_api_base == "https://global.api-route.com/v1"
    assert llm.openai_api_key.get_secret_value() == "route-test"


def test_create_llm_api_route_overrides(monkeypatch):
    """Explicit model and key override the preset and environment defaults."""
    monkeypatch.setenv("API_ROUTE_API_KEY", "route-test")
    llm = create_llm("api-route:custom-model", api_key="explicit-test")
    assert llm.model_name == "custom-model"
    assert llm.openai_api_base == "https://global.api-route.com/v1"
    assert llm.openai_api_key.get_secret_value() == "explicit-test"
