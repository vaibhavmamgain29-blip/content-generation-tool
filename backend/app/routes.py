"""FastAPI routes for the content generation tool."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from .config import get_settings
from .llm.factory import get_llm
from .schemas import GenerateRequest, HealthResponse

router = APIRouter(prefix="/api")


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    settings = get_settings()

    return HealthResponse(
    status="ok",
    llm_configured=settings.is_configured,
    model=f"{settings.llm_provider}:{getattr(settings, f'{settings.llm_provider}_model', 'unknown')}",
    )


@router.post("/generate")
async def generate(req: GenerateRequest):
    """Generate streamed content using the configured LLM."""

    settings = get_settings()

    if not settings.is_configured:
        raise HTTPException(
            status_code=503,
            detail=f"{settings.llm_provider.upper()} is not configured.",
        )

    llm = get_llm()

    return StreamingResponse(
        llm.stream(
            prompt=req.prompt,
            temperature=req.temperature,
            max_tokens=req.max_tokens,
        ),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )