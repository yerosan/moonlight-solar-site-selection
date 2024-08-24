import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from statsmodels.tsa.seasonal import seasonal_decompose
# from fbprophet import Prophet

# Function to load data from a CSV file
path="benin-malanville.csv"
def load_data(path):
    df = pd.read_csv(path, parse_dates=['Timestamp'], index_col='Timestamp')
    return df

# Streamlit application
st.title('Time Series Analysis Dashboard')

# File uploader
# uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# if uploaded_file is not None:
df = load_data(path)

st.write("Data Overview")
st.write(df.head())

# Time Series Plot
st.subheader('Time Series Plot')
fig, ax = plt.subplots()
ax.plot(df.index, df['GHI'], label='GHI')
ax.set_title('Time Series Plot')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend()
st.pyplot(fig)


# Run the Streamlit app
if __name__ == "__main__":
    st.write("Streamlit Dashboard Running")
