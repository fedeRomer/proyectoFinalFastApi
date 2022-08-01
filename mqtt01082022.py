

import paho.mqtt.client as mqtt



import httpx



import asyncio



from queue import Queue







queueData = Queue()







def on_message(client, userdata, message):



	datos = str(message.payload.decode("utf-8"))



	datosConv = datos.split('#')



	data = {"temperatura": float(datosConv[0]), "humedad": float(datosConv[1]), "ubicacion": str(datosConv[2])}



	queueData.put(data)



	print("Mensaje recibido: ", datos)







def on_connect(client, userdata, flags, rc):



	print("Conectado, codigo: " + str(rc))



	client.subscribe("Registros")







async def add(data):



	async with httpx.AsyncClient() as client:



		res = await client.post("http://localhost:8000/agregar", json = data)



		print(res.json())







async def main():



	mqttB = "192.168.1.39"



	client = mqtt.Client("ID")



	client.on_connect = on_connect



	client.on_message = on_message



	client.connect(mqttB)



	client.loop_start()



	



	while True:



		await add(queueData.get())



