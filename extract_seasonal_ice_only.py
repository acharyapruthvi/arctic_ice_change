import netCDF4  as nc 
import matplotlib.pyplot as plt

dataset = nc.Dataset('data/sic_psn25_197912_n07_v06r00.nc', 'r')

print(dataset.variables.keys())  # Print all variable names in the dataset

cdr_seaice_conc_monthly = dataset.variables['cdr_seaice_conc_monthly']  # Access the variable
print(cdr_seaice_conc_monthly[:])  # Print the variable details

plt.imshow(cdr_seaice_conc_monthly[0, :, :], cmap='jet')  # Display the first time slice
plt.colorbar(label='Sea Ice Concentration') 
plt.show()