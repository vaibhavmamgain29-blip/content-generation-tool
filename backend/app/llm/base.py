"""Base interface for all LLM providers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import AsyncGenerator


class BaseLLM(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    async def stream(
        self,
        prompt: str,
        temperature: float,
        max_tokens: int,
    ) -> AsyncGenerator[str, None]:
        """
        Stream the model response as Server-Sent Events (SSE).

        Every provider (Groq, Gemini, OpenAI, Ollama, etc.)
        must implement this method.

        Yields:
            SSE formatted strings.
        """
        raise NotImplementedError