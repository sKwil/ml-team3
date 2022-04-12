/*
 * This file initializes the weather database, where all the raw data will be
 * transferred ands stored.
 */

-- Drop the tables in case they already exist somehow
DROP TABLE IF EXISTS Stations;
DROP TABLE IF EXISTS MonthlyPrecipitationMedians;
DROP TABLE IF EXISTS MonthlyPrecipitationDaysH;
DROP TABLE IF EXISTS MonthlyPrecipitationDaysT;
DROP TABLE IF EXISTS MonthlyPrecipitationNormals;
DROP TABLE IF EXISTS MonthlySnowfallMedians;
DROP TABLE IF EXISTS MonthlySnowfallDaysT;
DROP TABLE IF EXISTS MonthlySnowfallDaysI;
DROP TABLE IF EXISTS MonthlySnowfallNormals;
DROP TABLE IF EXISTS MonthlySnowDepthDays;
DROP TABLE IF EXISTS MonthlyTempMaxNormals;
DROP TABLE IF EXISTS MonthlyTempMaxStdev;
DROP TABLE IF EXISTS MonthlyTempMinNormals;
DROP TABLE IF EXISTS MonthlyTempMinStdev;
DROP TABLE IF EXISTS MonthlyDataRaw;
DROP TABLE IF EXISTS Months;

/*
 * The Stations table stores the data from stations/allstations.txt. This is
 * a list of every station that may appear in the weather data somewhere,
 * primary used for lookups.
 */
CREATE TABLE Stations
(
    id        VARCHAR(11) PRIMARY KEY,
    latitude  REAL,
    longitude REAL,
    elevation REAL,
    state     VARCHAR(2),
    name      VARCHAR(30),
    gsn_flag  VARCHAR(3),
    hcn_flag  VARCHAR(3),
    wmo_id    VARCHAR(5),
    FOREIGN KEY (state) REFERENCES States (abbreviation)
);

/*
 * The Regions table contains a list of all the regions that each state can
 * be found in.
 */
CREATE TABLE Regions
(
    name TEXT PRIMARY KEY
);

/*
 * The States table contains additional information about each state that is not
 * listed in the source data set. This allows for easily filtering weather
 * stations based on their jurisdiction.
 */
CREATE TABLE States
(
    abbreviation TEXT PRIMARY KEY,
    name         TEXT NOT NULL,
    jurisdiction TEXT NOT NULL,
    region       TEXT,
    FOREIGN KEY (region) references Regions (name)
);


-- ##################################################
-- ##################################################
-- ##################################################
-- DEFINE TABLES FOR MONTHLY DATA
-- ##################################################
-- ##################################################
-- ##################################################


/*
 * The Months table is just a list of months given by their number and name.
 */
CREATE TABLE Months
(
    num  INTEGER PRIMARY KEY,
    name TEXT
);

/*
 * The MonthlyData table is an aggregate of all of the other monthly data
 * tables. It combines the monthly weather data for each station into one large
 * table that will later be used for training a model.
 */
CREATE TABLE MonthlyDataRaw
(
    station_id           VARCHAR(11),
    month                INTEGER,
    prcp_median          REAL,
    prcp_median_flag     VARCHAR(1),
    prcp_days_h          REAL,
    prcp_days_h_flag     VARCHAR(1),
    prcp_days_t          REAL,
    prcp_days_t_flag     VARCHAR(1),
    prcp_normal          REAL,
    prcp_normal_flag     VARCHAR(1),
    snow_median          REAL,
    snow_median_flag     VARCHAR(1),
    snow_days_t          REAL,
    snow_days_t_flag     VARCHAR(1),
    snow_days_i          REAL,
    snow_days_i_flag     VARCHAR(1),
    snow_depth_days      REAL,
    snow_depth_days_flag VARCHAR(1),
    snow_normal          REAL,
    snow_normal_flag     VARCHAR(1),
    temp_min_normal      REAL,
    temp_min_normal_flag VARCHAR(1),
    temp_min_stdev       REAL,
    temp_min_stdev_flag  VARCHAR(1),
    temp_max_normal      REAL,
    temp_max_normal_flag VARCHAR(1),
    temp_max_stdev       REAL,
    temp_max_stdev_flag  VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);


