import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats

def statsticsSummary(dataFrame, column):
    for colms in column:
        sb.histplot(dataFrame[colms],kde=True)
        plt.title(f"{colms} data distribution")
        plt.show()
    return dataFrame.describe()
def timeSerieAnalysis(df):
    plt.figure(figsize=(14, 8))
    plt.plot(df.index, df['GHI'], label='GHI', color='blue')
    plt.plot(df.index, df['DNI'], label='DNI', color='orange')
    plt.plot(df.index, df['DHI'], label='DHI', color='green')
    plt.plot(df.index, df['Tamb'], label='Ambient Temperature (Tamb)', color='red')
    plt.xlabel('Time')
    plt.ylabel('Values (W/m² or °C)')
    plt.title('Time Series of Solar Radiation Metrics and Temperature')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def cleaningEffect(df):
    plt.figure(figsize=(14, 8))

    plt.plot(df.index, df['ModA'], label='ModA', color='purple')
    plt.plot(df.index, df['ModB'], label='ModB', color='green')


    cleaning_times = df[df['Cleaning'] == 1].index  

    for cleaning_time in cleaning_times:
        plt.axvline(x=cleaning_time, color='black', linestyle='--', linewidth=0.7)

    plt.xlabel('Time')
    plt.ylabel('Sensor Readings (W/m²)')
    plt.title('Sensor Readings (ModA, ModB) and Cleaning Events')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


