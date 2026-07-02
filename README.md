# Juang-gSST-Fires
Statistical estimation of the contribution of the La Nina-like Pacific Ocean trend in sea-surface temperatures to western United States wildfire area in 1984-2022. This is the open code for our model.

# Citing this code
Please cite our manuscript and the code.

* Juang, C. S. (2026). Code for Contribution of La-Niña-like Pacific Ocean trend in sea-surface temperatures to western United States wildfire area, 1984–2022. _Zenodo_. Retrieved (date). https://doi.org/10.5281/zenodo.19224438

# Manuscript
Under review.

* Juang, C. S., Williams, A.P., Seager, R. (2026). Contribution of La-Niña-like Pacific Ocean trend in sea-surface temperatures to western United States wildfire area, 1984-2022. _Under review_.

# How to use this statistical model

## Data
Data are obtained from the following sources and regridded into 12 km resolution, projected into Albers Equal Area (epsg:5070). Please see the Methods in the manuscript for more detail.
1. Sea-surface temperature; MEI, PDO, SOI indices: from NOAA Physical Sciences Laboratory.
2. Climate: Precipitation, wet-day frequency, daily maximum temperature (Tmax), daily minimum temperature (Tmin) from the NOAA nClimGrid daily dataset.
3. Climate: Vapor pressure deficit calculated from saturation vapor pressure minus actual vapor pressure. Vapor pressure was calculated from daily dew point data from the Oregon State PRISM group (Daly et al., 2021) using the Clausius-Clapeyron formula. Saturation vapor pressure was calculated at the daily timestep as the average of saturation vapor pressure at Tmax and Tmin.
4. Climate: Solar radiation and wind-speed data are from dynamically downscaled ERA5 reanalysis (Rahimi et al., 2022).
5. Area burned: from WUMI2 (Juang & Williams, 2024; Juang et al., 2022).
6. Area burned: from MODIS (Giglio et al., 2016).

## Update the data and prepare the data for the models
1. Summarize area burned in WUMI2 and extend it with MODIS using **data/Ecoprovinces_ExtendData**
2. Format climate indices using **data/Data_CreateENSOIndex** and **data/Data_CreateModelData**. This will build the SST gradient (gSST), MEI, SOI, and PDO. 
3. Set up even more SST indices by manually changing the `climindname` in **Data_CreateModelData-gSST** and rerunning the notebook for each index.

## Train the models
Note: you can update all of the models and analysis figures at once using **Run_updateModel**. You will need to run it in several parts following the methods in the file, because some things need to be manually updated.
1. Change the climate index used for the gSST in the file **0_climindname.txt**
2. Run **Model_ENSOclim_CoeffCheck** and **Model_ENSOclim_CoeffCheck-avg**
3. Run **Model_ENSOclim_AkaikeCoeff** to input observed gSST and climate and output the models to predict the climate variables. 
4. Run **Model_Akaike** to input observed climate and area burned and output the models to predict the area burned.

## Predict area burned
After models are trained, do not retrain them unless retraining with a different gSST.
1. Change the right gSST in **0_climindname.txt**.
2. Run **Model_ENSOfull12-2022**. This will output the burned area predictions.
3. Run **Model_ENSOpredictclim** and **Model_ENSOfullclim12-2025**, which will output the climate predictions under a detrended SST gradient.
4. Perform cross-validation on the model with **Model_Akaike_CrossValid**
5. Perform experiments holding some variables constant to understand their contribution, by running **Model_ENSOfull12-2022-holdconstant**

## Analyze and produce manuscript figures
1. Produce gSST and climate-related figures in **Model_analysisv5**
3. Produce burned area figures is **Model_analysisv5-BAFigs**
4. Produce Supplemental info figures in **Model_analysisv5-Suppl**
5. Produce Supplemental info figures for SOI, MEI, PDO: rerun **Run_updateModel** with the correct climate index by changing **0_climindname.txt**
6. Supplemental info figures of original model but hold everything constant except for specific variables:
    * **Model_analysisv5-BAFigs-priorwettingonly**
    * **Model_analysisv5-BAFigs-warmingvarsonly**
    * **Model_analysisv5-BAFigs-y0wettingonly**
7. Produce supplemental info figures with a sensitivity analysis, moving gSST by 2 degrees in every cardinal direction: **Model_analysisv5-BAFigs-nudging**

# Climate Indices List
For defining in **0_climindname.txt**. These are created in **data/Data_CreateENSOIndex** and **data/Data_CreateModelData**.
* 'patch125-155_nino3-34' (**the SST gradient**), (125-155 deg lon) - nino3.4 + nino3 (190-270 deg)
* 'pdo_noaa' (Pacific Decadal Oscillation (PDO) index, from NOAA ERSSTv5)
* 'mei_noaa' (Multivariate ENSO (El Nino Southern Oscillation) Index)
* 'soi_noaa' (Southern Oscillation Index, SOI)

Nudged indicies for sensitivity tests:
* 'patch125-155_nino3-34a': nudge up (northward)
* 'patch125-155_nino3-34b': nudge down (southward)
* 'patch125-155_nino3-34c': nudge to the left (westward)
* 'patch125-155_nino3-34d': nudge to the right (eastward)

Alternate SSTs (for comparing SST data sources):
* 'patch125-155_nino3-34_COBEv2': from Japan Meteorological Agency, COBE-SST v2
* 'patch125-155_nino3-34_HadISST1': from Met Office Hadley Centre, HadISST1


# Contact

* Caroline S. Juang, c.juang@columbia.edu
* Google Scholar profile: https://scholar.google.com/citations?user=jKoNVJgAAAAJ

* January 2022 to July 2026