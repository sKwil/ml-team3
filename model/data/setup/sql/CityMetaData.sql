/*
 * This file creates the lookup table for a cities proximity to the ocean.
 */

CREATE TABLE CityMetaData
(
    city          TEXT PRIMARY KEY,
    near_ocean    INTEGER NOT NULL CHECK (is_near_ocean IN (0, 1)),
    near_mountain INTEGER NOT NULL CHECK (is_near_ocean IN (0, 1)),
    state         TEXT,
    region        TEXT,
    FOREIGN KEY (city) REFERENCES Cities (name)
);

INSERT INTO CityMetaData (city, near_ocean, near_mountain, state, region)
VALUES ('San Francisco', 2, 1, CA, S Pacif);

INSERT INTO CityMetaData (city, near_ocean, near_mountain, state, region)
VALUES ('Seattle', 2, 2, WA, N Pacif);

