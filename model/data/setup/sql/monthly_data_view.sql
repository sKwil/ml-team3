/*
 * This script creates the MonthlyData, MonthlyDataNotNull, and MonthlyDataModel views.
 *
 * MonthlyData is a selection of the MonthlyDataRaw table, where additional
 * information about the stations is included, and rows with null values for
 * every column are removed. Note that in the MonthlyData view, a row with only
 * some null values will remain. Only rows missing all weather data are omitted.
 *
 * The MonthlyDataNotNull view is identical to the MonthlyData view (in fact,
 * it is dependent on MonthlyData), except that it removes rows with *any*
 * null values, along with rows that contain invalid weather values (such as
 * -9999).
 *
 * MonthlyDataModel is a view based on MonthlyData that only includes columns
 * relevant to the ML model and removes observations with jurisdictions other
 * than 'state'.
 */

DROP VIEW IF EXISTS MonthlyData;
DROP VIEW IF EXISTS MonthlyDataNotNull;
DROP VIEW IF EXISTS MonthlyDataModel;


CREATE VIEW MonthlyData AS

SELECT MD.station_id,
       S.latitude,
       S.longitude,
       S.elevation,
       S.gsn_flag,
       S.hcn_flag,
       S.name,
       S.state,
       S.wmo_id,
       S2.jurisdiction,
       S2.region,
       MD.month,
       ROUND(MD.prcp_median, 3)          as prcp_median,
       MD.prcp_median_flag,
       MD.prcp_days_h,
       MD.prcp_days_h_flag,
       MD.prcp_days_t,
       MD.prcp_days_t_flag,
       ROUND(MD.prcp_normal, 3)          as prcp_normal,
       MD.prcp_normal_flag,
       MD.snow_median,
       MD.snow_median_flag,
       MD.snow_days_t,
       MD.snow_days_t_flag,
       MD.snow_days_i,
       MD.snow_days_i_flag,
       MD.snow_depth_days,
       MD.snow_depth_days_flag,
       MD.snow_normal,
       MD.snow_normal_flag,
       ROUND(MD.temp_min_normal, 3)      as temp_min_normal,
       MD.temp_min_normal_flag,
       ROUND(MD.temp_min_stdev, 3)       as temp_min_stdev,
       MD.temp_min_stdev_flag,
       ROUND(MD.temp_max_normal, 3)      as temp_max_normal,
       MD.temp_max_normal_flag,
       ROUND(MD.temp_max_stdev, 3)       as temp_max_stdev,
       MD.temp_max_stdev_flag,
       ROUND(MD.clouds_broken, 3)        as clouds_broken,
       MD.clouds_broken_flag,
       ROUND(MD.clouds_clear, 3)         as clouds_clear,
       MD.clouds_clear_flag,
       ROUND(MD.clouds_few, 3)           as clouds_few,
       MD.clouds_few_flag,
       ROUND(MD.clouds_overcast, 3)      as clouds_overcast,
       MD.clouds_overcast_flag,
       ROUND(MD.clouds_scattered, 3)     as clouds_scattered,
       MD.clouds_scattered_flag,
       ROUND(MD.dew_point, 3)            as dew_point,
       MD.dew_point_flag,
       ROUND(MD.heat_index, 3)           as heat_index,
       MD.heat_index_avg,
       ROUND(MD.pressure, 3)             as pressure,
       MD.pressure_flag,
       ROUND(MD.wind_speed, 3)           as wind_speed,
       MD.wind_speed_flag,
       ROUND(MD.wind_calm_percentage, 3) as wind_calm_percentage,
       MD.wind_calm_percentage_flag
FROM MonthlyDataRaw MD
         LEFT JOIN Stations S on MD.station_id = S.id
         LEFT JOIN States S2 on S.state = S2.abbreviation
