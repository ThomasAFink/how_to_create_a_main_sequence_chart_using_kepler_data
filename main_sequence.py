import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
kepler_data = pd.read_csv('kepler.csv')

# Filter out stars with effective temperature > 12000 K and drop duplicates
filtered_stars = kepler_data[kepler_data['koi_steff'] <= 12000].drop_duplicates(subset='kepid', keep='first')

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
solar_mass = 1.98847e30  # Solar mass in kg
solar_radius = 6.95700e8  # Solar radius in meters

# Estimate mass and lifespan
filtered_stars['Estimated_Mass'] = (filtered_stars['koi_slogg'].apply(lambda x: 10**x) * 
                                    (filtered_stars['koi_srad'] * solar_radius)**2 / G) / solar_mass
filtered_stars['Estimated_Lifespan'] = 10 * (filtered_stars['Estimated_Mass'])**-3.5

# Categorizing stars
def categorize_star(row):
    if row['koi_slogg'] > 5.0:
        return 'White Dwarf'
    elif row['koi_slogg'] < 3.0:
        return 'Super Giant'
    elif row['koi_slogg'] < 3.5:
        return 'Red Giant'
    elif 4.0 <= row['koi_slogg'] <= 4.9:
        return 'Main Sequence'
    else:
        return 'Other'
filtered_stars['Category'] = filtered_stars.apply(categorize_star, axis=1)

# Plot settings
categories = ['Main Sequence', 'Red Giant', 'Super Giant', 'White Dwarf', 'Other']
colors = ['yellow', 'red', 'magenta', 'white', 'grey']
background_color = '#333333'
font_axis_color = '#fcfcfc'

# Apply general plot aesthetics
plt.rcParams['axes.facecolor'] = background_color
plt.rcParams['figure.facecolor'] = background_color
plt.rcParams['axes.edgecolor'] = font_axis_color
plt.rcParams['axes.labelcolor'] = font_axis_color
plt.rcParams['xtick.color'] = font_axis_color
plt.rcParams['ytick.color'] = font_axis_color
plt.rcParams['text.color'] = font_axis_color

# Plot 1: Temperature vs. Kepler Magnitude
plt.figure(figsize=(12, 8))
for category, color in zip(categories, colors):
    subset = filtered_stars[filtered_stars['Category'] == category]
    plt.scatter(subset['koi_steff'], subset['koi_kepmag'], label=category, color=color, alpha=0.5, marker='.')
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.title('Temperature vs. Kepler Magnitude from Kepler Data')
plt.xlabel('Effective Temperature (K)')
plt.ylabel('Kepler Magnitude')
plt.legend()
plt.grid(True, which="both", ls="--", color=font_axis_color)
plt.savefig("1_temperature_magnitude_main_seqeuence_diagram.jpg", dpi=1000)
plt.show()

# Plot 2: Temperature vs. Stellar Radius with Log Scale
plt.figure(figsize=(12, 8))
for category, color in zip(categories, colors):
    subset = filtered_stars[filtered_stars['Category'] == category]
    plt.scatter(subset['koi_steff'], subset['koi_srad'], label=category, color=color, alpha=0.5, marker='.')
plt.gca().invert_xaxis()
plt.yscale('log')
plt.title('Temperature vs. Stellar Radius from Kepler Data (Log Scale)')
plt.xlabel('Effective Temperature (K)')
plt.ylabel('Stellar Radius (Solar Radii) [Log Scale]')
plt.legend()
plt.grid(True, which="major", ls="--", color=font_axis_color)
plt.savefig("2_temperature_radius_main_seqeuence_diagram.jpg", dpi=1000)
plt.show()

# Plot 3: Effective Temperature vs. Estimated Lifespan with Stellar Classifications
plt.figure(figsize=(12, 8))
for category, color in zip(categories, colors):
    subset = filtered_stars[filtered_stars['Category'] == category]
    plt.scatter(subset['koi_steff'], subset['Estimated_Lifespan'], label=category, color=color, alpha=0.5, marker='.')
plt.gca().invert_xaxis()
plt.yscale('log')
plt.title('Effective Temperature vs. Estimated Lifespan with Stellar Classifications from Kepler Data (Log Scale)')
plt.xlabel('Effective Temperature (K)')
plt.ylabel('Estimated Lifespan (Billion Years) [Log Scale]')
plt.legend()
plt.grid(True, which="major", ls="--", color=font_axis_color)
plt.savefig("3_temperature_estimated_lifespan_main_seqeuence_diagram.jpg", dpi=1000)
plt.show()

# Plot 4: Plotting each planet with color coding based on the host star's classification
# Plotting Planet Orbital Time vs. Host Star Effective Temperature
plt.figure(figsize=(12, 8))

# Loop through categories to plot each classification separately to assign colors
for category, color in zip(categories, colors):
    # Filter the dataset for the current category
    subset = filtered_stars[filtered_stars['Category'] == category]
    # Scatter plot for each category
    plt.scatter(subset['koi_steff'], subset['koi_period'], label=category, color=color, alpha=0.5, marker='.')

plt.gca().invert_xaxis()  # Hotter stars on the left
plt.yscale('log')  # Log scale for planet orbital time to handle wide range of values
plt.title('Planet Orbital Time vs. Host Star Effective Temperature with Stellar Classifications')
plt.xlabel('Host Star Effective Temperature (K)')
plt.xlabel('Orbital Period (days)')
plt.legend()
plt.grid(True, which="major", ls="--", color=font_axis_color)
plt.savefig("4_planet_host_star_classification_main_seqeuence_diagram.jpg", dpi=1000)
plt.show()


