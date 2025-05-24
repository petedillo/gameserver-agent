# GameServer Agent

A FastAPI-based service for managing game servers. This implementation provides a RESTful API to control Minecraft and Palworld servers through systemd services.

## Features

- **Server Management**: Start, stop, restart, and check status of game servers
- **Systemd Integration**: Manages servers through systemd services
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

## Setup Instructions

### Local Development
1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Systemd Configuration
The API requires proper systemd service configurations:

1. Minecraft Server:
   - Uses `minecraft.service`

2. Palworld Server:
   - Uses `palworld.service`

### Testing
Run the test suite: