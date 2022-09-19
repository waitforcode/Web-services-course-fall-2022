from fastapi import FastAPI
from models import Message

app = FastAPI()
fake_db_query = [{"item_name": "ITMO"},
                 {"item_name": "MFTI"},
                 {"item_name": "MSU"}]


@app.get('/')
async def root():
    return {'message': 'Hello world!'}


@app.get('/items/{item_id}')
async def read_path_param(item_id):
    return {'item_id': item_id}


@app.get('/query/')
async def read_query(skip: int = 0, limit: int = 10):
    return fake_db_query[skip: skip + limit]


@app.post('/message/')
async def create_item(message: Message):
    return message.text
