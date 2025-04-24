from fastapi import APIRouter, HTTPException, Body
from app.services.llm_agent import generate_task_breakdown, summarize_sprint_status
from app.services.jira_client import create_jira_task

router = APIRouter()

@router.post("/tasks/generate")
async def create_task_breakdown(feature_description: str = Body(..., embed=True)):
    """
    LLM ile görev üret
    """
    try:
        tasks = await generate_task_breakdown(feature_description)
        return {"tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sprint/analyze")
async def analyze_sprint_status(jira_summary: dict = Body(...)):
    """
    LLM ile sprint analiz özeti üret
    """
    try:
        summary = await summarize_sprint_status(jira_summary)
        return {"sprint_summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/task/create")
async def create_task_in_jira(
    access_token: str = Body(...),
    project_key: str = Body(...),
    summary: str = Body(...),
    description: str = Body(...)
):
    """
    LLM'den alınan bir görevi Jira'ya yaz
    """
    try:
        issue = await create_jira_task(
            access_token=access_token,
            project_key=project_key,
            summary=summary,
            description=description
        )
        return {"jira_issue": issue}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
