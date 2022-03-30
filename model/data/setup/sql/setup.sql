-- This file initializes the weather database, preparing the Cities and
-- Weather tables for data entry.

DROP TABLE IF EXISTS Cities;
DROP TABLE IF EXISTS Weather;

CREATE TABLE Cities
(
    name      TEXT PRIMARY KEY,
    country   TEXT,
    latitude  REAL,
    longitude REAL
);

CREATE TABLE Weather
(
    datetime            TIMESTAMP,
    city                TEXT NOT NULL,
    temperature         REAL,
    humidity            REAL,
    pressure            REAL,
    weather_description TEXT,
    wind_direction      REAL,
    wind_speed          REAL,
    PRIMARY KEY (dateitime, cty),
    FOREIGN KEY (city) REFERENCES Cities (name)
);
