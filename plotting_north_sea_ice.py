import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import pandas as pd

# Load the data
data = pd.read_csv('sea_ice_area.csv')

years = sorted(data['year'].unique())
cmap = cm.viridis
norm = mcolors.Normalize(vmin=min(years), vmax=max(years))

fig, ax = plt.subplots()
for year in years:
    year_data = data[data['year'] == year].sort_values('month')
    ax.plot(year_data['month'], year_data['sea_ice_area_percentage'], color=cmap(norm(year)))

sm = cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm, ax=ax, label='Year')
ax.set_xlabel('Month')
ax.set_ylabel('Sea Ice Area Percentage')
plt.show()