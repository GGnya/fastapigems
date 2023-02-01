from sqlmodel import select

from models.user_models import User
from utils.db_utils import get_session


def select_all_users():
    with get_session() as session:
        statement = select(User)
        res = session.exec(statement).all()
        return res

def find_user(name):
    with get_session() as session:
        statement = select(User).where(User.username == name)
        return session.exec(statement).first()
