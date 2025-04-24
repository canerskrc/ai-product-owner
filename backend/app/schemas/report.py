from pydantic import BaseModel
from typing import Dict, List, Any

class SprintReportRequest(BaseModel):
    team_data: Dict[str, int]
    issues: List[Dict[str, Any]]
    historical_velocity: float = 0.0

class SprintReportResponse(BaseModel):
    summary: str
    raw: Dict[str, Any]
