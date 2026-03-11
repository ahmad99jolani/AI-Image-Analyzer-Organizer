from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_VERSION: str
    APP_NAME: str
    IMAGE_TYPE: list
    IMAGE_SIZE: int
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()