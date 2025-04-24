from fastapi import APIRouter, HTTPException, Body
from app.services.report_engine import generate_sprint_report

router = APIRouter()

@router.post("/sprint")
async def get_sprint_report(
    team_data: dict = Body(...),
    issues: list = Body(...),
    historical_velocity: float = Body(0.0)
):
    """
    AI destekli sprint performans raporu üretir.
    """
    try:
        report = await generate_sprint_report(
            team_data=team_data,
            issues=issues,
            historical_velocity=historical_velocity
        )
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
