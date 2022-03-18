CLEAR_CITIES_TABLE = 'DELETE FROM Cities WHERE TRUE;'

CLEAR_WEATHER_TABLE = 'DELETE FROM Weather WHERE TRUE;'

ADD_CITY = 'INSERT INTO Cities (name, country, latitude, longitude) ' \
           'VALUES (?,?,?,?);'


ADD_WEATHER_TEMPERATURE = 'INSERT INTO Weather (datetime, city, temperature) ' \
                          'VALUES (?,?,?);'
