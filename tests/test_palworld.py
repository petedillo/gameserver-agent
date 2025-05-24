import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_start_palworld_server():
    response = client.post("/palworld/start")
    assert response.status_code == 200
    assert response.json() == {"message": "Palworld server started"}

def test_stop_palworld_server():
    response = client.post("/palworld/stop")
    assert response.status_code == 200
    assert response.json() == {"message": "Palworld server stopped"}

def test_restart_palworld_server():
    response = client.post("/palworld/restart")
    assert response.status_code == 200
    assert response.json() == {"message": "Palworld server restarted"}

def test_status_palworld_server():
    response = client.get("/palworld/status")
    assert response.status_code == 200
    assert "status" in response.json()