from fastapi import FastAPI



from pydantic import BaseModel



import databases



import sqlalchemy as sqlAlch



import datetime







url = 'mysql+aiomysql://root:MySQLTECEm$2022@127.0.0.1:3346/te_pilar_grp_1'



baseDatos = databases.Database(url)



metadata = sqlAlch.MetaData()



registros = sqlAlch.Table('Registros', metadata, sqlAlch.Column("idRegistros", sqlAlch.Integer, primary_key=True), sqlAlch.Column("Temperatura", sqlAlch.Float), sqlAlch.Column("Humedad", sqlAlch.Float), sqlAlch.Column("Fecha", sqlAlch.DateTime), sqlAlch.Column("Ubicacion", sqlAlch.String))











class Registro(BaseModel):



	temperatura: float



	humedad: float



	ubicacion: str







app = FastAPI()







@app.on_event("startup")



async def startup():



    await baseDatos.connect()







@app.on_event("shutdown")



async def shutdown():



    await baseDatos.disconnect()



 



@app.post("/agregar")



async def agregar(registro: Registro):



    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



    query = registros.insert().values(Temperatura = registro.temperatura, Humedad = registro.humedad, Fecha = fecha, Ubicacion = registro.ubicacion)



    id = await baseDatos.execute(query)



    return {"idRegistro": id, **registro.dict(), "Fecha": fecha}







@app.get("/obtenerMaxTemp")



async def maxTemp():



    query = registros.select().order_by(sqlAlch.desc(registros.columns.Temperatura)).limit(1)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerMinTemp")



async def minTemp():



    query = registros.select().order_by(sqlAlch.asc(registros.columns.Temperatura)).limit(1)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerMaxHumedad")



async def maxHumedad():



    query = registros.select().order_by(sqlAlch.desc(registros.columns.Humedad)).limit(1)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerMinHumedad")



async def minHumedad():



    query = registros.select().order_by(sqlAlch.asc(registros.columns.Humedad)).limit(1)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerMaxTemp/{cantidad}")



async def maxTempCantidad(cantidad):



    query = registros.select().order_by(sqlAlch.desc(registros.columns.Temperatura)).limit(cantidad)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerMinTemp/{cantidad}")



async def minTempCantidad(cantidad):



    query = registros.select().order_by(sqlAlch.asc(registros.columns.Temperatura)).limit(cantidad)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerMaxHumedad/{cantidad}")



async def maxHumedadCantidad(cantidad):



    query = registros.select().order_by(sqlAlch.desc(registros.columns.Humedad)).limit(cantidad)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerMinHumedad/{cantidad}")



async def minHumedadCantidad(cantidad):



    #query = sqlAlch.select(registros.columns.Humedad).order_by(sqlAlch.asc(registros.columns.Humedad)).limit(cantidad) Para devolver solamente el valor de humedad.



    query = registros.select().order_by(sqlAlch.asc(registros.columns.Humedad)).limit(cantidad)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerTemperaturaPorUbicacion/{ubicacion}")



async def obtenerTemperaturaPorUbicacion(ubicacion):



    query = registros.select().where(registros.columns.Ubicacion==ubicacion).order_by(sqlAlch.desc(registros.columns.Fecha)).limit(10)



    return await baseDatos.fetch_all(query)







@app.get("/obtenerHumedadPorUbicacion/{ubicacion}")



async def obtenerHumedadPorUbicacion(ubicacion):



    query = registros.select().where(registros.columns.Ubicacion==ubicacion).order_by(sqlAlch.desc(registros.columns.Fecha)).limit(10)



    return await baseDatos.fetch_all(query)

