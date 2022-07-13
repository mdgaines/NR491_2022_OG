
# https://hydrofunctions.readthedocs.io/en/latest/installation.html
# National Water Dashboard https://dashboard.waterdata.usgs.gov/app/nwd/?region=lower48&aoi=default

import pandas as pd
import hydrofunctions as hf
import matplotlib.pyplot as plt
%matplotlib inline

# general objects
site_no = '0208734210'
service = 'dv'
st_date = '2021-01-01'
end_date = '2022-01-01'

# flow ft3/s
daily_mean = hf.NWIS(site=site_no, service=service, start_date=st_date, end_date=end_date)
daily_mean_values = daily_mean.df('q').shift(4, freq='H')

# plotting
fig, ax = plt.subplots(figsize=(10, 8))
ax.step(daily_mean_values.loc[st_date:end_date].index.values, daily_mean_values.loc[st_date:end_date].values, where='post')
plt.yscale('log')
plt.ylabel('Log scaled streamflow (ft3/s)')
plt.title(f'USGS station:{site_no}.')
plt.show()


from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2021, 1, 1)
end = datetime(2021, 12, 31)

# Create Point for Vancouver, BC
vancouver = Point(35.765397, -78.685035)

# Get daily data for 2018
data = Daily(vancouver, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()

data['prcp'].plot()