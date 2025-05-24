from fastapi import FastAPI
from src.api.minecraft import router as minecraft_router
from src.api.palworld import router as palworld_router

app = FastAPI()

app.include_router(minecraft_router, prefix="/minecraft", tags=["Minecraft"])
app.include_router(palworld_router, prefix="/palworld", tags=["Palworld"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the GameServer Agent API!"}