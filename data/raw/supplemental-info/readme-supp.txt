README FILE FOR NOAA'S 1981-2010 SUPPLEMENTAL CLIMATE NORMALS

OUTLINE

I.   CONTENTS
II.  FILENAMING
III. FILE FORMATS
IV.  UNITS
V.   SPECIAL VALUES
VI.  FLAGS

I.  CONTENTS

    readme-supp.txt - this file
    
    status-supp.txt - the status history of the 1981-2010 Supplemental Normals
    
    Below are descriptions of the four directories at this level.

    A. products directory

       The 1981-2010 Normals are located in the products directory. Within 
       products, there are four subdirectories:       
         
       1. agricultural - contains all agricultural normals files including growing 
       	  degree day normals, frost-freeze date probabilities, growing
	  season length normals, and probabilities of frost-freeze 
	  occurrence.
       2. air-freezing-index - contains the air freezing index return period file
       3. hourly-10yr - contains all 2001-2010 normals derived from hourly data, 
          including temperature, dew point temperature, heat index, wind chill, wind, 
          cloudiness, heating and cooling degree hours, and pressure normals.
       4. monthly-temperatures - (future directory) will contain monthly temperature
          normals of maximum, minimum, and average temperature computed using 5-,
	  10-, 15, and 20-year averages; OCN; and the Hinge Fit approach.

    B. station-inventories directory

       This directory contains station inventories for each product class. These
       inventories include the GHCN-Daily ID, latitude, longitude, state, and 
       station names. 

       1. afi-inventory.txt contains all stations used in the air freezing index
          analysis
       2. agri-inventory.txt contains all stations used in the agricultural normals
          analysis (except growing degree days, which has its own inventory below)
       3. grdd-inventory.txt contains all stations used in the growing degree day
          analysis
       4. hly-inventory.txt contains all stations used in the hourly analysis
       5. temp-nnyear-inventory.txt (future file) will contain all stations used in
          the 5-, 10-, 15-, and 20-year monthly temperature normals analysis
       6. temp-ocn-hinge-inventory.txt (future file) will contain all stations used
          in the OCN and Hinge Fit monthly temperature normals analysis

    C. documentation directory

       The documentation directory contains technical information about how the
       normals were computed and other relevant information.
      
       1. afi-manuscript.pdf is a manuscript in review with the Journal of Applied
          Meteorology and Climatology that describes the Air Freezing Index return
	  periods.
       2. agricultural-normals-filenames.txt lists the filenames and descriptions of
          files containing the agricultural normals.
       3. agricultural-normals-methodology.pdf is a manuscript that describes the
          methodology used to compute the agricultural normals.
       4. hourly-10yr-filenames.txt lists the filenames and descriptions of files
          containing the 10-year normals derived from hourly data
       5. hourly-methodology-addendum-2014.pdf describes the methodology utilized to
          compute all normals calculated from hourly data.
       6. monthly-temperatures-filenames.txt (future file) will list the filenames
          and descriptions of files containing the supplemental monthly temperature
	  normals.
       7. monthly-temperatures-methodology.pdf (future file) will describe the
          methodology used to compute the supplemental monthly temperature normals.

    D. source-datasets directory

       The source-datasets directory contains source datasets used to compute the 
       1981-2010 Supplemental Normals found in this collection.      
      
       1. daily-filled-adjusted-tmax.dat.gz contains the serially-complete maximum
          temperature values used to compute seasonal Air Freezing Index values
       2. daily-filled-adjusted-tmin.dat.gz contains the serially-complete minimum
          temperature values used to compute seasonal Air Freezing Index values
       3. isdlite-normals.tar.gz contains the ISD-Lite hourly data
       4. monthly-filled-tmax-1951-2010.txt (future file) will contain the
          serially-complete monthly maximum temperature values from 1951 to 2010 used
	  to compute OCN and Hinge Fit Normals
       5. monthly-filled-tmin-1951-2010.txt (future file) will contain the
          serially-complete monthly minimum temperature values from 1951 to 2010 used
	  to compute OCN and Hinge Fit Normals
       
       The files listed above are intermediate values used in the computation of the
       Supplemental Normals. Users wishing to utilize these files for another purpose
       should contact NOAA/NCEI for formatting and other information.

