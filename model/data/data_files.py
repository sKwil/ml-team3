import os.path
import model.data.resources as re

ALL_STATIONS = os.path.join(re.DATA_RAW_DIR, 'stations', 'allstations.txt')

__PRODUCTS_DIR = os.path.join(re.DATA_RAW_DIR, 'products')

__PRECIPITATION_DIR = os.path.join(__PRODUCTS_DIR, 'precipitation')

MLY_PRCP_MEDIANS = os.path.join(__PRECIPITATION_DIR,
                                'mly-prcp-50pctl.txt')

MLY_PRCP_DAYS_AVG_HUNDREDTHS = os.path.join(__PRECIPITATION_DIR,
                                            'mly-prcp-avgnds-ge001hi.txt')

MLY_PRCP_DAYS_AVG_TENTHS = os.path.join(__PRECIPITATION_DIR,
                                        'mly-prcp-avgnds-ge010hi.txt')

MLY_PRCP_NORMALS = os.path.join(__PRECIPITATION_DIR,
                                'mly-prcp-normal.txt')

MLY_SNOW_MEDIANS = os.path.join(__PRECIPITATION_DIR,
                                'mly-snow-50pctl.txt')

MLY_SNOW_AVG_DAYS_FALL_TENTHS = os.path.join(__PRECIPITATION_DIR,
                                             'mly-snow-avgnds-ge001ti.txt')

MLY_SNOW_AVG_DAYS_FALL_INCHES = os.path.join(__PRECIPITATION_DIR,
                                             'mly-snow-avgnds-ge010ti.txt')

MLY_SNOW_NORMALS = os.path.join(__PRECIPITATION_DIR,
                                'mly-snow-normal.txt')

MLY_SNOW_AVG_DAYS_DEPTH_TENTHS = os.path.join(__PRECIPITATION_DIR,
                                              'mly-snow-avgnds-ge001wi.txt')
