from typing import Dict, List, Optional

class ServiceInfo:
    """Common service information structure"""
    def __init__(self, name: str, description: str, active_state: str):
        self.name = name
        self.description = description
        self.active_state = active_state

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "description": f"{self.name} Server Docker Compose Service",
            "active_state": self.active_state
        }

def get_basic_service_info(service_name: str, active_state: str = "inactive") -> ServiceInfo:
    """Get basic service information"""
    return ServiceInfo(
        name=service_name.capitalize(),
        description=f"{service_name.capitalize()} Server Docker Compose Service",
        active_state=active_state
    )
