/*
 * This script creates the MonthlyData and MonthlyDataNotNull views.
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
 */

DROP VIEW IF EXISTS MonthlyData;
DROP VIEW IF EXISTS MonthlyDataNotNull;


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
       ROUND(MD.prcp_median, 3)      as prcp_median,
       MD.prcp_median_flag,
       MD.prcp_days_h,
       MD.prcp_days_h_flag,
       MD.prcp_days_t,
       MD.prcp_days_t_flag,
       ROUND(MD.prcp_normal, 3)      as prcp_normal,
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
       ROUND(MD.temp_min_normal, 3)  as temp_min_normal,
       MD.temp_min_normal_flag,
       ROUND(MD.temp_min_stdev, 3)   as temp_min_stdev,
       MD.temp_min_stdev_flag,
       ROUND(MD.temp_max_normal, 3)  as temp_max_normal,
       MD.temp_max_normal_flag,
       ROUND(MD.temp_max_stdev, 3)   as temp_max_stdev,
       MD.temp_max_stdev_flag,
       ROUND(MD.clouds_broken, 3)    as clouds_broken,
       MD.clouds_broken_flag,
       ROUND(MD.clouds_clear, 3)     as clouds_clear,
       MD.clouds_clear_flag,
       ROUND(MD.clouds_few, 3)       as clouds_few,
       MD.clouds_few_flag,
       ROUND(MD.clouds_overcast, 3)  as clouds_overcast,
       MD.clouds_overcast_flag,
       ROUND(MD.clouds_scattered, 3) as clouds_scattered,
       MD.clouds_scattered_flag
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
   OR MD.clouds_scattered IS NOT NULL;



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
  AND MD.clouds_scattered IS NOT NULL;
