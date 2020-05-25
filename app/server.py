from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])

@app.get('/api/foo')
def example():
    return {'text': 'Hello World'}

