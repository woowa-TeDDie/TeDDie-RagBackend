from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    RELOAD: bool = True
    LOG_LEVEL: str = "info"
    ENV: str = "dev"

    PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent
    RAG_DATASET_PATH: Path = PROJECT_ROOT / "TeDDie-RagSystem" / "woowacourse_rag_dataset.jsonl"
    RAG_INDEX_PATH: Path = PROJECT_ROOT / "TeDDie-RagSystem" / "faiss_index.bin"

    DEFAULT_TOP_K: int = 3
    MAX_TOP_K: int = 10

    ENABLE_REQUEST_LOG: bool = True
    ENABLE_QUERY_LOG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
