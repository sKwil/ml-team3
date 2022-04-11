/*
 * This script creates the MonthlyData view, which is a selection of the
 * MonthlyData table, where additional information about the stations is
 * included, and rows with null values for every column are removed.
 *
 * Note that a row with only some null values will remain. Only rows missing all
 * weather data are omitted.
 */

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
       MD.month,
       MD.prcp_median,
       MD.prcp_median_flag,
       MD.prcp_days_h,
       MD.prcp_days_h_flag,
       MD.prcp_days_t,
       MD.prcp_days_t_flag,
       ROUND(MD.prcp_normal, 3)     as prcp_normal,
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
       ROUND(MD.temp_min_normal, 3) as temp_min_normal,
       MD.temp_min_normal_flag,
       MD.temp_min_stdev,
       MD.temp_min_stdev_flag,
       ROUND(MD.temp_max_normal, 3) as temp_max_normal,
       MD.temp_max_normal_flag,
       MD.temp_max_stdev,
       MD.temp_max_stdev_flag
FROM MonthlyDataRaw MD
         LEFT JOIN Stations S on MD.station_id = S.id
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
   OR MD.temp_min_norma IS NOT NULL
   OR MD.temp_min_normal_flag IS NOT NULL
   OR MD.temp_min_stdev IS NOT NULL
   OR MD.temp_min_stdev_flag IS NOT NULL
   OR MD.temp_max_normal IS NOT NULL
   OR MD.temp_max_normal_flag IS NOT NULL
   OR MD.temp_max_stdev IS NOT NULL
   OR MD.temp_max_stdev_flag IS NOT NULL;
