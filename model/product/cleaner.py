import numpy as np
import pandas as pd

from model.data import db

__BAD_VALUES = [-9999, -8888, -7777, -6666, -5555, -4444]


def get_cleaned_data() -> pd.DataFrame:
    """
    Load the SQL data and clean it, filling in null and invalid values. Also
    extract a numpy array of labels and drop unused features.

    :return: the final cleaned dataframe, ready for ML training.
    """

    # Get the station data and aggregate monthly data
    station_df, monthly_df = _get_data_frames()

    # Clean the data
    station_df = _clean_station_data(station_df, monthly_df)

    return station_df


def _get_data_frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Get the data frames from the SQL database that will be used to train the
    ML model. This loads two data frames:

    1. The first data frame is all the aggregate monthly data for each weather
       station.

    2. The second data frame is like the first, but averaged across all
       weather stations. There is one row for each month.

    :return: the data frames as a tuple
    """

    with db.get_conn() as conn:
        return (pd.read_sql_query('SELECT * FROM MonthlyDataModel;', conn),
                pd.read_sql_query('SELECT * FROM MonthlyAverages;', conn))


def _clean_station_data(station_data: pd.DataFrame,
                        monthly_data: pd.DataFrame) -> pd.DataFrame:
    """
    Take raw station data and clean it. This means replacing all the null and
    invalid values with the aggregate monthly data from the monthly_data
    DataFrame.

    This is done by extracting each feature as a numpy array and cleaning it
    from there. Then the arrays are reassembled into a new, cleaned dataframe.

    This does the following steps:
    1. Separate station and monthly data into separate numpy arrays for each
       column.
    2. Iterate through each value in the station data arrays, looking for bad
       values (NaN, -9999, etc.) If bad values are found, replace them with
       the corresponding monthly average.
    3. Reassemble the cleaned numpy arrays into a finished data frame. Here the
       region, latitude, and elevation features are implicitly dropped,
       as they're never put into the new dataframe. The longitude column
       stays, as it's used for separating training and testing data later.
    4. Do some sort of replacing NaN/infinity or something, idk.

    :param station_data: the raw station data that needs to be cleaned
    :param monthly_data: the average data used to fill in missing values
    :return: the cleaned station data
    """

    # Get stuff from the station_data dataframe
    months_array = station_data['month'].to_numpy()
    prcp_norm_array = station_data['prcp_normal'].to_numpy()
    prcp_days_t_array = station_data['prcp_days_t'].to_numpy()
    temp_max_normal_array = station_data['temp_max_normal'].to_numpy()
    temp_min_normal_array = station_data['temp_min_normal'].to_numpy()
    snow_depth_array = station_data['snow_depth_days'].to_numpy()
    snow_days_array = station_data['snow_days_t'].to_numpy()
    clouds_array = station_data['clouds'].to_numpy()
    dew_array = station_data['dew_point'].to_numpy()
    heat_array = station_data['heat_index'].to_numpy()
    pressure_array = station_data['pressure'].to_numpy()
    wind_array = station_data['wind_speed'].to_numpy()
    wind_calm_array = station_data['wind_calm_percentage'].to_numpy()

    # Get stuff from the monthly average data frame
    prcp_int_m = monthly_data['prcpInt'].to_numpy()
    prcp_freq_m = monthly_data['prcpFreq'].to_numpy()
    temp_max_normal_m = monthly_data['temp_max_normal'].to_numpy()
    temp_min_normal_m = monthly_data['temp_min_normal'].to_numpy()
    snow_depth_m = monthly_data['snowInt'].to_numpy()
    snow_days_m = monthly_data['snowFreq'].to_numpy()
    clouds_m = monthly_data['clouds'].to_numpy()
    dew_m = monthly_data['dew_point'].to_numpy()
    heat_m = monthly_data['heat_index'].to_numpy()
    pressure_m = monthly_data['pressure'].to_numpy()
    wind_m = monthly_data['wind_speed'].to_numpy()
    wind_calm_m = monthly_data['wind_calm_percentage'].to_numpy()

    # Replace all bad values
    for i in range(len(months_array)):
        if is_bad(prcp_days_t_array[i]):
            prcp_days_t_array[i] = prcp_freq_m[months_array[i] - 1]
        if is_bad(temp_max_normal_array[i]):
            temp_max_normal_array[i] = temp_max_normal_m[months_array[i] - 1]
        if is_bad(temp_min_normal_array[i]):
            temp_min_normal_array[i] = temp_min_normal_m[months_array[i] - 1]
        if is_bad(snow_days_array[i]):
            snow_days_array[i] = snow_days_m[months_array[i] - 1]
        if is_bad(clouds_array[i]):
            clouds_array[i] = clouds_m[months_array[i] - 1]
        if is_bad(dew_array[i]):
            dew_array[i] = dew_m[months_array[i] - 1]
        if is_bad(heat_array[i]):
            heat_array[i] = heat_m[months_array[i] - 1]
        if is_bad(wind_array[i]):
            wind_array[i] = wind_m[months_array[i] - 1]

    stateNump = station_data['state'].to_numpy()

    mount = stateNump.copy()
    ocean = stateNump.copy()

    mountSwitcher = {
        'AL': 1, 'AR': 2, 'AZ': 0, 'AK': 2, 'CA': 0, 'CO': 2, 'CT': 0,
        'DE': 0, 'FL': 0, 'GA': 1, 'HI': 0, 'IA': 2, 'ID': 2, 'IL': 2,
        'IN': 2, 'KS': 2, 'KY': 2, 'LA': 0, 'MA': 0, 'MD': 0, 'ME': 0,
        'MI': 1, 'MN': 1, 'MO': 2, 'MS': 1, 'MT': 2, 'NC': 0, 'ND': 2,
        'NE': 2, 'NH': 1, 'NJ': 0, 'NM': 1, 'NV': 2, 'NY': 1, 'OH': 1,
        'OK': 2, 'OR': 0, 'PA': 1, 'RI': 0, 'SC': 0, 'SD': 2, 'TN': 2,
        'TX': 0, 'UT': 2, 'VA': 1, 'VT': 1, 'WA': 0, 'WI': 1, 'WV': 2, 'WY': 2
    }

    oceanSwitcher = {
        'AL': 0, 'AR': 0, 'AZ': 2, 'AK': 0, 'CA': 1, 'CO': 2, 'CT': 1,
        'DE': 1, 'FL': 0, 'GA': 1, 'HI': 1, 'IA': 0, 'ID': 2, 'IL': 0,
        'IN': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'MA': 1, 'MD': 0, 'ME': 1,
        'MI': 0, 'MN': 0, 'MO': 0, 'MS': 0, 'MT': 2, 'NC': 1, 'ND': 0,
        'NE': 0, 'NH': 1, 'NJ': 0, 'NM': 2, 'NV': 2, 'NY': 1, 'OH': 1,
        'OK': 0, 'OR': 1, 'PA': 1, 'RI': 0, 'SC': 0, 'SD': 0, 'TN': 1,
        'TX': 0, 'UT': 2, 'VA': 0, 'VT': 1, 'WA': 2, 'WI': 0, 'WV': 1, 'WY': 2
    }

    for i in range(len(stateNump)):
        mount[i] = mountSwitcher[stateNump[i]]
        ocean[i] = oceanSwitcher[stateNump[i]]

    # Recreate dataframe from newly cleaned arrays
    cleaned = pd.DataFrame({
        'state': station_data['state'],
        'mountains_prox': mount,
        'ocean_prox': ocean,
        'longitude': station_data['longitude'],
        'month': months_array,
        'prcp_days_t_array': prcp_days_t_array,
        "temp_max_normal_array": temp_max_normal_array,
        "temp_min_normal_array": temp_min_normal_array,
        "snow_days_array": snow_days_array,
        "clouds_array": clouds_array,
        "dew_array": wind_array,
        "heat_array": wind_array,
        "wind_array": wind_array
    })

    # Replace some values, ig. I have no idea what this is for. Trenton got it
    # from the internet without citing his source.
    cleaned.replace([np.inf, -np.inf], np.nan, inplace=True)
    cleaned.fillna(method="ffill", inplace=True)

    return cleaned


def is_bad(value: any) -> bool:
    """
    Determine if a value is "bad" (meaning it's null, na, or one of the
    -9999/-8888/etc. error codes). If it's bad, return true; otherwise,
    return false.

    :param value: the value to check.
    :return: true if and only if the value is bad.
    """

    return value in __BAD_VALUES or pd.isna(value)
