# Juang-gSST-Fires
Statistical estimation of the contribution of the La Nina-like Pacific Ocean trend in sea-surface temperatures to western United States wildfire area in 1984-2022. This is the open code for our model.

# Citing this code
Please cite our manuscript and the code.

* Juang, C. S. (2026). Code for Contribution of La-Niña-like Pacific Ocean trend in sea-surface temperatures to western United States wildfire area, 1984–2022. _Zenodo_. Retrieved (date). https://doi.org/10.5281/zenodo.18930095

# Manuscript
Under review.

* Juang, C. S., Williams, A.P., Seager, R. (2026). Contribution of La-Niña-like Pacific Ocean trend in sea-surface temperatures to western United States wildfire area, 1984-2022. _Under review_.

# How to use this statistical model

## Data

Data are obtained from the following sources and regridded into 12 km resolution, projected into Albers Equal Area (epsg:5070).
1. Sea-surface temperature; MEI, PDO, SOI indices: from NOAA Physical Sciences Laboratory
2. Climate: Precipitation, wet-day frequency, daily maximum temperature (Tmax), daily minimum temperature (Tmin) from the NOAA nClimGrid daily dataset.
3. Climate: Vapor pressure deficit calculated from saturation vapor pressure minus actual vapor pressure. Vapor pressure was calculated from daily dew point data from the Oregon State PRISM group (Daly et al., 2021) using the Clausius-Clapeyron formula. Saturation vapor pressure was calculated at the daily timestep as the average of saturation vapor pressure at Tmax and Tmin.
4. Climate: Solar radiation and wind-speed data are from dynamically downscaled ERA5 reanalysis (Rahimi et al., 2022).
5. Area burned: from WUMI2 (Juang & Williams, 2024; Juang et al., 2022).
6. Area burned: from MODIS (Giglio et al., 2016).

## Update the data and prepare the data for the models


## Train the models


## Analyze and produce manuscript figures



# Contact

* Caroline S. Juang, c.juang@columbia.edu