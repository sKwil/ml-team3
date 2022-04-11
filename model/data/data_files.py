import os.path
import model.data.resources as re

ALL_STATIONS = os.path.join(re.DATA_RAW_DIR, 'stations', 'allstations.txt')

__PRODUCTS_DIR = os.path.join(re.DATA_RAW_DIR, 'products')

PRECIPITATION_DIR = os.path.join(__PRODUCTS_DIR, 'precipitation')

TEMPERATURE_DIR = os.path.join(__PRODUCTS_DIR, 'temperature')
