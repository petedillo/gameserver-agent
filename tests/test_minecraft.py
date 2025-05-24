import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_start_minecraft_server():
    response = client.post("/minecraft/start")
    assert response.status_code == 200
    assert response.json() == {"message": "Minecraft server started"}

def test_stop_minecraft_server():
    response = client.post("/minecraft/stop")
    assert response.status_code == 200
    assert response.json() == {"message": "Minecraft server stopped"}

def test_restart_minecraft_server():
    response = client.post("/minecraft/restart")
    assert response.status_code == 200
    assert response.json() == {"message": "Minecraft server restarted"}

def test_status_minecraft_server():
    response = client.get("/minecraft/status")
    assert response.status_code == 200
    assert "status" in response.json()