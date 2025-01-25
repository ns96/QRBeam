import numpy as np
import matplotlib.pyplot as plt
import csv

# Function to generate UV-Vis absorption spectrum
def generate_absorption_spectrum(wavelengths, peak_wavelength, width):
    return np.exp(-0.5 * ((wavelengths - peak_wavelength) / width) ** 2)

# Function to generate emission spectrum
def generate_emission_spectrum(wavelengths, peak_wavelength, width):
    return np.exp(-0.5 * ((wavelengths - peak_wavelength) / width) ** 2)

# Wavelength range in nm
wavelengths = np.linspace(200, 800, 100)

# Absorption spectrum parameters
abs_peak = 450  # peak wavelength for absorption (nm)
abs_width = 75   # width of the absorption peak
absorption = generate_absorption_spectrum(wavelengths, abs_peak, abs_width)

# Emission spectrum parameters
ems_peak = 625  # peak wavelength for emission (nm)
ems_width = 100   # width of the emission peak
emission = generate_emission_spectrum(wavelengths, ems_peak, ems_width)

# Add randomness to the data
np.random.seed(42)  # For reproducibility
absorption += np.random.normal(0, 0.02, size=absorption.shape)
emission += np.random.normal(0, 0.02, size=emission.shape)

# Round data to 2 decimal places
absorption = np.round(absorption, 2)
emission = np.round(emission, 2)

# Plot the spectra
plt.figure(figsize=(8, 6))
plt.plot(wavelengths, absorption, label='Absorption', color='blue')
plt.plot(wavelengths, emission, label='Emission', color='red')
plt.title('Simulated UV-Vis Absorption and Emission Spectra')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (a.u.)')
plt.legend()
plt.grid()
plt.show()

# Export the data to a CSV file
output_file = "abs_ems.tsv"
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(["Wavelength (nm)", "Absorption (a.u.)", "Emission (a.u.)"])
    for wl, abs_val, ems_val in zip(wavelengths, absorption, emission):
        writer.writerow([round(wl, 2), abs_val, ems_val])

print(f"Data exported to {output_file}")
