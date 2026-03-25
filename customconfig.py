# global variables for the analysis
directory = 'your_data_directory' # customize this

# customize number of rolling periods
ant_years = 1 # antecedent years to include (2 antecedent years + current year)
ant_season = 3 # n+1 of months to include in each period (e.g. input 2 would mean 3 months)

firstyear = 1984 # first year of data
finalyear = 2022 # final year of data (should be same as burned area)

# skip analysis for these (these are used after the models are run, only used for creating figures)
noforestmodels = ['ecoprov1','ecoprov3',
                  'ecoprov7','ecoprov18','ecoprov21']
nononforestmodels = []
print('MANUALLY DEFINED, no forest models:')
print(noforestmodels)
print('MANUALLY DEFINED, no nonforest models:')
print(nononforestmodels)

# create strings of the types of forests, remove #11
province_names = ['1: American Semi-Desert and Desert Province',
                  '2: Arizona-New Mexico Mountains Semi-Desert-Open Woodland-Coniferous Forest-Alpine Meadow Province',
                  '3: Black Hills Coniferous Forest Province',
                  '4: California Coastal Chapparral Forest and Shrub Province',
                  '5: California Coastal Range Open Woodland-Shrub-Coniferous Forest-Meadow Province',
                  '6: California Coastal Steppe-Mixed Forest-Redwood Forest Province',
                  '7: California Dry Steppe Province',
                  '8: Cascade Mixed Forest-Coniferous Forest-Alpine Meadow Province',
                  '9: Chihuahuan Semi-Desert Province',
                  '10: Colorado Plateau Semi-Desert Province',
                  '12: Great Plains-Palouse Dry Steppe Province',
                  '13: Intermountain Semi-Desert Province',
                  '14: Intermountain Semi-Desert and Desert Province',
                  '15: Middle Rocky Mountain Steppe-Coniferous Forest-Alpine Meadow Province',
                  '16: Nevada-Utah Mountains-Semi-Desert-Coniferous Forest-Alpine Meadow Province',
                  '17: Northern Rocky Mountain Forest-Steppe-Coniferous Forest-Alpine Meadow Province',
                  '18: Pacific Lowland Mixed Forest Province',
                  '19: Sierran Steppe-Mixed Forest-Coniferous Forest-Alpine Meadow Province',
                  '20: Southern Rocky Mountain Steppe-Open Woodland-Coniferous Forest-Alpine Meadow Province',
                  '21: Southwest Plateau and Plains Dry Steppe and Shrub Province']

# ecoregion names removing the ones not used for analysis
# this is the label printed on everything
prov_abbr_names = ['0: All western US',
                  '1: American Semi-Desert',
                  '2: AZ-NM Mountains',
                  'x: Black Hills Coniferous Forest',
                  '3: CA Coast Chapparral Forest',
                  '4: CA Coast Range Open Woodland',
                  'x: California Coastal Steppe-Redwood',
                  '5: CA Dry Steppe Province',
                  '6: Cascade Mixed Forest',
                  '7: Chihuahuan Semi-Desert',
                  '8: CO Plateau',
                  '9: Great Plains',
                  '10: IM Semi-Desert',
                  '11: IM Semi-Desert and Desert',
                  '12: Middle Rocky Mountain Steppe',
                  '13: NV-UT Mountains',
                  '14: Northern Rocky Mountain Forest',
                  'x: Pacific Lowland Mixed Forest Province',
                  '15: Sierran Steppe',
                  '16: Southern Rocky Mountain Steppe',
                  '17: SW Plateau and Plains']

# ecoregion names removing the ones we don't care about
# this is the label printed on everything
prov_label_names = ['1: American Semi-Desert',
                  '2: AZ-NM Mountains',
                  '3: CA Coast Chapparral Forest',
                  '4: CA Coast Range Open Woodland',
                  '5: CA Dry Steppe Province',
                  '6: Cascade Mixed Forest',
                  '7: Chihuahuan Semi-Desert',
                  '8: CO Plateau',
                  '9: Great Plains',
                  '10: IM Semi-Desert',
                  '11: IM Semi-Desert and Desert',
                  '12: Middle Rocky Mountain Steppe',
                  '13: NV-UT Mountains',
                  '14: Northern Rocky Mountain Forest',
                  '15: Sierran Steppe',
                  '16: Southern Rocky Mountain Steppe',
                  '17: SW Plateau and Plains']

# long-form names
province_names = ['American Semi-Desert and Desert Province',
                  'Arizona-New Mexico Mountains Semi-Desert-Open Woodland-Coniferous Forest-Alpine Meadow Province',
                  'Black Hills Coniferous Forest Province',
                  'California Coastal Chapparral Forest and Shrub Province',
                  'California Coastal Range Open Woodland-Shrub-Coniferous Forest-Meadow Province',
                  'California Coastal Steppe-Mixed Forest-Redwood Forest Province',
                  'California Dry Steppe Province',
                  'Cascade Mixed Forest-Coniferous Forest-Alpine Meadow Province',
                  'Chihuahuan Semi-Desert Province',
                  'Colorado Plateau Semi-Desert Province',
                  'Great Plains-Palouse Dry Steppe Province',
                  'Intermountain Semi-Desert Province',
                  'Intermountain Semi-Desert and Desert Province',
                  'Middle Rocky Mountain Steppe-Coniferous Forest-Alpine Meadow Province',
                  'Nevada-Utah Mountains-Semi-Desert-Coniferous Forest-Alpine Meadow Province',
                  'Northern Rocky Mountain Forest-Steppe-Coniferous Forest-Alpine Meadow Province',
                  'Pacific Lowland Mixed Forest Province',
                  'Sierran Steppe-Mixed Forest-Coniferous Forest-Alpine Meadow Province',
                  'Southern Rocky Mountain Steppe-Open Woodland-Coniferous Forest-Alpine Meadow Province',
                  'Southwest Plateau and Plains Dry Steppe and Shrub Province']


province_num = [item for item in range(len(province_names)+1+1)]
province_num.remove(11) # remove empty ecoregion - no overlap btwn westUS map and ecoregion
dfnames = ['allwestUS', 'ecoprov1', 'ecoprov2', 'ecoprov3', 'ecoprov4', 'ecoprov5', 
           'ecoprov6', 'ecoprov7', 'ecoprov8', 'ecoprov9', 'ecoprov10', 
           'ecoprov12','ecoprov13','ecoprov14','ecoprov15',
           'ecoprov16','ecoprov17','ecoprov18','ecoprov19','ecoprov20','ecoprov21']