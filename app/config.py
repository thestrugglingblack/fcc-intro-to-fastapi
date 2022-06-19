from pydantic import BaseSettings

'''
SETTING ENVIRONMENT VARIABLES
Use pydantic to make sure that the environment variables are in the correct data type.
Pydantic automatically turns the environment variables to lowercase when it reads it.
'''
class Settings(BaseSettings):
    db_hostname: str
    db_port: str
    db_password: str
    db_username: str
    db_name: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = '.env'


settings = Settings()
