"""Application configuration loaded from environment variables."""
from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    # ==========================================================
    # LLM Provider
    # ==========================================================
    llm_provider: str = Field(
        default="groq",
        alias="LLM_PROVIDER",
    )

    # ==========================================================
    # Groq
    # ==========================================================
    groq_api_key: str = Field(
        default="",
        alias="GROQ_API_KEY",
    )

    groq_model: str = Field(
        default="llama-3.3-70b-versatile",
        alias="GROQ_MODEL",
    )

    # ==========================================================
    # Gemini
    # ==========================================================
    gemini_api_key: str = Field(
        default="",
        alias="GEMINI_API_KEY",
    )

    gemini_model: str = Field(
        default="gemini-2.5-flash",
        alias="GEMINI_MODEL",
    )

    # ==========================================================
    # OpenAI
    # ==========================================================
    openai_api_key: str = Field(
        default="",
        alias="OPENAI_API_KEY",
    )

    openai_model: str = Field(
        default="gpt-4.1-mini",
        alias="OPENAI_MODEL",
    )

    # ==========================================================
    # Ollama
    # ==========================================================
    ollama_base_url: str = Field(
        default="http://localhost:11434",
        alias="OLLAMA_BASE_URL",
    )

    ollama_model: str = Field(
        default="llama3.2",
        alias="OLLAMA_MODEL",
    )

    # ==========================================================
    # CORS
    # ==========================================================
    cors_origins: str = Field(
        default="http://localhost:5173,http://127.0.0.1:5173,http://localhost:8080",
        alias="CORS_ORIGINS",
    )

    @property
    def allowed_origins(self) -> list[str]:
        """Return allowed CORS origins as a list."""
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]

    @property
    def is_configured(self) -> bool:
        """Check if the selected provider has the required configuration."""
        provider = self.llm_provider.lower()

        if provider == "groq":
            return bool(self.groq_api_key)

        if provider == "gemini":
            return bool(self.gemini_api_key)

        if provider == "openai":
            return bool(self.openai_api_key)

        if provider == "ollama":
            return True

        return False


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()