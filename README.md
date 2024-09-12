# Moonlight solar site selection

## Introduction

Welcome to the Solar Radiation Measurement project! This repository is dedicated to analyzing solar irradiance data across different regions, particularly focusing on optimizing site selection for solar energy installations. The project utilizes a data-driven approach to evaluate the potential of various regions based on key solar irradiance metrics such as Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI).

## Features

- **Time Series Analysis**: Compare the monthly variations in GHI, DNI, and DHI across different regions.
- **Mean Value Analysis**: Evaluate the average performance of different regions based on key solar metrics.
- **Site Selection Recommendations**: Provide data-backed recommendations for optimal solar installation sites.
- **Seasonal Considerations**: Account for seasonal variations in solar irradiance when selecting and designing solar systems.

## Data and Methodology

The project analyzes solar irradiance data for three West African regions: **Benin**, **Togo**, and **Sierra Leone**. The analysis is carried out in two main steps:

1. **Time Series Analysis**: Monthly sampled data is used to observe trends and consistency in solar irradiance.
2. **Mean Value Analysis**: Key metrics are averaged to provide a clear picture of each region's overall potential for solar energy generation.

## Key Insights

- **Primary Sites**: Benin and Togo have the highest and most consistent GHI and DNI values, making them the top candidates for solar energy projects.
- **Secondary Site**: Sierra Leone, despite having lower GHI and DNI, shows stable performance and is suitable for specialized projects, such as off-grid or hybrid systems.
- **Seasonal Considerations**: Seasonal variations are analyzed to optimize system design and ensure year-round efficiency.

## Recommendations

Based on the analysis, the following recommendations are made:

1. **Prioritize Benin** for large-scale solar installations due to its superior solar irradiance metrics.
2. **Consider Togo** as a secondary option, particularly for Concentrated Solar Power (CSP) projects.
3. **Include Sierra Leone** for specialized or off-grid projects that can effectively utilize lower solar irradiance.

## How to Use

To use the scripts and notebooks in this repository:

1. Clone the repository:
    ```bash
    git clone https://github.com/yerosan/Solar_Radiation_Measurement.git
    ```
2. Navigate to the project directory:
    ```bash
    cd moonlight-solar-site-selection
    ```
3. Install the required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Jupyter notebooks or scripts to reproduce the analysis:
    ```bash
    jupyter notebook
    ```

## Conclusion

This repository provides valuable insights into solar site selection using a data-driven approach. By analyzing key solar irradiance metrics, this project helps guide strategic decisions in solar energy investments, ensuring maximum energy output and efficiency.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the project.

## Contact

For any inquiries or further information, please contact [yerosan](yerosan).
