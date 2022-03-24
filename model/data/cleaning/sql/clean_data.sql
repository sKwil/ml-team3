/*
 * This script replaces blank cells with null in the Weather table
 */

UPDATE Weather
SET temperature         = nullif(temperature, ''),
    humidity            = nullif(humidity, ''),
    pressure            = nullif(pressure, ''),
    weather_description = nullif(weather_description, ''),
    wind_direction      = nullif(wind_direction, ''),
    wind_speed          = nullif(wind_speed, '');