import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings
from app.database.database import Base, get_db
from app.main import app

# Test veritabanı URL'si
TEST_DATABASE_URL = "sqlite:///./test.db"

# Test veritabanı engine'i
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Test session factory
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Test veritabanı session'ı oluşturur."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    """Test client'ı oluşturur."""
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def test_user(db_session):
    """Test kullanıcısı oluşturur."""
    from app.models.user import User
    user = User(
        email="test@example.com",
        hashed_password="hashed_password",
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture(scope="function")
def test_project(db_session, test_user):
    """Test projesi oluşturur."""
    from app.models.project import Project
    project = Project(
        name="Test Project",
        description="Test Project Description",
        owner_id=test_user.id
    )
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    return project

@pytest.fixture(scope="function")
def test_sprint(db_session, test_project):
    """Test sprint'i oluşturur."""
    from app.models.sprint import Sprint
    sprint = Sprint(
        name="Test Sprint",
        start_date="2024-01-01",
        end_date="2024-01-14",
        project_id=test_project.id
    )
    db_session.add(sprint)
    db_session.commit()
    db_session.refresh(sprint)
    return sprint

@pytest.fixture(scope="function")
def test_task(db_session, test_sprint):
    """Test task'ı oluşturur."""
    from app.models.task import Task
    task = Task(
        title="Test Task",
        description="Test Task Description",
        story_points=5,
        sprint_id=test_sprint.id
    )
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    return task
