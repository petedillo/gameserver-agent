# GameServer Agent

A FastAPI-based service for managing game servers. This implementation provides a RESTful API to control Minecraft and Palworld servers through systemd services.

## Features

- **Server Management**: Start, stop, restart, and check status of game servers
- **Systemd Integration**: Manages servers through systemd services
- **Docker Support**: Runs in a containerized environment
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation
- **Test Coverage**: Comprehensive test suite for all endpoints

## API Endpoints

### Minecraft Server
- `POST /minecraft/start` - Start the Minecraft server
- `POST /minecraft/stop` - Stop the Minecraft server
- `POST /minecraft/restart` - Restart the Minecraft server
- `GET /minecraft/status` - Get server status

### Palworld Server
- `POST /palworld/start` - Start the Palworld server
- `POST /palworld/stop` - Stop the Palworld server
- `POST /palworld/restart` - Restart the Palworld server
- `GET /palworld/status` - Get server status

## Project Structure

- `src/`: Contains the main application code.
  - `api/`: API route definitions for Minecraft and Palworld.
  - `core/`: Core logic for managing servers.
  - `models/`: Data models for server management.
  - `schemas/`: Pydantic schemas for request and response validation.
  - `config.py`: Configuration settings for the application.
  - `main.py`: Entry point for the FastAPI application.
  - `utils.py`: Utility functions used throughout the application.
  
- `tests/`: Contains unit tests for the application.
- `.env.example`: Example environment variables file.
- `requirements.txt`: List of dependencies for the project.
- `Dockerfile`: Docker configuration for containerization.

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Configure environment variables in a `.env` file based on `.env.example`.
5. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## API Endpoints

- `POST /minecraft/start`: Start the Minecraft server.
- `POST /minecraft/stop`: Stop the Minecraft server.
- `POST /minecraft/restart`: Restart the Minecraft server.
- `GET /minecraft/status`: Check the status of the Minecraft server.

- `POST /palworld/start`: Start the Palworld server.
- `POST /palworld/stop`: Stop the Palworld server.
- `POST /palworld/restart`: Restart the Palworld server.
- `GET /palworld/status`: Check the status of the Palworld server.

## License

This project is licensed under the MIT License. See the LICENSE file for details.