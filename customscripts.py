# global scripts for all files
import numpy as np
from customconfig import *

def in_forest(variable, thisregion):
    """
    For getting the average values only in a forest area.
    Requirements: the forest netCDF.
    Returns one weighted average of the variable for each timestep.
    """
    forestregion = forest*thisregion # get in the region
    weightedsum = (variable*(forestregion)).sum(dim=['X','Y'], skipna=True)
    forestsum = (forestregion).sum()
    return  weightedsum / forestsum


def in_nonforest(variable, thisregion):
    """
    For getting the average values only in a nonforested area in the western US.
    Requirements: the forest netCDF, a mask of the western US.
    Returns one weighted average of the variable for each timestep and the selected region.
    """
    nonforestregion = nonforest*thisregion # get in the region
    weightedsum = (variable*(nonforestregion)).sum(dim=['X','Y'], skipna=True)
    nonforestsum = (nonforestregion).sum()
    return  weightedsum / nonforestsum

# just format the name of the climate variable
def suppnameformat(plotvarname):
    """
    Input is `plotvarname`, which is the climate name as it is formatted in the 
    pandas dataframe, but just the name and no month or year. (e.g. prec, vpd, rh)
    Reformat the name of the climate plus include units.
    Returns [fullname, timeseries, units]
    """
    plotvarname = plotvarname.capitalize()
    # color palette: "omni spring pastels" from https://www.heavy.ai/blog/12-color-palettes-for-telling-better-stories-with-your-data
    colorpalette = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7"]
    # fix names, assign units and color
    if 'Vpd' in plotvarname:
        plotvarname = 'VPD'
        units = 'hPa'
        color = colorpalette[0]
    elif 'Prec' in plotvarname:
        plotvarname = 'Precipitation'
        units = 'mm'
        color = colorpalette[1]
    elif 'Rh' in plotvarname:
        plotvarname = 'RH'
        units = '%'
        color = colorpalette[2]
    elif 'Wetdays' in plotvarname:
        plotvarname = 'Wet_days'
        units = 'fraction of days >2.54 mm'
        color = colorpalette[3]
    elif 'Solar' in plotvarname:
        plotvarname = 'Solar_radiation'
        units = 'W/m$^2$'
        color = colorpalette[4]
    elif 'Tmax' in plotvarname:
        units = '$\degree$C'
        color = colorpalette[5]
    elif 'Tmin' in plotvarname:
        units = '$\degree$C'
        color = colorpalette[6]
    elif 'Wind' in plotvarname:
        units = 'm/s'
        color = colorpalette[7]
    elif 'Tmean' in plotvarname:
        plotvarname = 'Tmean'
        units = '$\degree$C'
        color = colorpalette[8]
    elif 'Gsst' in plotvarname:
        plotvarname = 'gSST'
        units = '$\degree$C'
        color = 'k'
    return plotvarname, units, color

# format plot script
def suppclimplotformat(variablename):
    """
    Input is `variablename`, which is the climate name as it is formatted in the pandas dataframes
    (e.g. prec y0 mo 1-3, or "variable_name year month month-numbers"). 
    Reformat the name of the plot, and also provide the unit labels and timeseries 
    for the y-axis of the plot.
    Returns [fullname, timeseries, units] (e.g. Precipitation y-0 JFM, 1984-2022, mm)
    """
    varsplit = variablename.split(' ')
    plotvaryear = varsplit[1] # y0 or y-1
    plotvarmo = varsplit[3] # month numbers
    # fix names
    plotvarname, units, color = suppnameformat(varsplit[0])

    # fix months
    if '1-3' in varsplit[3]:
        plotvarmo = 'JFM'
    elif '4-6' in varsplit[3]:
        plotvarmo = 'AMJ'
    elif '7-9' in varsplit[3]:
        plotvarmo = 'JAS'
    elif '10-12' in varsplit[3]:
        plotvarmo = 'OND'

    # fix years
    if 'y0' in varsplit[1]:
        timeseries = np.arange(firstyear, finalyear+1)
        plotvaryear = 'y-0'
    elif 'y-1' in varsplit[1]:
        timeseries = np.arange(firstyear-1, finalyear)

    fullname = plotvarname + ' ' + plotvaryear + ',' + plotvarmo
    return fullname, timeseries, units

# printing significance
def addSigMarker(pvalue):
    """
    Add an asterisk for values that are significant.
    p<0.05, add *
    p<0.01, add **
    otherwise add an empty space
    """
    if pvalue<0.01:
        adddot = '**' # significance marker
    elif pvalue<0.05:
        adddot = '*'# add significance marker
    else:
        adddot = ' ' # no significance
    return adddot


# average climate variables, within a selected season

def annual_seasonAvg(data, firstmonth, finalmonth):
    """
    This intakes an array of current ecoregion's climate variable of monthly averages (data), 
    Output: an array of yearly averages of the ecoregion climate variable, in the
    seasons specified (firstmonth, finalmonth).
    Requirements: time = an xarray timeseries of months in datetime format.
    """
    withinyear = (time['time.year']>= years[0]) & (time['time.year'] <= years[-1])
    withinseason = (time['time.month'] >= firstmonth) & (time['time.month'] <= finalmonth)
    thistime = time[withinseason & withinyear] # cut time

    # create pd dataframe based on data, for time resampling
    thisdf = pd.DataFrame({'time': pd.to_datetime(thistime.values), 'clim':data[withinyear & withinseason]}).set_index('time')
    thisdf = thisdf.resample('Y').mean().reset_index()
    return thisdf.clim.values


