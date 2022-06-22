create database arduinoLogger;

USE arduinoLogger;

CREATE TABLE Temperature (
    id int,
    temperatureValue float(10,7),
  	location varchar(256)
);

CREATE TABLE Humidity (
    id int,
    humidityValue float(10,7),
  	location varchar(256)
);
