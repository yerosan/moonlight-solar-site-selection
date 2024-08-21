import pandas as pd
# import numpy as np
import seaborn as sb
import matplotlib.pyplot as mp


beninData="data/benin-malanville.csv"
sierraleoneData="data/sierraleone-bumbuna.csv"
togoData="data/togo-dapaong_qc.csv"


def main():
    try:
        #Loading data
        df=pd.read_csv(beninData)
        
        #Inspecting data
        
        print(f"Data structure: {df.info()}")
        print(f"Missing values: {df.isnull().sum()}")
        print(f"Basic statistics: {df.describe()}")

    except FileExistsError:
        print(f"Error: the was not found at {beninData}")
    except pd.errors.EmptyDataError:
        print("Error:The file is empty")
    except pd.errors.ParserError:
        print("Erro: There were a problem on parsing the file")
    except Exception as err:
        print(f" An unexpected error was occurred: {str(err)}")


if __name__=="__main__":
    main()