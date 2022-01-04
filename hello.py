from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello_api():
    return {'detail': 'Hello World!'}
