from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.minecraft import router as minecraft_router
from src.api.palworld import router as palworld_router
from src.utils import get_basic_service_info
from src.systemd_service import check_status
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get CORS origins from environment variable
# Split the string by comma and strip whitespace
CORS_ORIGINS = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")]

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,  # Use environment variable
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(minecraft_router, prefix="/minecraft", tags=["Minecraft"])
app.include_router(palworld_router, prefix="/palworld", tags=["Palworld"])

@app.get("/")
def read_root():
    minecraft_status = check_status("minecraft")
    palworld_status = check_status("palworld")
    
    return {
        "message": "Welcome to the GameServer Agent API!",
        "services": [
            get_basic_service_info("minecraft", minecraft_status["active_state"]).to_dict(),
            get_basic_service_info("palworld", palworld_status["active_state"]).to_dict()
        ]
    }