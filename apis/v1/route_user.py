from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.users import create_new_user
from db.session import get_db
from schemas.users import ShowUser, UserCreate

router = APIRouter()


@router.post('/create-user', response_model=ShowUser)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user
