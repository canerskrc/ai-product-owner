import httpx
from app.core.config import settings

JIRA_BASE_URL = "https://api.atlassian.com"

# OAuth ile access token alındıktan sonra kullanılacak headers
def get_jira_headers(access_token: str):
    return {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

# 1. Kullanıcının site ID'sini (cloud ID) al
async def get_cloud_id(access_token: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{JIRA_BASE_URL}/oauth/token/accessible-resources",
            headers=get_jira_headers(access_token)
        )
        response.raise_for_status()
        return response.json()[0]["id"]  # İlk siteyi varsayıyoruz

# 2. Kullanıcının Jira projelerini getir
async def get_user_projects(access_token: str) -> list:
    cloud_id = await get_cloud_id(access_token)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{JIRA_BASE_URL}/ex/jira/{cloud_id}/rest/api/3/project",
            headers=get_jira_headers(access_token)
        )
        response.raise_for_status()
        return response.json()

# 3. Jira'ya yeni bir görev (issue) oluştur
async def create_jira_task(access_token: str, project_key: str, summary: str, description: str):
    cloud_id = await get_cloud_id(access_token)
    payload = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": description,
            "issuetype": {
                "name": "Task"
            }
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{JIRA_BASE_URL}/ex/jira/{cloud_id}/rest/api/3/issue",
            headers=get_jira_headers(access_token),
            json=payload
        )
        response.raise_for_status()
        return response.json()
