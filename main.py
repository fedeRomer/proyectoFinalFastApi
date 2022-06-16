import sqlalchemy

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy.ext.declarative import declarative_base

##requirement: 
# pip install 
#               PyMySQL
#               SQLAlchemy
#               fastapi
#               "uvicorn[standard]"

app = FastAPI()

#German: server USAL
#IP check discord
#Usuario check discord
#Password check discord

#User mysql: check discord
#Pass mysql: check discord

# Define the engine using MYSQL Connector/Python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USER:PASSWORD@***check discord:3306/te_pilar_grp1'
# Check Conn
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/querytest")
def run_query():

    
    
    return {print(engine.table_names())}