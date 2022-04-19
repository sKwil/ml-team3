/*
 * After running the setup process, execute this script as the last step to
 * clean up the database. It drops the all of the Monthly*** tables that came
 * from individual data files, because those were used to create the aggregate
 * MonthlyDataRaw table and are now unnecessary.
 */

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
DROP TABLE IF EXISTS HourlyCloudsBroken;
DROP TABLE IF EXISTS HourlyCloudsClear;
DROP TABLE IF EXISTS HourlyCloudsFew;
DROP TABLE IF EXISTS HourlyCloudsOvercast;
DROP TABLE IF EXISTS HourlyCloudsScattered;
DROP TABLE IF EXISTS HourlyAggregateData;
DROP TABLE IF EXISTS HourlyDewPointNormal;
DROP TABLE IF EXISTS HourlyHeatIndexNormal;
DROP TABLE IF EXISTS HourlyPressureNormal;
DROP TABLE IF EXISTS HourlyWindSpeedAvg;
DROP TABLE IF EXISTS HourlyPercentCalm;
