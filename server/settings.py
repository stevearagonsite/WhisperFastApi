from functools import lru_cache


class Settings:
    PROJECT_NAME: str = "FastAPI Role Based Access Control Auth Service"
    API_V1_STR: str = "/api/v1"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
