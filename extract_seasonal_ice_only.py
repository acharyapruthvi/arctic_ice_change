import netCDF4  as nc 
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

# ==============Setting up directory paths=========================
data_dir = 'data/north_pole'  # Directory where the NetCDF file is located

# =================Reading the NetCDF file=========================
rows = []
for filename in os.listdir(data_dir):
    if filename.endswith('.nc'):
        file_path = os.path.join(data_dir, filename)
        # Open the NetCDF file
        dataset = nc.Dataset(file_path, 'r')
        seasonal_ice_concentration = dataset.variables['cdr_seaice_conc_monthly'] # Access the variable
        actual_data = seasonal_ice_concentration[0, :, :]  # Extract the first time slice
        seasonal_ice_data = actual_data >= 0.5  # Convert to a NumPy array
        # area
        area = np.sum(seasonal_ice_data) / np.sum(actual_data >= 0) * 100  # Calculate the area of sea ice
        print(f"Area of sea ice for {filename}: {area}")

        time = os.path.basename(filename).split('_')[2]  # Extract the time from the filename
        year = time[:4]  # Extract the year from the time
        month = time[4:6]  # Extract the month from the time

        print(f"Year: {year}, Month: {month}")

        rows.append({'year': year, 'month': month, 'sea_ice_area_percentage': round(float(area), 4)})

        print(f"Processed {filename}: Year={year}, Month={month}, Sea Ice Area={area:.2f}%")
output_csv = os.path.join(data_dir, 'sea_ice_area.csv')
with open(output_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['year', 'month', 'sea_ice_area_percentage'])
    writer.writeheader()
    writer.writerows(rows)
print(f"CSV saved to {output_csv}")
