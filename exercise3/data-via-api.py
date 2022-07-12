
# https://hydrofunctions.readthedocs.io/en/latest/installation.html
# National Water Dashboard https://dashboard.waterdata.usgs.gov/app/nwd/?region=lower48&aoi=default

import pandas as pd
import hydrofunctions as hf
import matplotlib.pyplot as plt
%matplotlib inline

# flow 
daily_mean = hf.NWIS(site = '0208734210',service = 'dv',start_date='2016-01-01',end_date='2022-01-01')
daily_mean_values = daily_mean.df('q').shift(4, freq='H')

fig, ax = plt.subplots(figsize=(20, 10))
ax.step(daily_mean_values.loc['2016-01-01':'2022-01-01'].index.values, daily_mean_values.loc['2016-01-01':'2022-01-01'].values, where='post')
plt.yscale('log')
plt.show()

# peak flow
