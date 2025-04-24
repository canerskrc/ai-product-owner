from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DATABASE_URL: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    JIRA_CLIENT_ID: str
    JIRA_CLIENT_SECRET: str
    JIRA_REDIRECT_URI: str

    class Config:
        env_file = ".env"

settings = Settings()
