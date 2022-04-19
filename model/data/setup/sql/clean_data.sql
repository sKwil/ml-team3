/*
 * This script looks for empty cells in the MonthlyDataRaw and Stations tables
 * and replaces them with <null>.
 */

UPDATE Stations
SET gsn_flag = NULLIF(TRIM(gsn_flag), ''),
    hcn_flag = NULLIF(TRIM(hcn_flag), ''),
    wmo_id   = NULLIF(TRIM(wmo_id), '');


UPDATE MonthlyDataRaw
SET station_id            = NULLIF(TRIM(station_id), ''),
    month                 = NULLIF(TRIM(month), ''),
    prcp_median           = NULLIF(TRIM(prcp_median), ''),
    prcp_median_flag      = NULLIF(TRIM(prcp_median_flag), ''),
    prcp_days_h           = NULLIF(TRIM(prcp_days_h), ''),
    prcp_days_h_flag      = NULLIF(TRIM(prcp_days_h_flag), ''),
    prcp_days_t           = NULLIF(TRIM(prcp_days_t), ''),
    prcp_days_t_flag      = NULLIF(TRIM(prcp_days_t_flag), ''),
    prcp_normal           = NULLIF(TRIM(prcp_normal), ''),
    prcp_normal_flag      = NULLIF(TRIM(prcp_normal_flag), ''),
    snow_median           = NULLIF(TRIM(snow_median), ''),
    snow_median_flag      = NULLIF(TRIM(snow_median_flag), ''),
    snow_days_t           = NULLIF(TRIM(snow_days_t), ''),
    snow_days_t_flag      = NULLIF(TRIM(snow_days_t_flag), ''),
    snow_days_i           = NULLIF(TRIM(snow_days_i), ''),
    snow_days_i_flag      = NULLIF(TRIM(snow_days_i_flag), ''),
    snow_depth_days       = NULLIF(TRIM(snow_depth_days), ''),
    snow_depth_days_flag  = NULLIF(TRIM(snow_depth_days_flag), ''),
    snow_normal           = NULLIF(TRIM(snow_normal), ''),
    snow_normal_flag      = NULLIF(TRIM(snow_normal_flag), ''),
    temp_min_normal       = NULLIF(TRIM(temp_min_normal), ''),
    temp_min_normal_flag  = NULLIF(TRIM(temp_min_normal_flag), ''),
    temp_min_stdev        = NULLIF(TRIM(temp_min_stdev), ''),
    temp_min_stdev_flag   = NULLIF(TRIM(temp_min_stdev_flag), ''),
    temp_max_normal       = NULLIF(TRIM(temp_max_normal), ''),
    temp_max_normal_flag  = NULLIF(TRIM(temp_max_normal_flag), ''),
    temp_max_stdev        = NULLIF(TRIM(temp_max_stdev), ''),
    temp_max_stdev_flag   = NULLIF(TRIM(temp_max_stdev_flag), ''),
    clouds_broken         = NULLIF(TRIM(clouds_broken), ''),
    clouds_broken_flag    = NULLIF(TRIM(clouds_broken_flag), ''),
    clouds_clear          = NULLIF(TRIM(clouds_clear), ''),
    clouds_clear_flag     = NULLIF(TRIM(clouds_clear_flag), ''),
    clouds_few            = NULLIF(TRIM(clouds_few), ''),
    clouds_few_flag       = NULLIF(TRIM(clouds_few_flag), ''),
    clouds_overcast       = NULLIF(TRIM(clouds_overcast), ''),
    clouds_overcast_flag  = NULLIF(TRIM(clouds_overcast_flag), ''),
    clouds_scattered      = NULLIF(TRIM(clouds_scattered), ''),
    clouds_scattered_flag = NULLIF(TRIM(clouds_scattered_flag), '');
