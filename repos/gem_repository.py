from models.gem_models import Gem, GemProperties
from sqlmodel import Session, select

from utils.db_utils import get_engine_from_settings

engine = get_engine_from_settings()

def select_all_gem():
    with Session(engine) as session:
        statement = select(Gem, GemProperties).join(GemProperties)
        # statement = statement.where(Gem.id == 2)
        result = session.exec(statement)
        res = []
        for gem, props in result:
            res.append({'gem': gem, 'props': props})
        return res


def select_gem(id):
    with Session(engine) as session:
        statement = select(Gem, GemProperties).join(GemProperties)
        statement = statement.where(Gem.id == id)
        result = session.exec(statement)

        return result.first()

