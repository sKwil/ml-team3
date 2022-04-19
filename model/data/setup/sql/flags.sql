/*
 * This script populates the Flags table, which is a list of all the flags
 * that are given for numeric data in the raw data files. The flags have an
 * intrinsic order (or 'rank') according to their level of "completeness".
 */

INSERT INTO Flags (flag, description, rank)
VALUES ('C', 'Complete', 1);

INSERT INTO Flags (flag, description, rank)
VALUES ('S', 'Standard', 2);

INSERT INTO Flags (flag, description, rank)
VALUES ('R', 'Representative', 3);

INSERT INTO Flags (flag, description, rank)
VALUES ('P', 'Provisional', 4);

INSERT INTO Flags (flag, description, rank)
VALUES ('Q', 'Quasi-normal', 5);

INSERT INTO Flags (flag, description, rank)
VALUES (' ', 'Blank', 6);
