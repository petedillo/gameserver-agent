from fastapi import APIRouter, HTTPException
from src.utils import start_server, stop_server, restart_server, check_status

router = APIRouter()

@router.post("/start")
async def start_palworld():
    result = start_server("palworld")
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Failed to start Palworld server")
    return {"message": "Palworld server started"}

@router.post("/stop")
async def stop_palworld():
    result = stop_server("palworld")
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Failed to stop Palworld server")
    return {"message": "Palworld server stopped"}

@router.post("/restart")
async def restart_palworld():
    result = restart_server("palworld")
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Failed to restart Palworld server")
    return {"message": "Palworld server restarted"}

@router.get("/status")
async def status_palworld():
    result = check_status("palworld")
    return {"status": result.stdout if result.stdout else result.stderr}