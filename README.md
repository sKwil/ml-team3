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

## Authors

Each member of the group contributed separate but related work towards the final project:

**Simon Kwilinski**
- Organizing GitHub, managing branches, and setting up group members
- Establishing cohesive project structure and Python modules
- Creating initial Flask framework and organizing webpage
- Locating and downloading dataset
- Creating SQLite database and manipulating raw data
- Finalizing ML pipeline to load, clean, scale, train, and save the final model
- Writing this README

**Trenton Metcalfe**
- Researching dataset and reading documentation
- Selecting best model features and adding additional features
- Training and managing suite of ML models
- Identifying hyperparameters for final model

**Sean Maher**
- Training select models
- Finalizing Flask website
- Adding group member resumes to individual webpages

**Jermaine Presbery**
- Working on Flask website
- Refactoring website structure

## Finding a Dataset

This project started when we downloaded a [dataset](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data?select=humidity.csv) of historical weather data from 2012-2017 from kaggle. The data contained many useful features, including humidity, pressure, temperature, a weather description, the wind direction, and the wind speed. Each feature was recorded for around 30 cities, most of which were in the U.S., and the data was very clean.

We began working with this data, creating a project framework to transfer the data from raw `csv` files to a SQLite database file. From there, we manipulated and aggregated the data through SQL and then began training machine learning models on it.

Unfortunately, our models consistently had low accuracy. Even though the dataset contained hourly data for each of the cities across five years, the goal of our project required aggregating all of that data by month. In the end, we had far fewer observations than expected, with one row for each month-city pair for a total of around 350 rows. Since we couldn't easily obtain more data in the same format, we elected to switch datasets.

After trying unsuccessfully to make use of some weather APIs, we found a freely available [dataset from the NOAA](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00822) with U.S. monthly climate normals from 1981 to 2010. This dataset contains thousands of stations, with weather data measured over a 30 year period. All together, this was vastly more data than the previous dataset.

Unfortunately, this data was much harder to use. It is stored in `txt` files that require thorough reading of the documentation files to understand. Eventually, though, we were able to create Python functions to parse this data and load it into the SQLite database as before. With this data, the loading process went from a couple seconds to around five minutes running locally on a machine.

## Data Processing

The raw data we used for this project came from a database of `txt` files measuring weather data for many stations across the U.S. It is stored efficiently, but is not in a format conducive to training machine learning models. The first step in this project was to find a method for cleaning the data.

Studying the documentation files for this dataset showed us a breakdown of each symbol in the data files. It explained what each column contained, and what characters positions were assigned to each column. Additionally, it allowed us to dramatically filter down the dataset as we removed unnecessary files for our project. We rewrote the old installation functions to laod this new data, and created extensiev SQL scripts to manipulate it and get it in a format that would allow us to easily access it later.

This process did not involve any direct machine learning. Instead, it consisted of learning SQLite syntax to organize an efficient SQL database that could handle the data. Most of the work at this stage went into database management, ensuring that everyone in the group would be able to access and utilize the data in the SQL format.

We also experimented with adding additional tables and features in this stage. We wanted to create a robust model of foreign and private keys in the database, and this required writing SQL statements to manually populate tables of U.S. states, regions, and flags for weather data. That way, columns in the final weather data table could have foreign key constraints pointing to other tables, which allowed us to ensure data integrity and easily run SQL joins in our queries. In addition to creating tables for keys, we also created entirely new features, somewhat unrelated to weather, that are based on U.S. geography. We added ocean and mountain proximity data at a state-by-state granularity, allowing us to ask the end user for mountain and ocean preference. Though not directly related to weather, these features are helpful for the vacation model, and they serve to improve the accuracy of our models.

## Model Training

We trained an extensive variety of ML models on our data. We ran numerous grid searches to find the most optimal hyperparameters for each model. In the end, processing time proved the only constraint on our ability to train a wide breadth of models. We pursued a variety of models rather than refining specific ones as we sought it best to faimilarize ourselves with the scope of ML tools at our disposal for a beginning project.

Since we were largely constrained by time, we were unable to make highly refined models with high accuracy. Hiccups in the data processing phase, a short project timeframe, and finite computer processing capabilities meant that the depth of model research was unfortunately limited. However, we spent considerable time organizing an efficient project and database structure such that we could easily train additional models in the future in pursuit of ideal models and hyperparameters.

We added a product Python module to the model code, which contains a refined pipeline for training the final machine learning model. This pipeline loads the newest data from the SQLite database, runs extensive data cleaning on it to remove and replace null and invalid data points, divides the data into separate training and testing datasets, scales the training data so that it will conform to the standards expected by the ML models, trains a model using preprogrammed hyperparmeters selected during the research phase, and finally saves the state of the trained model to a pickle file in the data directory.

In the future, we can use this pickle file to quickly import and read the models with its fully trained parameters. From there, we can easily make predictions for incoming data and test our model's accuracy against testing data.