II. FILENAMING

    All supplemental normals files are named following the form 
    RRR-EEEE-SSSSSS[-CCCCCCC].txt, where the portion in brackets is only used
    when necessary. The four components are defined as follows.

    A. RRR is the Reporting period, which can take the following values:

       ann = annual
       djf = December, January, February (winter)
       dly = daily
       jja = June, July, August (summer)
       mam = March, April, May (spring)
       mly = monthly
       rtp = return periods (used for Air Freezing Index)
       son = September, October, November (autumn)

    B. EEEE is the meteorological Element, which can take the following values:

       cldd = cooling degree days
       cldh = cooling degree hours
       clod = clouds
       dewp = dew point temperature
       grdd = growing degree days
       hidx = heat index
       htdd = heating degree days
       htdh = heating degree hours
       pres = sea level pressure
       tavg = daily mean temperature (average of tmax and tmin)
       temp = temperature
       tmax = daily maximum temperature
       tmin = daily minimum temperature
       wchl = wind chill
       wind = wind

    C. SSSSSS is the Statistic, which can take the following values:

       05year = 2006-2010 average
       10pctl = Climatological 10th percentile
       10year = 2001-2010 average
       15year = 1996-2010 average
       1stdir = Prevailing Wind Direction
       1stpct = Prevailing Wind Percentage
       20year = 1991-2010 average
       2nddir = Secondary Wind Direction
       2ndpct = Secondary Wind Percentage
       90pctl = Climatological 90th percentile
       afzndx = Air Freezing Index
       avgspd = Average Wind Speed
       baseNN = Growing degree day normals with base temperature NN
                NN can be 40, 45, 50, 55, 57, 60, 65, 70, or 72F
       hngfit = Hinge Fit Normals for 2010
       normal = Climatological Average
       ocnorm = Optimal Climate Normals (OCN)
       pctbkn = Percent Broken (clouds)
       pctclm = Percent Calm (winds)
       pctclr = Percent Clear (clouds)
       pctfew = Percent Few (clouds)
       pctovc = Percent Overcast (clouds)
       pctsct = Percent Scattered (clouds)
       prbfst = Probability of first frost-freeze of the cold season occurring on
                specified date or earlier
       prbgsl = Probability of specified growing season length or longer
       prblst = Probability of last frost-freeze of the cold season occurring on
                specified date or later
       prbocc = Probability of occurrence of specified minimum temperature or
                lower
       tbXX86 = Truncated base growing degree day normal for corn
                XX can be 48 or 50F
       vctdir = Mean Wind Vector Direction
       vctspd = Mean Wind Vector Magnitude


    D. CCCCCCC is the Condition used in conjunction with probabilities:

       tXXFpYY = the XX temperature threshold at probability level YY% 
       		 YY can be 10, 20, 30, 40, 50, 60, 70, 80,or 90
		 XX can be 16, 20, 24, 28, 32, or 36
       
       lsthNNN = less than or equal to NNN whole degrees Fahrenheit
	         NNN can be 016,020,024,028,032,036

