/*
 * This file initializes the weather database, where all the raw data will be
 * transferred ands stored.
 */

DROP TABLE IF EXISTS Stations;

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
    wmo_id    VARCHAR(5)
);

/*
 * The MonthlyPrecipitationMedians table stores data for each month from each
 * station. It's the 50th percentile of precipitation totals for that month,
 * given in inches.
 */
CREATE TABLE MonthlyPrecipitationMedians
(
    id     VARCHAR(11),
    month  INTEGER,
    inches REAL,
    flag   VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlyPrecipitationDaysH table stores data for each month from each
 * station. It's the average number of days with at least 0.01 inches (1
 * hundredth) of precipitation per month.
 */
CREATE TABLE MonthlyPrecipitationDaysH
(
    id    VARCHAR(11),
    month INTEGER,
    days  REAL,
    flag  VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlyPrecipitationDaysT table is the same as
 * MonthlyPrecipitationDaysH, except that the cutoff is at least 0.1 inches
 * (1 tenth) rather than 0.01.
 */
CREATE TABLE MonthlyPrecipitationDaysT
(
    id    VARCHAR(11),
    month INTEGER,
    days  REAL,
    flag  VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlyPrecipitationNormals table stores data for each month from each
 * station. It's the long term average of monthly precipitation totals (the
 * 'normal').
 */
CREATE TABLE MonthlyPrecipitationNormals
(
    id     VARCHAR(11),
    month  INTEGER,
    normal REAL,
    flag   VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallMedians table stores data for each month from each
 * station. It's the 50th percentile of snowfall totals for that month, given
 * in inches.
 */
CREATE TABLE MonthlySnowfallMedians
(
    id     VARCHAR(11),
    month  INTEGER,
    inches REAL,
    flag   VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallDaysT table stores data for each month from each
 * station. It's the average number of days with at least 0.1 inches (1
 * tenth) of snowfall per month.
 */
CREATE TABLE MonthlySnowfallDaysT
(
    id    VARCHAR(11),
    month INTEGER,
    days  REAL,
    flag  VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallDaysI table is the same as MonthlySnowfallDaysH, except
 * that the cutoff is at least 1 inch rather than 0.1.
 */
CREATE TABLE MonthlySnowfallDaysI
(
    id    VARCHAR(11),
    month INTEGER,
    days  REAL,
    flag  VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowDepthDays table stores data for each month from each station.
 * It's the average number of days per month with at least 1 inch of snow
 * depth on the ground.
 */
CREATE TABLE MonthlySnowDepthDays
(
    id    VARCHAR(11),
    month INTEGER,
    days  REAL,
    flag  VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);

/*
 * The MonthlySnowfallNormals table stores data for each month from each
 * station. It's the long term average of monthly snowfall totals (the
 * 'normal').
 */
CREATE TABLE MonthlySnowfallNormals
(
    id     VARCHAR(11),
    month  INTEGER,
    normal REAL,
    flag   VARCHAR(1),
    FOREIGN KEY (id) REFERENCES Stations (id)
);
