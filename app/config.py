from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "MCP Server"
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
