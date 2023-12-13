from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    BOT_TOKEN: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_PORT: str
    DB_HOST: str

    @property
    def bot_token(self):
        return self.BOT_TOKEN

    @property
    def db_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='.env')


bot_config = BotConfig()
