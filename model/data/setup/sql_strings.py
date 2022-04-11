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