-- ##################################################
-- ##################################################
-- ##################################################
-- DEFINE TABLES FOR PRECIPITATION DATA
-- ##################################################
-- ##################################################
-- ##################################################


/*
 * The MonthlyPrecipitationMedians table stores data for each month from each
 * station. It's the 50th percentile of precipitation totals for that month,
 * given in inches.
 */
CREATE TABLE MonthlyPrecipitationMedians
(
    station_id VARCHAR(11),
    month      INTEGER,
    inches     REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlyPrecipitationDaysH table stores data for each month from each
 * station. It's the average number of days with at least 0.01 inches (1
 * hundredth) of precipitation per month.
 */
CREATE TABLE MonthlyPrecipitationDaysH
(
    station_id VARCHAR(11),
    month      INTEGER,
    days       REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlyPrecipitationDaysT table is the same as
 * MonthlyPrecipitationDaysH, except that the cutoff is at least 0.1 inches
 * (1 tenth) rather than 0.01.
 */
CREATE TABLE MonthlyPrecipitationDaysT
(
    station_id VARCHAR(11),
    month      INTEGER,
    days       REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlyPrecipitationNormals table stores data for each month from each
 * station. It's the long term average of monthly precipitation totals (the
 * 'normal').
 */
CREATE TABLE MonthlyPrecipitationNormals
(
    station_id VARCHAR(11),
    month      INTEGER,
    inches     REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallMedians table stores data for each month from each
 * station. It's the 50th percentile of snowfall totals for that month, given
 * in inches.
 */
CREATE TABLE MonthlySnowfallMedians
(
    station_id VARCHAR(11),
    month      INTEGER,
    inches     REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallDaysT table stores data for each month from each
 * station. It's the average number of days with at least 0.1 inches (1
 * tenth) of snowfall per month.
 */
CREATE TABLE MonthlySnowfallDaysT
(
    station_id VARCHAR(11),
    month      INTEGER,
    days       REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallDaysI table is the same as MonthlySnowfallDaysH, except
 * that the cutoff is at least 1 inch rather than 0.1.
 */
CREATE TABLE MonthlySnowfallDaysI
(
    station_id VARCHAR(11),
    month      INTEGER,
    days       REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowDepthDays table stores data for each month from each station.
 * It's the average number of days per month with at least 1 inch of snow
 * depth on the ground.
 */
CREATE TABLE MonthlySnowDepthDays
(
    station_id VARCHAR(11),
    month      INTEGER,
    days       REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallNormals table stores data for each month from each
 * station. It's the long term average of monthly snowfall totals (the
 * 'normal').
 */
CREATE TABLE MonthlySnowfallNormals
(
    station_id VARCHAR(11),
    month      INTEGER,
    inches     REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);



-- ##################################################
-- ##################################################
-- ##################################################
-- DEFINE TABLES FOR TEMPERATURE DATA
-- ##################################################
-- ##################################################
-- ##################################################


/*
 * The MonthlyTempMaxNormals stores data for each month from each station.
 * It's the long term average max temperature for each month (the 'normal').
 */
CREATE TABLE MonthlyTempMaxNormals
(
    station_id  VARCHAR(11),
    month       INTEGER,
    normal_temp REAL,
    flag        VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlyTempMaxStdev stores data for each month from each station.
 * It's the long term standard deviation of the max temperature for each month.
 */
CREATE TABLE MonthlyTempMaxStdev
(
    station_id VARCHAR(11),
    month      INTEGER,
    stdev      REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlyTempMinNormals stores data for each month from each station.
 * It's the long term average min temperature for each month (the 'normal').
 */
CREATE TABLE MonthlyTempMinNormals
(
    station_id  VARCHAR(11),
    month       INTEGER,
    normal_temp REAL,
    flag        VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);

/*
 * The MonthlyTempMinStdev stores data for each month from each station.
 * It's the long term standard deviation of the min temperature for each month.
 */
CREATE TABLE MonthlyTempMinStdev
(
    station_id VARCHAR(11),
    month      INTEGER,
    stdev      REAL,
    flag       VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES Stations (id)
);