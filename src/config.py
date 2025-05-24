import os

class Config:
    PROJECT_NAME = "GameServer Agent"
    VERSION = "1.0.0"
    MINECRAFT_SERVER_PATH = os.getenv("MINECRAFT_SERVER_PATH", "/path/to/minecraft/server")
    PALWORLD_SERVER_PATH = os.getenv("PALWORLD_SERVER_PATH", "/path/to/palworld/server")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")