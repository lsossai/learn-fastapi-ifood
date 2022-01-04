from fastapi import FastAPI

from apis.base import api_router
from db.base import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get('/')
async def hello_api():
    return {'detail': 'Hello World!'}
