from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])

@app.get('/api/foo')
def example():
    return {'text': f'Hello World and utc now is {datetime.utcnow()}'}

