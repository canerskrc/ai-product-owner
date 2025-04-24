#  AI Product Owner Agent

An autonomous AI agent that integrates with Jira and acts like a real Product Owner:
- Creates technical tasks from plain feature requests
- Analyzes sprint progress and developer load
- Posts smart, daily, and sprint-end reports

Built with **FastAPI** + **Streamlit** + **OpenAI** + **Jira API** + **Docker Compose** 💼

---

##  Features

| Module | Description |
|--------|-------------|
|  Task Breakdown | Converts feature descriptions into Jira-ready tasks using GPT-4 |
|  Sprint Reporter | AI-analyzes sprint data for bottlenecks, progress & team insights |
|  Jira Integration | Auth, project fetch, and issue creation via OAuth2 |
|  Streamlit UI | Investor-ready professional agent interface |
|  Redis Enabled | Async caching and queue-ready agent structure |

---

##  Quick Start (Docker Compose)

### 1. Clone the repository
```bash
git clone https://github.com/canerskrc/ai-product-owner.git
cd ai-product-owner
```

### 2. Add your environment variables
Create a `.env` file in root:
```env
OPENAI_API_KEY=your-openai-key
DATABASE_URL=postgresql://user:pass@db/dbname
REDIS_HOST=redis
REDIS_PORT=6379
JIRA_CLIENT_ID=...
JIRA_CLIENT_SECRET=...
JIRA_REDIRECT_URI=http://localhost:8000/jira/callback
```

### 3. Build and start the stack
```bash
docker-compose up --build
```

### 4. Access the app
- **Backend (FastAPI):** http://localhost:8000/docs
- **Frontend (Streamlit):** http://localhost:8501

---

##  How It Works

### 1. Feature → Task Breakdown
```json
{
  "feature_description": "Add email notifications"
}
```
⟶ Returns:
```json
{
  "tasks": ["Design notification schema", "Integrate with SendGrid", ...]
}
```

### 2. Sprint Analyzer
```json
{
  "team_data": {"ahmet": 4, "murat": 2},
  "issues": [ {"title": "Bug fix", "status": "done", "assignee": "murat"} ]
}
```
⟶ Returns: AI-written performance summary.

---

## 📁 Project Structure

```
project-root/
├── backend/
│   ├── app/        # FastAPI application
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app.py      # Streamlit UI
│   ├── .streamlit/config.toml
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── .env
└── README.md
```

---

##  Testing
```bash
cd backend
pytest
```

---

##  Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) 
- [OpenAI GPT-4](https://platform.openai.com/docs)
- [Jira REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Streamlit](https://streamlit.io/) UI
- [Docker Compose](https://docs.docker.com/compose/) 📦
- [Redis](https://redis.io/) for caching & task pub/sub

---

##  Ideal Use Cases
- Agile Product Teams with complex roadmaps
- AI-augmented Project Management
- Investor / Demo-ready AI prototypes

---

##  Contact / License
**Authors**: Caner Sekerci / Atıl Samancıoglu  
**Contact**: [LinkedIn] ( https://www.linkedin.com/in/canersekerci/ )
