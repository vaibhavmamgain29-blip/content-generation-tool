"""Pydantic schemas for request/response validation."""
from __future__ import annotations

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """Request body for text generation."""

    prompt: str = Field(
        ...,
        min_length=1,
        max_length=8000,
    )

    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
    )

    max_tokens: int = Field(
        default=2048,
        ge=1,
        le=8192,
    )


class HealthResponse(BaseModel):
    """Response returned by /api/health."""

    status: str
    llm_configured: bool
    model: str