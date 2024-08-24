import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np

def hadlingAnomali(data,columns):
    df_filtered = data[data[columns].gt(0).any(axis=1)]
    return df_filtered


def detectingOutLayer(df , column):
    # Boxplot to check for outliers in GHI
    sb.boxplot(x=df[column])
    plt.title(f'{column} Boxplot')
    plt.show()

   
def IQRmethodOutliter(data,columns):
    Q1 = data[columns].quantile(0.25)
    Q3 = data[columns].quantile(0.75)
    IQR = Q3 - Q1

    # Filtering out outliers
    outliers = data[(data[columns] < (Q1 - 1.5 * IQR)) | 
                    (data[columns] > (Q3 + 1.5 * IQR))]
    sb.boxplot(data=data[columns])
    data[columns].hist(bins=30, figsize=(10, 8))
    plt.show()

def zScoreBaseOutliers(data, columns):
   
    z_scores = np.abs(stats.zscore(data[columns]))
    outliers = data[(z_scores > 3).any(axis=1)]
    return outliers


def daiylAnalysis(df):
    daily_data = df.resample('D').mean()  # 'D' stands for daily resampling

    plt.figure(figsize=(12, 6))
    plt.plot(daily_data.index, daily_data['GHI'], label='Daily GHI', color='orange')
    plt.plot(daily_data.index, daily_data['DNI'], label='Daily DNI', color='blue')
    plt.plot(daily_data.index, daily_data['DHI'], label='Daily DHI', color='green')
    plt.xlabel('Date')
    plt.ylabel('Irradiance (W/m²)')
    plt.title('Daily Solar Radiation Trends')
    plt.legend()
    plt.show()

    # return daily_data
    

def monthlyAnalysis(df):
    monthly_data = df.resample('M').mean()  # 'M' stands for monthly resampling
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data.index, monthly_data['GHI'], label='Monthly GHI', color='orange')
    plt.plot(monthly_data.index, monthly_data['DNI'], label='Monthly DNI', color='blue')
    plt.plot(monthly_data.index, monthly_data['DHI'], label='Monthly DHI', color='green')
    plt.xlabel('Month')
    plt.ylabel('Irradiance (W/m²)')
    plt.title('Monthly Solar Radiation Trends')
    plt.legend()
    plt.show()


def bubbleChart (df):

    plt.figure(figsize=(10, 6))
    sb.scatterplot(
        x='GHI', 
        y='Tamb', 
        size='BP',  # Bubble size
        hue='WS',   # Bubble color
        sizes=(20, 200),  # Range of bubble sizes
        palette='viridis',  # Color map for WS
        data=df,
        alpha=0.6
    )

    plt.title('Bubble Chart: GHI vs Tamb vs WS with Bubble Size Representing BP')
    plt.show()

