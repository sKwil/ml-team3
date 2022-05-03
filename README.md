# Location Prediction with ML
### ml-team3

**Authors:** Trenton Metcalfe, Sean Maher, Simon Kwilinski, Jermaine Presbery

## Contents

- readme.md - this file  
- .ebextensions - contains configuration directory for elastic beanstalk
- data - contains all the data
- jupyter - contains all model and pipeline testing
- model - creates the database to be used for the models
- website - contains all the code for creating the website with the model
- requirements.txt - has all of the python requirements for the project
		 
## Functionality
    
This site was made as a destination finder. A user is able to input the time of year and their preferred weather
specifications and the model will suggest locations for the user to go to that match these specifications. The model
does this by using a Voting classifier compiled of a handful of different models all optimized for this task. The models
are trained on a large weather dataset that includes specific locations, temperature, time of year, time of day, and other
more specific weather features (pressure, humidity, precipitation, etc.).

## Finding a Dataset

This project started when we downloaded a [dataset](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data?select=humidity.csv) of historical weather data from 2012-2017 from kaggle. The data contained many useful features, including humidity, pressure, temperature, a weather description, the wind direction, and the wind speed. Each feature was recorded for around 30 cities, most of which were in the U.S., and the data was very clean.

We began working with this data, creating a project framework to transfer the data from raw `csv` files to a SQLite database file. From there, we manipulated and aggregated the data through SQL and then began training machine learning models on it.

Unfortunately, our models consistently had low accuracy. Even though the dataset contained hourly data for each of the cities across five years, the goal of our project required aggregating all of that data by month. In the end, we had far fewer observations than expected, with one row for each month-city pair for a total of around 350 rows. Since we couldn't easily obtain more data in the same format, we elected to switch datasets.

After trying unsuccessfully to make use of some weather APIs, we found a freely available [dataset from the NOAA](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00822) with U.S. monthly climate normals from 1981 to 2010. This dataset contains thousands of stations, with weather data measured over a 30 year period. All together, this was vastly more data than the previous dataset.

Unfortunately, this data was much harder to use. It is stored in `txt` files that require thorough reading of the documentation files to understand. Eventually, though, we were able to create Python functions to parse this data and load it into the SQLite database as before. With this data, the loading process went from a couple seconds to around five minutes running locally on a machine.
