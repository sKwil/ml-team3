/*
 * Initially, the monthly data from each file is put in a separate table in
 * the database. This script takes that separate data and merges it into one
 * table with monthly data for each station.
 */

INSERT INTO MonthlyDataRaw
SELECT S.id                            as station_id,
       M.num                           as month,
       PM.inches                       as prcp_median,
       PM.flag                         as prcp_median_flag,
       PDH.days                        as prcp_days_h,
       PDH.flag                        as prcp_days_h_flag,
       PDT.days                        as prcp_days_t,
       PDT.flag                        as prcp_days_t_flag,
       PN.inches                       as prcp_normal,
       PN.flag                         as prcp_normal_flag,
       SM.inches                       as snow_median,
       SM.flag                         as snow_median_flag,
       SDT.days                        as snow_days_t,
       SDT.flag                        as snow_days_t_flag,
       SDI.days                        as snow_days_i,
       SDI.flag                        as snow_days_i_flag,
       SDD.days                        as snow_depth_days,
       SDD.flag                        as snow_depth_days_flag,
       SN.inches                       as snow_normal,
       SN.flag                         as snow_normal_flag,
       TMIN.normal_temp                as temp_min_normal,
       TMIN.flag                       as temp_min_normal_flag,
       TMIS.stdev                      as temp_min_stdev,
       TMIS.flag                       as temp_min_stdev_flag,
       TMAN.normal_temp                as temp_max_normal,
       TMAN.flag                       as temp_max_normal_flag,
       TMAS.stdev                      as temp_max_stdev,
       TMAS.flag                       as temp_max_stdev_flag,
       HAD.broken_clouds_percentage    as clouds_broken,
       HAD.broken_clouds_flag          as clouds_broken_flag,
       HAD.clear_clouds_percentage     as clouds_clear,
       HAD.clear_clouds_flag           as clouds_clear_flag,
       HAD.few_clouds_percentage       as clouds_few,
       HAD.few_clouds_flag             as clouds_few_flag,
       HAD.overcast_clouds_percentage  as clouds_overcast,
       HAD.overcast_clouds_flag        as clouds_overcast_flag,
       HAD.scattered_clouds_percentage as clouds_scattered,
       HAD.scattered_clouds_flag       as clouds_scattered_flag,
       HAD.dew_point_avg               as dew_point,
       HAD.dew_point_avg_flag          as dew_point_flag,
       HAD.heat_index_avg              as heat_index,
       HAD.heat_index_avg_flag         as heat_index_avg,
       HAD.pressure_avg                as pressure,
       HAD.pressure_avg_flag           as pressure_flag,
       HAD.wind_speed_avg              as wind_speed,
       HAD.wind_speed_avg_flag         as wind_speed_flag,
       HAD.wind_calm_percentage        as wind_calm_percentage,
       HAD.wind_calm_percentage_flag   as wind_calm_percentage_flag

FROM Stations as S
         CROSS JOIN Months AS M
         LEFT JOIN MonthlyPrecipitationMedians PM
                   ON S.id = PM.station_id AND M.num = PM.month
         LEFT JOIN MonthlyPrecipitationDaysH PDH
                   ON S.id = PDH.station_id AND M.num = PDH.month
         LEFT JOIN MonthlyPrecipitationDaysT PDT
                   ON S.id = PDT.station_id AND M.num = PDT.month
         LEFT JOIN MonthlyPrecipitationNormals PN
                   ON S.id = PN.station_id AND M.num = PN.month
         LEFT JOIN MonthlySnowfallMedians SM
                   ON S.id = SM.station_id AND M.num = SM.month
         LEFT JOIN MonthlySnowfallDaysT SDT
                   ON S.id = SDT.station_id AND M.num = SDT.month
         LEFT JOIN MonthlySnowfallDaysI SDI
                   ON S.id = SDI.station_id AND M.num = SDI.month
         LEFT JOIN MonthlySnowfallNormals SN
                   ON S.id = SN.station_id AND M.num = SN.month
         LEFT JOIN MonthlySnowDepthDays SDD
                   ON S.id = SDD.station_id AND M.num = SDD.month
         LEFT JOIN MonthlyTempMaxNormals TMAN
                   ON S.id = TMAN.station_id AND M.num = TMAN.month
         LEFT JOIN MonthlyTempMaxStdev TMAS
                   ON S.id = TMAS.station_id AND M.num = TMAS.month
         LEFT JOIN MonthlyTempMinNormals TMIN
                   ON S.id = TMIN.station_id AND M.num = TMIN.month
         LEFT JOIN MonthlyTempMinStdev TMIS
                   ON S.id = TMIS.station_id AND M.num = TMIS.month
         LEFT JOIN HourlyAggregateData HAD
                   ON S.id = HAD.station_id AND M.num = HAD.month;