WHERE MD.prcp_median IS NOT NULL
   OR MD.prcp_median_flag IS NOT NULL
   OR MD.prcp_days_h IS NOT NULL
   OR MD.prcp_days_h_flag IS NOT NULL
   OR MD.prcp_days_t IS NOT NULL
   OR MD.prcp_days_t_flag IS NOT NULL
   OR MD.prcp_normal IS NOT NULL
   OR MD.prcp_normal_flag IS NOT NULL
   OR MD.snow_median IS NOT NULL
   OR MD.snow_median_flag IS NOT NULL
   OR MD.snow_days_t IS NOT NULL
   OR MD.snow_days_t_flag IS NOT NULL
   OR MD.snow_days_i IS NOT NULL
   OR MD.snow_days_i_flag IS NOT NULL
   OR MD.snow_depth_days IS NOT NULL
   OR MD.snow_depth_days_flag IS NOT NULL
   OR MD.snow_normal IS NOT NULL
   OR MD.snow_normal_flag IS NOT NULL
   OR MD.temp_min_normal IS NOT NULL
   OR MD.temp_min_normal_flag IS NOT NULL
   OR MD.temp_min_stdev IS NOT NULL
   OR MD.temp_min_stdev_flag IS NOT NULL
   OR MD.temp_max_normal IS NOT NULL
   OR MD.temp_max_normal_flag IS NOT NULL
   OR MD.temp_max_stdev IS NOT NULL
   OR MD.temp_max_stdev_flag IS NOT NULL
   OR MD.clouds_broken IS NOT NULL
   OR MD.clouds_clear IS NOT NULL
   OR MD.clouds_few IS NOT NULL
   OR MD.clouds_overcast IS NOT NULL
   OR MD.clouds_scattered IS NOT NULL
   OR MD.dew_point IS NOT NULL
   OR MD.heat_index IS NOT NULL
   OR MD.pressure IS NOT NULL
   OR MD.wind_speed IS NOT NULL
   OR MD.wind_calm_percentage IS NOT NULL;



CREATE VIEW MonthlyDataNotNull AS

SELECT *
FROM MonthlyData as MD
WHERE MD.prcp_median IS NOT NULL
  AND MD.prcp_median_flag IS NOT NULL
  AND MD.prcp_days_h IS NOT NULL
  AND MD.prcp_days_h_flag IS NOT NULL
  AND MD.prcp_days_t IS NOT NULL
  AND MD.prcp_days_t_flag IS NOT NULL
  AND MD.prcp_normal IS NOT NULL
  AND MD.prcp_normal_flag IS NOT NULL
  AND MD.snow_median IS NOT NULL
  AND MD.snow_median_flag IS NOT NULL
  AND MD.snow_days_t IS NOT NULL
  AND MD.snow_days_t_flag IS NOT NULL
  AND MD.snow_days_i IS NOT NULL
  AND MD.snow_days_i_flag IS NOT NULL
  AND MD.snow_depth_days IS NOT NULL
  AND MD.snow_depth_days_flag IS NOT NULL
  AND MD.snow_normal IS NOT NULL
  AND MD.snow_normal_flag IS NOT NULL
  AND MD.temp_min_normal IS NOT NULL
  AND MD.temp_min_normal_flag IS NOT NULL
  AND MD.temp_min_stdev IS NOT NULL
  AND MD.temp_min_stdev_flag IS NOT NULL
  AND MD.temp_max_normal IS NOT NULL
  AND MD.temp_max_normal_flag IS NOT NULL
  AND MD.temp_max_stdev IS NOT NULL
  AND MD.temp_max_stdev_flag IS NOT NULL
  AND MD.clouds_broken IS NOT NULL
  AND MD.clouds_clear IS NOT NULL
  AND MD.clouds_few IS NOT NULL
  AND MD.clouds_overcast IS NOT NULL
  AND MD.clouds_scattered IS NOT NULL
  AND MD.dew_point IS NOT NULL
  AND MD.heat_index IS NOT NULL
  AND MD.pressure IS NOT NULL
  AND MD.wind_speed IS NOT NULL
  AND MD.wind_calm_percentage IS NOT NULL;



CREATE VIEW MonthlyDataModel AS
SELECT latitude,
       longitude,
       elevation,
       state,
       region,
       month,
       prcp_normal,
       prcp_days_t,
       temp_max_normal,
       temp_min_normal,
       snow_depth_days,
       snow_days_t,
       clouds_overcast + clouds_broken as clouds,
       dew_point,
       heat_index,
       pressure,
       wind_speed,
       wind_calm_percentage
FROM MonthlyData
WHERE jurisdiction = 'state';


CREATE VIEW MonthlyAverages AS
SELECT month,
       AVG(prcp_normal)          as prcpInt,
       AVG(prcp_days_t)          as prcpFreq,
       AVG(temp_max_normal)      as temp_max_normal,
       AVG(temp_min_normal)      as temp_min_normal,
       AVG(snow_depth_days)      as snowInt,
       AVG(snow_days_t)          as snowFreq,
       AVG(clouds)               as clouds,
       AVG(dew_point)            as dew_point,
       AVG(heat_index)           as heat_index,
       AVG(pressure)             as pressure,
       AVG(wind_speed)           as wind_speed,
       AVG(wind_calm_percentage) as wind_calm_percentage
FROM MonthlyDataModel
GROUP BY month;

