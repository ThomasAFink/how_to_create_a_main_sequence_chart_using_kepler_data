# How To Create a Main Sequence Chart Using Kepler Data

This repository showcases an in-depth analysis of data from the Kepler space telescope. The visualizations focus on the relationships between stellar characteristics, their classification, and the properties of their orbiting planets. This detailed exploration includes stellar temperature, magnitude, radius, estimated lifespans based on stellar mass, and the orbital periods of planets in relation to their host stars' temperatures. The Kepler mission has provided an unprecedented dataset for identifying exoplanets in our galaxy downloaded from Kaggle at https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results

## The Hertzsprung-Russell Diagram (H-R Diagram)

The Hertzsprung-Russell Diagram (H-R Diagram) is a pivotal tool introduced in beginner astrophysics that plots stars according to their brightness against their temperature. Developed independently by Ejnar Hertzsprung and Henry Norris Russell in the early 20th century, this diagram reveals the relationship between a star's temperature (or color) and its luminosity (or absolute magnitude).

In the H-R Diagram:
- The **x-axis** typically represents the star's surface temperature, decreasing from left to right (hot to cool).
- The **y-axis** shows the luminosity or absolute magnitude of the stars, with brighter stars at the top.

The diagram is famous for showing the main sequence, a continuous and distinctive band of stars that runs from the top left (hot, luminous stars) to the bottom right (cool, dim stars). This sequence reflects stars in the primary stage of their stellar evolution. The diagram also helps identify other stages of stellar evolution, such as giants, supergiants, and white dwarfs.

## Visualizations Overview

### Chart 1: Temperature vs. Kepler Magnitude

![Temperature vs. Kepler Magnitude](https://github.com/ThomasAFink/how_to_create_a_main_sequence_chart_using_kepler_data/blob/main/1_temperature_magnitude_main_seqeuence_diagram.jpg?raw=true)

**Description:**  
This chart plots the effective temperature of stars against their Kepler magnitude, categorized and color-coded by stellar classification. The Kepler magnitude, a measure of brightness as observed by the Kepler telescope, helps identify the luminosity and size of the stars. Stars with lower Kepler magnitudes are brighter, indicating larger or more luminous stars. The chart inversely plots magnitude to align with astronomical conventions, where brighter stars appear higher.

**Insights:**  
- The distribution reveals how stellar brightness correlates with temperature across different classifications.  
- Main Sequence stars show a wide range of temperatures but generally follow a distinct trend in brightness.

### Chart 2: Temperature vs. Stellar Radius with Log Scale

![Temperature vs. Stellar Radius](https://github.com/ThomasAFink/how_to_create_a_main_sequence_chart_using_kepler_data/blob/main/2_temperature_radius_main_seqeuence_diagram.jpg?raw=true)

**Description:**  
This visualization showcases the relationship between the effective temperature of stars and their radii, employing a logarithmic scale for the stellar radius to accommodate a wide range of values. The stellar radius, when plotted against temperature, provides insight into the physical size and evolutionary state of stars.

**Methodology:**  
- Stellar radius is a critical factor in determining a star's luminosity, as described by the Stefan-Boltzmann law:  
  ![Stefan-Boltzmann Law](https://latex.codecogs.com/png.latex?L%20%3D%204%5Cpi%20R%5E2%5Csigma%20T%5E4)  
  where \(L\) is luminosity, \(R\) is radius, \(\sigma\) is the Stefan-Boltzmann constant, and \(T\) is effective temperature.

**Insights:**  
- Larger radii are prevalent among cooler stars, indicative of Red Giants and Super Giants.  
- Main Sequence stars exhibit a narrower range of radii, highlighting their more uniform size in this phase of stellar evolution.

### Chart 3: Effective Temperature vs. Estimated Lifespan with Stellar Classifications

![Effective Temperature vs. Estimated Lifespan](https://github.com/ThomasAFink/how_to_create_a_main_sequence_chart_using_kepler_data/blob/main/3_temperature_estimated_lifespan_main_seqeuence_diagram.jpg?raw=true)

**Description:**  
This chart correlates the effective temperature of stars with their estimated lifespans, categorized by stellar classification. The estimation of lifespan is a key focus, which involves an indirect method to approximate the mass of stars since the dataset does not directly provide stellar masses.

**Methodology for Estimating Mass and Lifespan:**  
To estimate the masses of Main Sequence stars in the Kepler dataset, we utilize the stellar radius (`koi_srad`) and surface gravity (`koi_slogg`) for an indirect approximation. The formula for surface gravity is given by:

![Surface Gravity Equation](https://latex.codecogs.com/png.latex?g%20%3D%20%5Cfrac%7BG%20%5Ccdot%20M%7D%7BR%5E2%7D)

where:
- \(g\) is the surface gravity,
- \(G\) is the gravitational constant,
- \(M\) is the mass of the star,
- \(R\) is the radius of the star.

Rearranging this formula to solve for mass (\(M\)):

![Mass Equation](https://latex.codecogs.com/png.latex?M%20%3D%20%5Cfrac%7Bg%20%5Ccdot%20R%5E2%7D%7BG%7D)

This rearranged formula allows us to estimate each star's mass from its surface gravity and radius. Subsequently, we apply the mass-luminosity relationship to estimate lifespans:

![Lifespan Estimation](https://latex.codecogs.com/png.latex?Lifespan%20%3D%2010%20%5Ctimes%20%28M%29%5E%7B-3.5%7D)

where the lifespan is in billion years, and \(M\) is in solar masses. This relationship indicates that more massive stars, which are typically hotter, have shorter lifespans due to their faster hydrogen fusion rates.

**Insights:**  
- The plot illustrates the inverse relationship between a star's mass (inferred from temperature and luminosity) and its estimated lifespan, emphasizing how stellar classification impacts longevity.
- Main Sequence stars, depicted in the visualization, show a broad range of lifespans based on their mass and effective temperature, highlighting the diverse nature of stellar evolution.

By analyzing the effective temperature of stars alongside their estimated lifespans, this chart provides a window into the lifecycle of stars within the Main Sequence and beyond, underscoring the mass-luminosity relationship's role in determining stellar ages.

### Chart 4: Planet Orbital Period vs. Host Star Effective Temperature with Stellar Classifications

![Planet Orbital Period vs. Host Star Effective Temperature](https://github.com/ThomasAFink/how_to_create_a_main_sequence_chart_using_kepler_data/blob/main/4_planet_host_star_classification_main_seqeuence_diagram.jpg?raw=true)

**Description:**  
This chart examines the orbital periods of planets in relation to the effective temperature of their host stars, with each planet highlighted based on the classification of its host star. The chart explores how the characteristics of stars affect the orbital dynamics of their planets.

**Methodology:**  
- Orbital periods are plotted on a logarithmic scale to capture the wide range of observed values.  
- The effective temperature of the host star serves as a proxy for its mass and luminosity, factors that can influence planetary orbits.

**Insights:**  
- The distribution of orbital periods across different star types offers clues into the diversity of planetary systems.  
- Certain star classifications, particularly Main Sequence stars, host a wide variety of planetary systems with varying orbital periods. Many more planets have been detected around Main Sequence stars.

## Conclusion

The Kepler data visualizations provide a multifaceted view of the cosmos, highlighting the intricate relationships between stars and their planets. Through detailed analysis of stellar temperatures, magnitudes, radii, and estimated lifespans, we gain insights into the lifecycle of stars and the dynamic nature of their planetary systems.
