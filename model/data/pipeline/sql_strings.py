"""
These SQL strings are used during the pipeline process, primarily by the
aggregation file.
"""

from model.data.pipeline import resources as re

CITY_MONTH_PAIRS = "SELECT city, month FROM {t} GROUP BY city, month;".format(
    t=re.IN_TABLE)

AGG_TEMPERATURE = "SELECT city, month, avg(temperature) as temperature " \
                  "FROM {t} " \
                  "WHERE phase == 'midday' " \
                  "GROUP BY city, month;".format(t=re.IN_TABLE)
