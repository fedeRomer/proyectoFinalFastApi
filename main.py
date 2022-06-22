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

##
""" Consigna para tener resuelta para la semana que viene

Incorporar registro temporal de las lecturas y ubicación

Desarrollar los siguientes métodos para la API TEMP

Método max_temp: devuelte el valor máximo de temperatura

Método max_hum: devuelve el valor máximo de humedad

Método min_temp: devuelte el valor mínimo de temperatura

Método min_hum: devuelve el valor mínimo de humedad

Método temp_max_by_qty: devuele la cantidad de registros de temperatura máximas solicitados

Método hum_max_by_qty: devuele la cantidad de registros de humedad máximas solicitados

Método temp_min_by_qty: devuele la cantidad de registros de temperatura mínimas solicitados

Método hum_min_by_qty: devuele la cantidad de registros de humedad mínimas solicitados

Método temp_by_location: devuelve los últimos 10 registros de temperatura de la ubicación especificada

Método hum_by_location: devuelve los últimos 10 registros de humedad de la ubicación especificada
 """

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/querytest")
def run_query():

    
    
    return {print(engine.table_names())}

@app.post("/saveTemperature")
def save(temperature):

    
    return{"temperature": temperature}