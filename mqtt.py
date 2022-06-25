import paho.mqtt.client as mqtt

import time

import httpx



def on_message(client, userdata, message):

	datos = str(message.payload.decode("utf-8"))

	datosConv = datos.split('#')

	data = {"temperatura": float(datosConv[0]), "humedad": float(datosConv[1]), "ubicacion": str(datosConv[2])}

	httpx.post("http://localhost:8000/agregar", json = data)

	print("Mensaje recibido: ", str(message.payload.decode("utf-8")))





mqttB = "192.168.0.156"

client = mqtt.Client("ID")

client.connect(mqttB)



client.on_message = on_message

client.subscribe("Registros")

client.loop_forever()