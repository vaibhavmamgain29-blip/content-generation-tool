"""Factory for selecting the configured LLM provider."""

from __future__ import annotations

from .groq import GroqProvider
from ..config import get_settings


def get_llm():
    """
    Return the configured LLM provider.
    """
    settings = get_settings()

    provider = settings.llm_provider.lower()

    if provider == "groq":
        return GroqProvider()

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )