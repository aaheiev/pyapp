import logging
import os
from os.path import join, dirname
from pathlib import Path

class Settings():
    DEBUG: bool = os.getenv("APP_DEBUG", 'True').lower() in ('true', '1', 't')
    APP_LOG_LEVEL: str = os.getenv("APP_LOG_LEVEL", 'INFO').upper()
    APP_LOG_FORMATTER: str = "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
    APP_NAME: str = f"Example python app: { os.getenv('APP_NAME', 'APP') }"
    APP_VERSION: str = os.getenv('APP_VERSION', 'development')
    APP_KEY: str = os.getenv("APP_KEY")
    APP_KEY_PATH: str = os.getenv("APP_KEY_PATH")

    def __init__(self):
        if not self.APP_KEY:
            if self.APP_KEY_PATH:
                self.APP_KEY = Path( self.APP_KEY_PATH ).read_text()
            else:
                message = "Either APP_KEY or APP_KEY_PATH must be set"
                logging.error(message)
                raise ValueError(message)

settings = Settings()

if __name__ == "__main__":
    print("this is settings.py file")
