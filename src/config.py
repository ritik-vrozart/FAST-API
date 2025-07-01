from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
   DB_URI :str = "postgresql://postgres:postgres@localhost:5432/sample"  # Default value, replace as needed

   model_config = SettingsConfigDict(env_file=".env")


Config = Settings()