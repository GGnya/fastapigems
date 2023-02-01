from local_settings.local_settings import postgres as settings
from sqlmodel import create_engine, Session
# from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, create_database

def get_engine(user: str, password: str, host: int, port: int, db: str):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, pool_size=50, echo=True)
    return engine


def get_engine_from_settings():
    keys = ['user', 'password', 'host', 'port', 'database']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')

    return get_engine(settings['user'],
                      settings['password'],
                      settings['host'],
                      settings['port'],
                      settings['database'])


def get_session():
    engine = get_engine_from_settings()
    session = Session(bind=engine)
    return session
