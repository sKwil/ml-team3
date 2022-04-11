CLEAR_STATIONS_TABLE = 'DELETE FROM Stations;'

CLEAR_WEATHER_TABLE = 'DELETE FROM Weather WHERE TRUE;'

ADD_STATION = 'INSERT INTO Stations (id, latitude, longitude, elevation, ' \
              'state, name, gsn_flag, hcn_flag, wmo_id) ' \
              'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'

ADD_PRECIPITATION_MEDIAN = 'INSERT INTO MonthlyPrecipitationMedians ' \
                           '(station_id, month, inches, flag) ' \
                           'VALUES (?, ?, ?, ?);'

ADD_PRECIPITATION_DAYS_H = 'INSERT INTO MonthlyPrecipitationDaysH ' \
                           '(station_id, month, days, flag) ' \
                           'VALUES (?, ?, ?, ?);'

ADD_PRECIPITATION_DAYS_T = 'INSERT INTO MonthlyPrecipitationDaysT ' \
                           '(station_id, month, days, flag) ' \
                           'VALUES (?, ?, ?, ?);'

ADD_PRECIPITATION_NORMALS = 'INSERT INTO MonthlyPrecipitationNormals ' \
                            '(station_id, month, normal, flag) ' \
                            'VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_MEDIAN = 'INSERT INTO MonthlySnowfallMedians ' \
                      '(station_id, month, inches, flag) VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_DAYS_T = 'INSERT INTO MonthlySnowfallDaysT ' \
                      '(station_id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_DAYS_I = 'INSERT INTO MonthlySnowfallDaysI ' \
                      '(station_id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_SNOW_DEPTH_DAYS = 'INSERT INTO MonthlySnowDepthDays ' \
                      '(station_id, month, days, flag) VALUES (?, ?, ?, ?);'

ADD_SNOWFALL_NORMALS = 'INSERT INTO MonthlySnowfallNormals ' \
                       '(station_id, month, normal, flag) VALUES (?, ?, ?, ?);'

ADD_TEMP_MAX_NORMAL = 'INSERT INTO MonthlyTempMaxNormals ' \
                      '(station_id, month, normal, flag) VALUES (?, ?, ?, ?);'

ADD_TEMP_MAX_STDEV = 'INSERT INTO MonthlyTempMaxStdev ' \
                     '(station_id, month, stdev, flag) VALUES (?, ?, ?, ?);'

ADD_TEMP_MIN_NORMAL = 'INSERT INTO MonthlyTempMinNormals ' \
                      '(station_id, month, normal, flag) VALUES (?, ?, ?, ?);'

ADD_TEMP_MIN_STDEV = 'INSERT INTO MonthlyTempMinStdev ' \
                     '(station_id, month, stdev, flag) VALUES (?, ?, ?, ?);'
