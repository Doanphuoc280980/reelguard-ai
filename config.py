import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    META_API_URL: str = os.getenv("META_API_URL", "https://api.meta.com/v1/models/chat")
    META_API_KEY: str = os.getenv("META_API_KEY", "MOCK_META_KEY")
    WARNING_THRESHOLD_MINUTES: int = 20
    CRITICAL_THRESHOLD_MINUTES: int = 45

settings = Settings()
