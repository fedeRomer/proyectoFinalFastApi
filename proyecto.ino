#include <Ethernet.h>
#include <PubSubClient.h>
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

byte mac[] = { 0xDE, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA };

IPAddress ip(192, 168, 0, 157);
IPAddress mqttS(192, 168, 0, 156);

const char* nombreTopico = "Registros";

EthernetClient ethernetCliente;
PubSubClient pubClient(ethernetCliente);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Ethernet.begin(mac, ip);
  pubClient.setServer(mqttS, 1883);
}

void loop() {
  if (!(pubClient.connected())) {
    pubClient.connect("Cliente");
  } else {
    float temperatura = dht.readTemperature();
    float humedad = dht.readHumidity();

    if (isnan(temperatura) || isnan(humedad)) {
      return;
    }

    String reg = String(temperatura) + "#" + String(humedad) + "#" + "Pilar";

    char arrayChar[reg.length() + 1];

    reg.toCharArray(arrayChar, reg.length() + 1);

    pubClient.publish(nombreTopico, arrayChar);
  }

  delay(5000);
}
