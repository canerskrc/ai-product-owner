from fastapi import APIRouter, Depends, HTTPException, Body
from app.schemas.user import UserLogin, UserOut
from app.utils.token import create_access_token, verify_token
from app.models.user import User
from app.database.session import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

# DB bağımlılığı
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=UserOut)
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Kullanıcı adı ve şifre ile login → JWT üret
    """
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.username})
    return {"username": db_user.username, "token": token}

@router.get("/me")
def read_user_data(token: str = Depends(verify_token)):
    """
    Token ile kimlik doğrulama örneği
    """
    return {"message": f"Hoş geldin {token['sub']}"}
