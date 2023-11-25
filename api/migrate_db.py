from sqlalchemy import create_engine

import api.const as const
from api.models.task import Base

DB_URL = f"mysql+pymysql://{const.USER}:{const.PASSWORD}@{const.HOST}:{const.PORT}/{const.DB}?charset=utf8mb4"

engine = create_engine(DB_URL, echo=True)


def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    reset_db()
