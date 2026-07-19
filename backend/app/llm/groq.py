"""Groq LLM Provider."""

from __future__ import annotations

import asyncio
import json
import logging
from typing import AsyncGenerator

from groq import AsyncGroq

from ..config import get_settings
from .base import BaseLLM

logger = logging.getLogger(__name__)


class GroqProvider(BaseLLM):
    """Groq implementation of the BaseLLM interface."""

    def __init__(self):
        self.settings = get_settings()

        if self.settings.is_configured:
            self.client = AsyncGroq(
                api_key=self.settings.groq_api_key
            )
        else:
            self.client = None

    async def stream(
        self,
        prompt: str,
        temperature: float,
        max_tokens: int,
    ) -> AsyncGenerator[str, None]:

        if self.client is None:
            yield (
                f"data: {json.dumps({'type': 'error', 'content': 'GROQ_API_KEY is not configured.'})}\n\n"
            )
            return

        try:
            stream = await self.client.chat.completions.create(
                model=self.settings.groq_model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
            )

            async for chunk in stream:

                if (
                    chunk.choices
                    and chunk.choices[0].delta.content
                ):
                    token = chunk.choices[0].delta.content

                    yield (
                        f"data: {json.dumps({'type': 'token', 'content': token})}\n\n"
                    )

                    await asyncio.sleep(0)

            yield (
                f"data: {json.dumps({'type': 'done'})}\n\n"
            )

        except Exception as e:
            logger.exception("Groq Streaming Error")

            yield (
                f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"
            )