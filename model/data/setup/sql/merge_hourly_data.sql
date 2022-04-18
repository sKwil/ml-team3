/*
 * This script merges all of the hourly data into one table. The data is
 * aggregated by month. Later, this data will be used by the
 * merge_monthly_data.sql script, which will combine it with the other monthly
 * data to form the final aggregate table: MonthlyDataRaw.
 */

INSERT INTO HourlyAggregateData

WITH BrokenClouds as (
    WITH J as (
        SELECT H.*, F.rank
        FROM HourlyCloudsBroken H
                 LEFT JOIN Flags F on H.flag = F.flag
    ),
         P as (
             SELECT station_id,
                    month,
                    AVG(percentage) as percentage
             FROM J
             WHERE percentage >= 0
             GROUP BY station_id, month
         ),
         F as (
             SELECT station_id, month, MAX(rank) as flag_rank
             FROM J
             GROUP BY station_id, month
         )
    SELECT P.station_id, P.month, P.percentage, Flags.flag
    FROM P
             LEFT OUTER JOIN F
                             ON P.station_id =
                                F.station_id and
                                P.month = F.month
             LEFT JOIN Flags ON F.flag_rank = Flags.rank),

     ClearClouds as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyCloudsClear H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(percentage) as percentage
                  FROM J
                  WHERE percentage >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.percentage, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     FewClouds as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyCloudsFew H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(percentage) as percentage
                  FROM J
                  WHERE percentage >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.percentage, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     OvercastClouds as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyCloudsOvercast H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(percentage) as percentage
                  FROM J
                  WHERE percentage >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.percentage, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     ScatteredClouds as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyCloudsScattered H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(percentage) as percentage
                  FROM J
                  WHERE percentage >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.percentage, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     DewPoint as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyDewPointNormal H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(dew_point) as dew_point
                  FROM J
                  WHERE dew_point >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.dew_point, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     HeatIndex as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyHeadIndexNormal H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(heat_index) as heat_index
                  FROM J
                  WHERE heat_index >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.heat_index, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     Pressure as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyPressureNormal H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(pressure) as pressure
                  FROM J
                  WHERE pressure >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.pressure, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     WindSpeed as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyWindSpeedAvg H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(wind_speed) as wind_speed
                  FROM J
                  WHERE wind_speed >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.wind_speed, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     ),

     WindCalm as (
         WITH J as (
             SELECT H.*, F.rank
             FROM HourlyPercentCalm H
                      LEFT JOIN Flags F on H.flag = F.flag
         ),
              P as (
                  SELECT station_id,
                         month,
                         AVG(percentage) as percentage
                  FROM J
                  WHERE percentage >= 0
                  GROUP BY station_id, month
              ),
              F as (
                  SELECT station_id, month, MAX(rank) as flag_rank
                  FROM J
                  GROUP BY station_id, month
              )
         SELECT P.station_id, P.month, P.percentage, Flags.flag
         FROM P
                  LEFT OUTER JOIN F
                                  ON P.station_id =
                                     F.station_id and
                                     P.month = F.month
                  LEFT JOIN Flags ON F.flag_rank = Flags.rank
     )


SELECT S.id                       as station_id,
       M.num                      as month,
       BrokenClouds.percentage    as broken_clouds_percentage,
       BrokenClouds.flag          as broken_clouds_flag,
       ClearClouds.percentage     as clear_clouds_percentage,
       ClearClouds.flag           as clear_clouds_flag,
       FewClouds.percentage       as few_clouds_percentage,
       FewClouds.flag             as few_clouds_flag,
       OvercastClouds.percentage  as overcast_clouds_percentage,
       OvercastClouds.flag        as overcast_clouds_flag,
       ScatteredClouds.percentage as scattered_clouds_percentage,
       ScatteredClouds.flag       as scattered_clouds_flag,
       DewPoint.dew_point         as dew_point_avg,
       DewPoint.flag              as dew_point_avg_flag,
       HeatIndex.heat_index       as heat_index_avg,
       HeatIndex.flag             as heat_index_avg_flag,
       Pressure.pressure          as pressure_avg,
       Pressure.flag              as pressure_avg_flag,
       WindSpeed.wind_speed       as wind_speed_avg,
       WindSpeed.flag             as wind_speed_avg_flag,
       WindCalm.percentage        as wind_calm_percentage,
       WindCalm.flag              as wind_calm_percentage_flag
FROM Stations as S
         CROSS JOIN Months as M
         LEFT JOIN BrokenClouds on BrokenClouds.station_id = S.id and
                                   BrokenClouds.month = M.num
         LEFT JOIN ClearClouds on ClearClouds.station_id = S.id and
                                  ClearClouds.month = M.num
         LEFT JOIN FewClouds on FewClouds.station_id = S.id and
                                FewClouds.month = M.num
         LEFT JOIN OvercastClouds on OvercastClouds.station_id = S.id and
                                     OvercastClouds.month = M.num
         LEFT JOIN ScatteredClouds on ScatteredClouds.station_id = S.id and
                                      ScatteredClouds.month = M.num
         LEFT JOIN DewPoint on DewPoint.station_id = S.id and
                               DewPoint.month = M.num
         LEFT JOIN HeatIndex on HeatIndex.station_id = S.id and
                                HeatIndex.month = M.num
         LEFT JOIN Pressure on Pressure.station_id = S.id and
                               Pressure.month = M.num
         LEFT JOIN WindSpeed on WindSpeed.station_id = S.id and
                                WindSpeed.month = M.num
         LEFT JOIN WindCalm on WindCalm.station_id = S.id and
                               WindCalm.month = M.num;
