/*
This file runs after loading the csv data into the Cities and Weather tables.
It creates views for more easily accessing often used data.
 */

-- First, replace blank cells with null in the Weather table
UPDATE Weather
SET temperature         = nullif(temperature, ''),
    humidity            = nullif(humidity, ''),
    pressure            = nullif(pressure, ''),
    weather_description = nullif(weather_description, ''),
    wind_direction      = nullif(wind_direction, ''),
    wind_speed          = nullif(wind_speed, '');


-- Create a view with all the information for all cities
CREATE VIEW DataAll AS
SELECT W.datetime,
       W.city,
       C.country,
       C.latitude,
       C.longitude,
       W.temperature,
       W.humidity,
       W.pressure,
       W.weather_description,
       W.wind_direction,
       W.wind_speed
FROM Weather as W
         LEFT JOIN Cities C on C.name = W.city;

-- Create a view for US data with null entries removed
CREATE VIEW USWeather AS
SELECT * FROM DataAll
WHERE country = 'United States' AND
      temperature IS NOT NULL AND
      humidity IS NOT NULL AND
      pressure IS NOT NULL AND
      weather_description IS NOT NULL AND
      wind_direction IS NOT NULL AND
      wind_speed IS NOT NULL;
