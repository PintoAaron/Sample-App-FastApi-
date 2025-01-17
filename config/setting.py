from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    API_NAME: str = "SAMPLE APP"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "SAMPLE APP API"
    API_PREFIX: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./app_db.db"

    class config:
        env_file = ".env"


app_settings = AppSettings()
