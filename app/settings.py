from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    random_api_base_url: str = "http://localhost:5000"