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
