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
    return outliers

def zScoreBaseOutliers(data, columns):
   
    z_scores = np.abs(stats.zscore(data[columns]))
    outliers = data[(z_scores > 3).any(axis=1)]
    return outliers