from pydantic import Field , ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str = Field(default="yolov8s")
    confidence: float = Field(default=0.4, ge=0.0, le=1.0)
    camera_id: int   = Field(default=0, ge=0)

    # Load from .env; no need to specify env names on each field
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