III.FILE FORMATS

    A. FORMAT OF ANNUAL/SEASONAL FILES
       (ann-*.txt, djf-*.txt, mam-*.txt, jja-*.txt, son-*.txt)

       Each file contains the annual/seasonal values of one parameter at all 
       qualifying stations. There is one record (line) per station.

       The variables in each record include the following:

       Variable  Columns  Type
       ----------------------------
       STNID       1- 11  Character
       VALUE      19- 23  Integer
       FLAG       24- 24  Character
       ----------------------------

       These variables have the following definitions:

       STNID   is the GHCN-Daily station identification code.
       VALUE1  is the annual/seasonal value.
       FLAG1   is the completeness flag for the annual/seasonal value. See Flags
               section below.

    B. FORMAT OF MONTHLY FILES (mly-*.txt)

       Each file contains the values of one parameter for each month of the year 
       at all qualifying stations. There is one record per station.

       The variables in each record include the following:

       Variable  Columns  Type
       ----------------------------
       STNID       1- 11  Character
       VALUE1     19- 23  Integer
       FLAG1      24- 24  Character
       - - - - - - - - - - - - - -
       VALUE12    96-100  Integer
       FLAG12    101-101  Character
       ----------------------------

       These variables have the following definitions:

       STNID   is the GHCN-Daily station identification code.
       VALUE1  is the January value.
       FLAG1   is the completeness flag for January. See Flags section below.
       - - - -
       Value12 is the December value.
       Flag12  is the completeness flag for December.

    C. FORMAT OF DAILY FILES
       (dly-*.txt)          

       Each file contains the values of one parameter for each day of the year 
       at all qualifying stations. There is one record per station-calendar month.

       The variables in each record include the following:

       Variable  Columns  Type
       ----------------------------
       STNID       1- 11  Character
       MONTH      13- 14  Integer
       VALUE1     19- 23  Integer
       FLAG1      24- 24  Character
       - - - - - - - - - - - - - - 
       VALUE31   229-233  Integer
       FLAG31    234-234  Character
       ----------------------------

       These variables have the following definitions:

       STNID   is the GHCN-Daily station identification code.
       MONTH   is the month in the 30-year period used. 01=January; 12=December
       VALUE1  is the value for the first day of the month.
       FLAG1   is a completeness flag based on the WMO normals classification, for 
               the first day of the month. See Flags Section below.
       - - - -
       Value31 is the value for day 31 of the month.
       Flag31  is the completeness flag for day 31 of the month.

    D. FORMAT OF HOURLY FILES
       (hly-*.txt)

       Each file contains the values of one parameter for each hour of the day 
       at all qualifying stations. There is one record per station-calendar day.

       The variables in each record include the following:

       Variable  Columns  Type
       ----------------------------
       STNID       1- 11  Character
       MONTH      13- 14  Integer
       DAY        16- 17  Integer
       VALUE1     19- 23  Integer
       FLAG1      24- 24  Character
       - - - - - - - - - - - - - - 
       VALUE24   180-184  Integer
       FLAG24    185-185  Character
       ----------------------------

       These variables have the following definitions:

       STNID   is the GHCN-Daily station identification code
       MONTH   is the month in the 30-year period used. 01=January; 12=December
       DAY     is the day in the 30-year period used. Varies from 1 to 31 in each 
               record.
       VALUE1  is the value for the first hour of the day
       FLAG1   is a completeness flag based on the WMO normals classification, for 
               the first hour of the day. See Flags Section below.
       - - - -
       VALUE24 is the value for last hour of the month.
       FLAG24  is the completeness flag for the last hour of the day
    
    E. FORMAT OF THE AFI RETURN PERIOD FILE
       (rtp-tavg-afzndx.txt)

       The file contains the AFI return period values for the following return
       periods (in years): 1.1, 1.25, 2, 2.5, 3.3, 5, 10, 20, 25, 50, 100. There is
       one record per station.

       The variables in each record include the following:

       Variable  Columns  Type
       ----------------------------
       STNID       1 - 11  Character
       VALUE1     19 - 23  Integer
       FLAG1      24 - 24  Character
       - - - - - - - - - - - - - - 
       VALUE11    89 - 93  Integer
       FLAG11     94 - 94  Character
       ----------------------------

       These variables have the following definitions:

       STNID   is the GHCN-Daily station identification code.
       VALUE1  is the 1.1-year return period.
       FLAG1   is a completeness flag.
       - - - -
       VALUE11 is the 100-year return period.
       FLAG24  is a completeness flag.
    
    F. FORMAT OF STATION INVENTORIES (*-inventory.txt)

       Each file contains on station per line.

       The variables in each record include the following:
       ------------------------------
       Variable   Columns   Type
       ------------------------------
       ID            1-11   Character
       LATITUDE     13-20   Real
       LONGITUDE    22-30   Real
       ELEVATION    32-37   Real
       STATE        39-40   Character
       NAME         42-71   Character
       GSNFLAG      73-75   Character
       HCNFLAG      77-79   Character
       WMOID        81-85   Character
       ------------------------------

       These variables have the following definitions:

       ID         is the station identification code.  Note that the first two
                  characters denote the FIPS country code, the third character 
                  is a network code that identifies the station numbering system 
                  used, and the remaining eight characters contain the actual 
                  station ID.
       LATITUDE   is latitude of the station (in decimal degrees).
       LONGITUDE  is the longitude of the station (in decimal degrees).
       ELEVATION  is the elevation of the station (in meters, missing = -999.9).
       STATE      is the U.S. postal code for the state (for U.S. stations only).
       NAME       is the name of the station.
       GSNFLAG    is a flag that indicates whether the station is part of the 
                  GCOS Surface Network (GSN). The flag is assigned by 
		  cross-referencing the number in the WMOID field with the
		  official list of GSN stations. There are two possible values:

                  Blank = non-GSN station or WMO Station number not available
                  GSN   = GSN station 

       HCNFLAG    is a flag that indicates whether the station is part of the
                  U.S. Historical Climatology Network (HCN).  There are two 
		  possible values:

                  Blank = non-HCN station
                  HCN   = HCN station

       WMOID      is the World Meteorological Organization (WMO) number for the
                  station. If the station has no WMO number, then the field is
		  blank.

