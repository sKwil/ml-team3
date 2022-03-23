/*
 * This file creates the lookup table for the time of day.
 */

CREATE TABLE DayPhase
(
    hour  INTEGER,
    phase TEXT
);

INSERT INTO DayPhase (hour, phase) VALUES (0, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (1, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (2, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (3, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (4, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (5, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (6, 'morning');
INSERT INTO DayPhase (hour, phase) VALUES (7, 'morning');
INSERT INTO DayPhase (hour, phase) VALUES (8, 'morning');
INSERT INTO DayPhase (hour, phase) VALUES (9, 'morning');
INSERT INTO DayPhase (hour, phase) VALUES (10, 'morning');
INSERT INTO DayPhase (hour, phase) VALUES (11, 'midday');
INSERT INTO DayPhase (hour, phase) VALUES (12, 'midday');
INSERT INTO DayPhase (hour, phase) VALUES (13, 'midday');
INSERT INTO DayPhase (hour, phase) VALUES (14, 'midday');
INSERT INTO DayPhase (hour, phase) VALUES (15, 'midday');
INSERT INTO DayPhase (hour, phase) VALUES (16, 'midday');
INSERT INTO DayPhase (hour, phase) VALUES (17, 'evening');
INSERT INTO DayPhase (hour, phase) VALUES (18, 'evening');
INSERT INTO DayPhase (hour, phase) VALUES (19, 'evening');
INSERT INTO DayPhase (hour, phase) VALUES (20, 'evening');
INSERT INTO DayPhase (hour, phase) VALUES (21, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (22, 'night');
INSERT INTO DayPhase (hour, phase) VALUES (23, 'night');