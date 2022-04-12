"""
These SQL strings are used during the pipeline process, primarily by the
aggregation file.
"""

from model.data.pipeline import resources as re

GET_MONTHLY_DATA = 'SELECT * From MonthlyData;'
