/*
 * This file creates the lookup table for weather descriptions.
 */

CREATE TABLE WeatherDesc
(
    description               TEXT PRIMARY KEY,
    is_rain            INTEGER NOT NULL CHECK (is_rain IN (0, 1)),
    is_snow            INTEGER NOT NULL CHECK (is_snow IN (0, 1)),
    is_cloud           INTEGER NOT NULL CHECK (is_cloud IN (0, 1)),
    is_fog             INTEGER NOT NULL CHECK (is_fog IN (0, 1)),
    is_extreme_weather INTEGER NOT NULL CHECK (is_extreme_weather IN (0, 1))
);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('broken clouds', 0, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('drizzle', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('dust', 0, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('few clouds', 0, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('fog', 0, 0, 0, 1, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('freezing rain', 1, 0, 0, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('haze', 0, 0, 0, 1, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('heavy intensity drizzle', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('heavy intensity rain', 1, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('heavy intensity shower rain', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('heavy shower snow', 0, 1, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('heavy snow', 0, 1, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('heavy thunderstorm', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light intensity drizzle', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light intensity drizzle rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light intensity shower rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light rain and snow', 1, 1, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light shower sleet', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light shower snow', 0, 1, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('light snow', 0, 1, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('mist', 0, 0, 0, 1, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('moderate rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('overcast clouds', 0, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('proximity moderate rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('proximity sand/dust whirls', 1, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('proximity shower rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('proximity thunderstorm', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('proximity thunderstorm with drizzle', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('proximity thunderstorm with rain', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('ragged thunderstorm', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('sand', 0, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('sand/dust whirls', 0, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('scattered clouds', 0, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('shower drizzle', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('shower rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('shower snow', 0, 1, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('sky is clear', 0, 0, 0, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('sleet', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('smoke', 0, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('snow', 0, 1, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('squalls', 0, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('thunderstorm', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('thunderstorm with drizzle', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('thunderstorm with heavy drizzle', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('thunderstorm with heavy rain', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('thunderstorm with light drizzle', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('thunderstorm with light rain', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('thunderstorm with rain', 1, 0, 1, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('tornado', 0, 0, 0, 0, 1);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('very heavy rain', 1, 0, 1, 0, 0);

INSERT INTO WeatherDesc (description, is_rain, is_snow, is_cloud, is_fog,
                         is_extreme_weather)
VALUES ('volcanic ash', 0, 0, 0, 0, 1);

