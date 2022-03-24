"""
This file contains SQL statements for selecting summary data from the
USWeather table.
"""

AVG_TEMPS = 'SELECT month, phase, city, avg(temperature) as avgTemp ' \
            'FROM USWeather ' \
            'GROUP BY city, phase, month;'

AVG_HUMIDITY = 'SELECT month, phase, city, avg(humidity) as avgHumidity ' \
               'FROM USWeather ' \
               'GROUP BY city, phase, month;'

AVG_PRESSURE = 'SELECT month, phase, city, avg(pressure) as avgPressure ' \
               'FROM USWeather ' \
               'GROUP BY city, phase, month;'

WEATHER_DESC_FREQ = 'SELECT month, phase, city, ' \
                    'weather_description, count() ' \
                    'FROM USWeather ' \
                    'GROUP BY city, phase, month, weather_description;'

AVG_WIND_DIR = 'SELECT month, phase, city, avg(wind_direction) as avgWindDir ' \
               'FROM USWeather ' \
               'GROUP BY city, phase, month;'

AVG_WIND_SPEED = 'SELECT month, phase, city, avg(wind_speed) as avgWindSpeed ' \
                 'FROM USWeather ' \
                 'GROUP BY city, phase, month;'
