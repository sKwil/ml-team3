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
                            '(station_id, month, inches, flag) ' \
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
                       '(station_id, month, inches, flag) VALUES (?, ?, ?, ?);'

ADD_TEMP_MAX_NORMAL = 'INSERT INTO MonthlyTempMaxNormals ' \
                      '(station_id, month, normal_temp, flag) ' \
                      'VALUES (?, ?, ?, ?);'

ADD_TEMP_MAX_STDEV = 'INSERT INTO MonthlyTempMaxStdev ' \
                     '(station_id, month, stdev, flag) VALUES (?, ?, ?, ?);'

ADD_TEMP_MIN_NORMAL = 'INSERT INTO MonthlyTempMinNormals ' \
                      '(station_id, month, normal_temp, flag) ' \
                      'VALUES (?, ?, ?, ?);'

ADD_TEMP_MIN_STDEV = 'INSERT INTO MonthlyTempMinStdev ' \
                     '(station_id, month, stdev, flag) VALUES (?, ?, ?, ?);'

ADD_CLOUD_BROKEN = 'INSERT INTO HourlyCloudsBroken ' \
                   '(station_id, month, day, hour, percentage, flag) ' \
                   'VALUES (?, ?, ?, ?, ?, ?);'

ADD_CLOUD_CLEAR = 'INSERT INTO HourlyCloudsClear ' \
                  '(station_id, month, day, hour, percentage, flag) ' \
                  'VALUES (?, ?, ?, ?, ?, ?);'

ADD_CLOUD_FEW = 'INSERT INTO HourlyCloudsFew ' \
                '(station_id, month, day, hour, percentage, flag) ' \
                'VALUES (?, ?, ?, ?, ?, ?);'

ADD_CLOUD_OVERCAST = 'INSERT INTO HourlyCloudsOvercast ' \
                     '(station_id, month, day, hour, percentage, flag) ' \
                     'VALUES (?, ?, ?, ?, ?, ?);'

ADD_CLOUD_SCATTERED = 'INSERT INTO HourlyCloudsScattered ' \
                      '(station_id, month, day, hour, percentage, flag) ' \
                      'VALUES (?, ?, ?, ?, ?, ?);'

ADD_DEW_POINT_NORMAL = 'INSERT INTO HourlyDewPointNormal ' \
                       '(station_id, month, day, hour, dew_point, flag) ' \
                       'VALUES (?, ?, ?, ?, ?, ?);'

ADD_HEAT_INDEX_NORMAL = 'INSERT INTO HourlyHeadIndexNormal ' \
                        '(station_id, month, day, hour, heat_index, flag) ' \
                        'VALUES (?, ?, ?, ?, ?, ?);'

ADD_PRESSURE_NORMAL = 'INSERT INTO HourlyPressureNormal ' \
                      '(station_id, month, day, hour, pressure, flag) ' \
                      'VALUES (?, ?, ?, ?, ?, ?);'

ADD_AVG_WIND_SPEED = 'INSERT INTO HourlyWindSpeedAvg ' \
                     '(station_id, month, day, hour, wind_speed, flag) ' \
                     'VALUES (?, ?, ?, ?, ?, ?);'

ADD_WIND_PERCENT_CALM = 'INSERT INTO HourlyPercentCalm ' \
                        '(station_id, month, day, hour, percentage, flag) ' \
                        'VALUES (?, ?, ?, ?, ?, ?);'
