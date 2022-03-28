"""
These SQL strings are used during the pipeline process, primarily by the
aggregation file.
"""

from model.data.pipeline import resources as re

AGG_INDICES = "SELECT city, year, month FROM {t} " \
              "GROUP BY city, year, month;".format(t=re.IN_TABLE)

AGG_TEMPERATURE = "SELECT city, year, month, avg(temperature) as temperature " \
                  "FROM {t} " \
                  "WHERE phase == 'midday' " \
                  "GROUP BY city, year, month;".format(t=re.IN_TABLE)

AGG_HUMIDITY = "SELECT city, year, month, avg(humidity) as humidity " \
               "FROM {t} " \
               "WHERE phase == 'midday' " \
               "GROUP BY city, year, month;".format(t=re.IN_TABLE)

AGG_PRESSURE = "SELECT city, year, month, avg(pressure) as pressure " \
               "FROM {t} " \
               "WHERE phase == 'midday' " \
               "GROUP BY city, year, month;".format(t=re.IN_TABLE)

AGG_WIND_SPEED = "SELECT city, year, month, avg(wind_speed) as wind_speed " \
                 "FROM {t} " \
                 "WHERE phase == 'midday' " \
                 "GROUP BY city, year, month;".format(t=re.IN_TABLE)

AGG_WEATHER_DESCRIPTION = 'SELECT city, year, month, ' \
                          '1.0 * sum(W.is_rain) / count() as rain, ' \
                          '1.0 * sum(W.is_snow) / count() as snow, ' \
                          '1.0 * sum(W.is_cloud) / count() as cloud, ' \
                          '1.0 * sum(W.is_fog) / count() as fog, ' \
                          '1.0 * sum(W.is_extreme_weather) / count() ' \
                          'as extreme_weather ' \
                          'FROM {t} ' \
                          'LEFT JOIN WeatherDesc W on ' \
                          'weather_description == W.description ' \
                          'GROUP BY city, year, month;'.format(t=re.IN_TABLE)
