from openai import AsyncOpenAI
from app.core.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

# Ana analiz fonksiyonu
async def generate_sprint_report(team_data: dict, issues: list[dict], historical_velocity: float = 0.0) -> dict:
    """
    Takım verilerine göre haftalık/sprint raporu üretir:
    - Sprint özeti
    - Geliştirici yük analizi
    - Anomali tespiti
    - AI önerileri
    """

    prompt = f"""
    You are an AI product owner assistant. Here is the current sprint data:
    Team Members: {team_data}
    Issues: {issues}
    Historical Velocity: {historical_velocity}

    Based on this, provide the following in markdown:
    1. Overall Sprint Performance Summary
    2. Developer-wise Task Distribution
    3. Highlight Bottlenecks or Unusual Delays
    4. Suggestions to Improve Next Sprint
    5. Estimated Team Velocity Trend
    """
    
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    
    full_report = response.choices[0].message.content.strip()
    
    return {
        "summary": full_report,
        "raw": {
            "team_data": team_data,
            "issues": issues,
            "velocity_reference": historical_velocity
        }
    }
