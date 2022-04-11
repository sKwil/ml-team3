CLEAR_STATIONS_TABLE = 'DELETE FROM Stations;'

CLEAR_WEATHER_TABLE = 'DELETE FROM Weather WHERE TRUE;'

ADD_STATION = 'INSERT INTO Stations (id, latitude, longitude, elevation, ' \
              'state, name, gsn_flag, hcn_flag, wmo_id) ' \
              'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'

ADD_WEATHER_TEMPERATURE = 'INSERT INTO Weather (datetime, city, temperature) ' \
                          'VALUES (?,?,?);'

UPDATE_WEATHER_HUMIDITY = 'UPDATE Weather ' \
                          'SET humidity = ? ' \
                          'WHERE datetime = ? AND ' \
                          'city = ?;'

ADD_WEATHER_DATA = 'INSERT INTO Weather ' \
                   '(datetime, city, temperature, humidity, pressure, ' \
                   'weather_description, wind_direction, wind_speed) ' \
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?);'

ADD_PRECIPITATION_MEDIAN = 'INSERT INTO MonthlyPrecipitationMedians ' \
                           '(id, month, inches, flag) VALUES (?, ?, ?, ?);'

ADD_PRECIPITATION_DAYS_H = 'INSERT INTO MonthlyPrecipitationDaysH ' \
                           '(id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_PRECIPITATION_DAYS_T = 'INSERT INTO MonthlyPrecipitationDaysT ' \
                           '(id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_PRECIPITATION_NORMALS = 'INSERT INTO MonthlyPrecipitationNormals ' \
                            '(id, month, normal, flag) VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_MEDIAN = 'INSERT INTO MonthlySnowfallMedians ' \
                      '(id, month, inches, flag) VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_DAYS_T = 'INSERT INTO MonthlySnowfallDaysT ' \
                      '(id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_DAYS_I = 'INSERT INTO MonthlySnowfallDaysI ' \
                      '(id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_SNOW_DEPTH_DAYS = 'INSERT INTO MonthlySnowDepthDays ' \
                      '(id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_NORMALS = 'INSERT INTO MonthlySnowfallNormals ' \
                       '(id, month, normal, flag) VALUES (?, ?, ?, ?);'
