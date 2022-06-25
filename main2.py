from fastapi import FastAPI

from sqlalchemy.sql import text

from pydantic import BaseModel



import sqlalchemy as base



motor = base.create_engine('mysql+pymysql://root:MySQLTECEm$2022@127.0.0.1:3346/te_pilar_grp_1')

conexion = motor.connect()

metadata = base.MetaData()

registros = base.Table('Registros', metadata, autoload=True, autoload_with=motor)



class Registro(BaseModel):

	temperatura: float

	humedad: float

	ubicacion: str



app = FastAPI()

 

@app.post("/agregar")

async def agregar(registro: Registro):

  query = text("INSERT INTO Registros (Temperatura, Humedad, Ubicacion) VALUES (:temperatura, :humedad, :ubicacion)")

  conexion.execute(query, {"temperatura": registro.temperatura, "humedad": registro.humedad, "ubicacion": registro.ubicacion})

  return {"Temperatura": registro.temperatura, "Humedad": registro.humedad, "Ubicacion": registro.ubicacion}



@app.get("/obtenerMaxTemp")

async def maxTemp():

    query = base.select(registros).order_by(base.desc(registros.columns.Temperatura)).limit(1)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerMinTemp")

async def minTemp():

    query = base.select(registros).order_by(base.asc(registros.columns.Temperatura)).limit(1)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerMaxHumedad")

async def maxHumedad():

    query = base.select(registros).order_by(base.desc(registros.columns.Humedad)).limit(1)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerMinHumedad")

async def minHumedad():

    query = base.select(registros).order_by(base.asc(registros.columns.Humedad)).limit(1)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerMaxTemp/{cantidad}")

async def maxTempCantidad(cantidad):

    query = base.select(registros).order_by(base.desc(registros.columns.Temperatura)).limit(cantidad)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerMinTemp/{cantidad}")

async def minTempCantidad(cantidad):

    query = base.select(registros).order_by(base.asc(registros.columns.Temperatura)).limit(cantidad)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerMaxHumedad/{cantidad}")

async def maxHumedadCantidad(cantidad):

    query = base.select(registros).order_by(base.desc(registros.columns.Humedad)).limit(cantidad)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerMinHumedad/{cantidad}")

async def minHumedadCantidad(cantidad):

    query = base.select(registros).order_by(base.asc(registros.columns.Humedad)).limit(cantidad)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerTemperaturaPorUbicacion/{ubicacion}")

async def obtenerTemperaturaPorUbicacion(ubicacion):

    query = base.select(registros).where(registros.columns.Ubicacion==ubicacion).order_by(base.desc(registros.columns.Fecha)).limit(10)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()



@app.get("/obtenerHumedadPorUbicacion/{ubicacion}")

async def obtenerHumedadPorUbicacion(ubicacion):

    query = base.select(registros.columns.Humedad).where(registros.columns.Ubicacion==ubicacion).order_by(base.desc(registros.columns.Fecha)).limit(10)

    ResultProxy = conexion.execute(query)

    return ResultProxy.all()