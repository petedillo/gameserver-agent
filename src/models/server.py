from pydantic import BaseModel

class Server(BaseModel):
    name: str
    status: str

class GameServer(Server):
    game_type: str

    def start(self):
        # Implement logic to start the server
        pass

    def stop(self):
        # Implement logic to stop the server
        pass

    def restart(self):
        # Implement logic to restart the server
        pass

    def check_status(self):
        # Implement logic to check the server status
        pass