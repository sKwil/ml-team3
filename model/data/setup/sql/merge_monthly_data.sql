/*
 * Initially, the monthly data from each file is put in a separate table in
 * the database. This script takes that separate data and merges it into one
 * table with monthly data for each station.
 */

INSERT INTO MonthlyDataRaw
SELECT S.id        as station,
       M.num       as month,
       PN.normal   as precipitation_median,
       PN.flag     as precipitation_median_flag,
       PDH.days    as precipitation_days_h,
       PDH.flag    as precipitation_days_h_flag,
       PDT.days    as precipitation_days_t,
       PDT.flag    as precipitation_days_t_flag,
       PN.normal   as precipitation_normal,
       PN.flag     as precipitation_normal_flag,
       SM.inches   as snow_median,
       SM.flag     as snow_median_flag,
       SDT.days    as snow_days_t,
       SDT.flag    as snow_days_t_flag,
       SDI.days    as snow_days_i,
       SDI.flag    as snow_days_i_flag,
       SN.normal   as snow_normals,
       SN.flag     as snow_normals_flag,
       SDD.days    as snow_depth_days,
       SDD.flag    as snow_depth_days_flag,
       TMAN.normal as temp_max_normal,
       TMAN.flag   as temp_max_normal_flag,
       TMAS.stdev  as temp_max_stdev,
       TMAS.flag   as temp_max_stdev_flag,
       TMIN.normal as temp_min_normal,
       TMIN.flag   as temp_min_normal_flag,
       TMIS.stdev  as temp_min_stdev,
       TMIS.flag   as temp_min_stdev_flag
FROM Stations as S
         CROSS JOIN Months as M
         LEFT JOIN MonthlyPrecipitationMedians PM
                   on S.id = PM.station_id AND M.num = PM.month
         LEFT JOIN MonthlyPrecipitationDaysH PDH
                   on S.id = PDH.station_id AND M.num = PDH.month
         LEFT JOIN MonthlyPrecipitationDaysT PDT
                   on S.id = PDT.station_id AND M.num = PDT.month
         LEFT JOIN MonthlyPrecipitationNormals PN
                   on S.id = PN.station_id AND M.num = PN.month
         LEFT JOIN MonthlySnowfallMedians SM
                   on S.id = SM.station_id AND M.num = SM.month
         LEFT JOIN MonthlySnowfallDaysT SDT
                   on S.id = SDT.station_id AND M.num = SDT.month
         LEFT JOIN MonthlySnowfallDaysI SDI
                   on S.id = SDI.station_id AND M.num = SDI.month
         LEFT JOIN MonthlySnowfallNormals SN
                   on S.id = SN.station_id AND M.num = SN.month
         LEFT JOIN MonthlySnowDepthDays SDD
                   on S.id = SDD.station_id AND M.num = SDD.month
         LEFT JOIN MonthlyTempMaxNormals TMAN
                   on S.id = TMAN.station_id AND M.num = TMAN.month
         LEFT JOIN MonthlyTempMaxStdev TMAS
                   on S.id = TMAS.station_id AND M.num = TMAS.month
         LEFT JOIN MonthlyTempMinNormals TMIN
                   on S.id = TMIN.station_id AND M.num = TMIN.month
         LEFT JOIN MonthlyTempMinStdev TMIS
                   on S.id = TMIS.station_id AND M.num = TMIS.month;