IV. UNITS

    tenths of degrees Fahrenheit for maximum, minimum, average, dew point, heat 
    index, wind chill, and air temperature normals (e.g., "703" is 70.3F)
    
    whole degrees Fahrenheit for growing degree days

    dates (MM/DD) for probabilities of first/last events (e.g., 05/01 is May 1)
    
    whole days for growing season length 
    
    tenths of percent for probabilities of occurrence (e.g., "299" is 29.9%)
    
    tenths of degree hours for heating and cooling degree hours (e.g., "152" is 15.2)
    
    tenths of millibars for mean sea level pressure normals (e.g., "10147" is 1014.7
    mb)
    
    tenths of percent for prevailing and secondary wind direction percentages (e.g.,
    "299" is 29.9%)
    
    prevailing and secondary wind directions can take on 8 values: 1=N, 2=NE, 3=E, 
    4=SE, 5=S, 6=SW, 7=W, 8=NW
    
    tenths of mph for wind speeds and vector magnitudes (e.g. "73" is 7.3 mph)
    
    whole degrees for mean vector wind directions

V. SPECIAL VALUES

    -9999: missing or insufficient data; values cannot be computed
    -8888: date not defined (e.g. February 30, September 31) - used in daily
           files to achieve fixed-length records 
    -7777: a non-zero growing degree day value that would round to zero
    -6666: parameter undefined; used in probabilities of first/last events to
           indicate the event is too infrequent to estimate dates, as well as
	   AFI return periods that cannot be computed because too few years have
	   non-zero seasonal AFI values; "too warm to compute"
    -4444: indicates year-round risk of frost-freeze; "too cold to compute"

VI. FLAGS

    Flags accompany every Normals value and indicate the completeness of the data 
    record used to compute each value. There are six flag options described 
    generally below. 
 	
   C = complete (all 30 years used)
   S = standard (no more than 5 years missing and no more than 3 consecutive 
       years missing among the sufficiently complete years)
   R = representative (observed record utilized incomplete, but value was scaled
       or based on filled values to be representative of the full period of
       record)
   P = provisional (at least 10 years used, but not sufficiently complete to be 
       labeled as standard or representative).
   Q = quasi-normal (at least 2 years per month, but not sufficiently complete to 
       be labeled as provisional or any other higher flag code). The associated
       value was computed using a pseudonormals approach or derived from monthly
       pseudonormals.
   Blank = the data value is reported as a special value such as -8888
