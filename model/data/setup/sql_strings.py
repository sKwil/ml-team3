CLEAR_CITIES_TABLE = 'DELETE FROM Cities WHERE TRUE;'

CLEAR_WEATHER_TABLE = 'DELETE FROM Weather WHERE TRUE;'

ADD_CITY = 'INSERT INTO Cities (name, country, latitude, longitude) ' \
           'VALUES (?,?,?,?);'

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
