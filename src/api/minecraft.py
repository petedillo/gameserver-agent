from fastapi import APIRouter, HTTPException
from src.utils import start_server, stop_server, restart_server, check_status

router = APIRouter()

@router.post("/start")
async def start_minecraft():
    result = start_server("minecraft")
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Failed to start Minecraft server")
    return {"message": "Minecraft server started"}

@router.post("/stop")
async def stop_minecraft():
    result = stop_server("minecraft")
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Failed to stop Minecraft server")
    return {"message": "Minecraft server stopped"}

@router.post("/restart")
async def restart_minecraft():
    result = restart_server("minecraft")
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Failed to restart Minecraft server")
    return {"message": "Minecraft server restarted"}

@router.get("/status")
async def status_minecraft():
    result = check_status("minecraft")
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result