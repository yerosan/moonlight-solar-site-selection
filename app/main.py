import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the dashboard
st.title("Solar Radiation Data Dashboard")

# File paths for the datasets
benin = "data/benin-malanville.csv"
togo = "data/togo-dapaong_qc.csv"
sierra_leone = "data/sierraleone-bumbuna.csv"

# Load dataset 

def load_data(site):
    if site == 'Benin':
        return pd.read_csv(benin)
    elif site == 'Togo':
        return pd.read_csv(togo)
    else:
        return pd.read_csv(sierra_leone)

# Dropdown for site selection
site_options = ['Benin', 'Togo', 'Sierra Leone']
selected_site = st.selectbox("Select a site to display its data:", site_options)
site_data = load_data(selected_site)

# Button for data cleaning actions
if st.button("Clean Data (Remove Comments, Negative Radiation Values)"):
    site_data = site_data.drop("Comments", axis=1)  # Remove 'Comments' column
    site_data = site_data[site_data['GHI'] > 0]
    site_data = site_data[site_data['DHI'] > 0]
    site_data = site_data[site_data['DNI'] > 0]
    st.success("Data cleaned successfully!")

# Show raw data
if st.checkbox(f"Show raw data for {selected_site}"):
    st.write(site_data.head())

# Key metrics
st.write("### Key Solar Radiation Metrics")
ghi_mean = site_data['GHI'].mean()
dni_mean = site_data['DNI'].mean()
dhi_mean = site_data['DHI'].mean()

st.write(f"**Average GHI:** {ghi_mean:.2f} W/m²")
st.write(f"**Average DNI:** {dni_mean:.2f} W/m²")
st.write(f"**Average DHI:** {dhi_mean:.2f} W/m²")

# Time series plot
st.write("### Time Series Plot: GHI, DNI, DHI")
site_data['Timestamp'] = pd.to_datetime(site_data['Timestamp'])
site_data.set_index('Timestamp', inplace=True)
fig = px.line(site_data, x=site_data.index, y=['GHI', 'DNI', 'DHI'], title=f'Solar Radiation Over Time ({selected_site})')
st.plotly_chart(fig)

# Correlation heatmap
st.write("### Correlation Heatmap")
corr_matrix = site_data[['GHI', 'DNI', 'DHI', 'Tamb', 'ModA', 'ModB']].corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# GHI filter
st.write("### Filter Data by GHI")
ghi_min, ghi_max = int(site_data['GHI'].min()), int(site_data['GHI'].max())
ghi_range = st.slider("Select GHI range:", min_value=ghi_min, max_value=ghi_max, value=(ghi_min, ghi_max))
filtered_data = site_data[(site_data['GHI'] >= ghi_range[0]) & (site_data['GHI'] <= ghi_range[1])]
st.write(f"Showing data with GHI between {ghi_range[0]} and {ghi_range[1]}")
st.write(filtered_data.head())

# Additional Visualization: Scatter plot of GHI vs. DNI
st.write("### Scatter Plot: GHI vs DNI")
scatter_fig = px.scatter(site_data, x='GHI', y='DNI', color='DHI', title='Scatter Plot of GHI vs DNI')
st.plotly_chart(scatter_fig)

# Bubble Chart: GHI vs Tamb vs WS with RH as bubble size
st.write("### Bubble Chart: GHI vs Tamb vs WS (Bubble Size = RH)")
if all(col in site_data.columns for col in ['GHI', 'Tamb', 'WS', 'RH']):
    bubble_fig = px.scatter(site_data, x='GHI', y='Tamb', size='RH', color='WS',
                            title='GHI vs Tamb vs WS with RH as Bubble Size')
    st.plotly_chart(bubble_fig)
else:
    st.warning("Required columns for bubble chart not found in the dataset.")
