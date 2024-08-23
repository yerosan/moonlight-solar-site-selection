# Solar Radiation and Environmental Data Analysis

## Project Overview
This project focuses on performing Exploratory Data Analysis (EDA) and statistical analysis on solar radiation and environmental data. The primary objective is to derive actionable insights that can guide strategic solar investments by understanding patterns and trends in solar irradiance, temperature, wind speed, and other environmental factors. The analysis aims to support MoonLight Energy Solutions in identifying high-potential regions for solar installations, with an emphasis on sustainability.

## Deliverables

### 1. Summary Statistics
I calculate essential summary statistics such as mean, median, standard deviation, and other relevant metrics for key variables:

- **GHI (Global Horizontal Irradiance)**
- **DNI (Direct Normal Irradiance)**
- **DHI (Diffuse Horizontal Irradiance)**
- **Ambient Temperature (Tamb)**
- **Relative Humidity (RH)**
- **Wind Speed (WS, WSgust)**

These statistics provide a comprehensive understanding of the data distribution and central tendencies.

### 2. Data Quality Checks
I conduct thorough data quality checks to identify and address any issues, focusing on:

- **Negative values** in solar radiation metrics (GHI, DNI, DHI) that are physically incorrect.
- **Outlier detection** using the Interquartile Range (IQR) method and Z-Score method for variables such as ModA, ModB, and WS.

### 3. Time Series Analysis
I perform time series analysis to uncover patterns and trends over time, including:

- **Plotting GHI, DNI, DHI, and Tamb** over time to reveal daily and seasonal trends.
- **Evaluating the impact of cleaning events** on sensor readings (ModA, ModB) by analyzing the `Cleaning` column.

### 4. Correlation Analysis
I examine correlations between key variables specially the solar radidation and the enviromental variable to understand their interdependence, particularly:

- **GHI, DNI, DHI, and Tamb (Ambient Temperature)**
- **Wind Speed (WS, WSgust)** and solar irradiance components.

### 5. Data Cleaning
After identifying data anomalies such as negative values and outliers, I perform data cleaning to ensure the integrity and reliability of the dataset:

- **Removing negative values** in solar radiation metrics.
- **Handling missing values and outliers** to improve data quality.

### 6. Visualizations
I use various visualizations to communicate insights effectively:

- **Histograms**: Visualize the frequency distribution of solar radiation metrics and other environmental variables.
- **Scatter plots**: Analyze relationships between variables such as GHI vs. Tamb.
- **Heatmaps**: Examine correlations between different variables.
- **Time Series Plots**: Observe trends in solar irradiance and temperature over time.

## Repository Content
This repository contains the code, data, and documentation required for the analysis. The project is organized as follows:

<!-- - `data/`: Contains the raw and cleaned datasets. -->
- `notebooks/`: Jupyter notebooks with EDA, statistical analysis, and visualizations.
- `scripts/`: Python scripts used for data processing and analysis.
- `README.md`: Project overview and documentation (this file).
- `requirements.txt`: List of Python packages required to run the analysis.