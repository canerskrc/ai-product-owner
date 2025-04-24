from openai import AsyncOpenAI
from app.core.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

# 1. Görev Üretici - Kullanıcıdan gelen feature isteğini parçalara ayırır
async def generate_task_breakdown(feature_description: str) -> list[str]:
    prompt = f"""
    You are an experienced software product owner.
    Please break down the following feature into technical tasks.
    Respond only with a markdown list. Feature: {feature_description}
    """
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    task_list = response.choices[0].message.content.strip().split('\n')
    return [task.strip("-* ").strip() for task in task_list if task]

# 2. Sprint Durumu Özetleyici - Jira sprint verilerini yorumlar
async def summarize_sprint_status(jira_summary: dict) -> str:
    jira_json = str(jira_summary)
    prompt = f"""
    Given the following sprint summary data, act as a product owner and write:
    - A summary of overall team performance
    - Any delays or blockers
    - Actionable suggestions for improvement
    Data: {jira_json}
    """
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()
