"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st
import pandas as pd
import pydeck as pdk

# [PY3] Error checking with try/except
# [DA1] Clean the data: Load the data and handle potential errors
@st.cache_data
def load_data(file_path="new_england_airports.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
        return pd.DataFrame()  # Empty DataFrame as fallback


# Load data
data = load_data()

# Avoid mutating cached data
if not data.empty:
    # [DA9] Add a new column or perform calculations on a DataFrame column
    modified_data = data.copy()
    modified_data['elevation_m'] = modified_data['elevation_ft'].apply(lambda x: x * 0.3048 if pd.notna(x) else None)

# Application Title
st.title("New England Airports Data Explorer")

# [ST4] Sidebar for Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a Page:", ["Summary Report", "Airport Queries", "Map Visualization"])

# Summary Report
if options == "Summary Report":
    st.header("Summary Report")
    st.write("Here’s a summary of the data:")

    # [VIZ1] Basic statistics as a table
    st.subheader("Basic Statistics")
    st.write(modified_data.describe())

    # [DA7] Group data and count by airport type
    # [VIZ2] Bar chart visualization
    st.subheader("Airport Counts by Type")
    airport_type_counts = modified_data['type'].value_counts()
    st.bar_chart(airport_type_counts)

    # [DA3] Find the maximum, minimum, and average of a column
    st.subheader("Elevation Analysis")
    st.write(f"Maximum Elevation: {modified_data['elevation_ft'].max()} ft")
    st.write(f"Minimum Elevation: {modified_data['elevation_ft'].min()} ft")
    st.write(f"Average Elevation: {modified_data['elevation_ft'].mean():.2f} ft")

# Airport Queries
elif options == "Airport Queries":
    st.header("Airport Queries")

    # [ST1] Selectbox widget
    airport_types = modified_data['type'].unique()
    selected_type = st.selectbox("Filter by Airport Type:", airport_types)
    filtered_data_type = modified_data[modified_data['type'] == selected_type]
    st.subheader(f"Airports of Type: {selected_type}")
    st.write(filtered_data_type)

    # [ST2] Text input widget
    municipality_query = st.text_input("Search Airports by Municipality:", "")
    if municipality_query:
        # [DA4] Filter data by one condition
        filtered_data_municipality = modified_data[
            modified_data['municipality'].str.contains(municipality_query, case=False, na=False)
        ]
        st.subheader(f"Airports in Municipality: {municipality_query}")
        st.write(filtered_data_municipality)

    # [ST3] Slider widget
    st.subheader("Filter Airports by Elevation Range")
    min_elevation, max_elevation = st.slider(
        "Select Elevation Range (ft):",
        int(modified_data['elevation_ft'].min()),
        int(modified_data['elevation_ft'].max()),
        (0, 5000)
    )
    # [DA5] Filter data by two conditions with AND
    filtered_data_elevation = modified_data[
        (modified_data['elevation_ft'] >= min_elevation) & (modified_data['elevation_ft'] <= max_elevation)
    ]
    st.write(f"Airports with Elevation between {min_elevation} and {max_elevation} ft:")
    st.write(filtered_data_elevation)

# Map Visualization
elif options == "Map Visualization":
    st.header("Map Visualization")

    # [DA6] Clean and prepare data for mapping
    map_data = modified_data.dropna(subset=['latitude_deg', 'longitude_deg']).rename(
        columns={'latitude_deg': 'lat', 'longitude_deg': 'lon'}
    )

    # [MAP] PyDeck Scatterplot Map
    st.subheader("PyDeck Scatterplot of Airports")
    scatterplot_layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        get_position='[lon, lat]',
        get_radius=500,
        get_fill_color='[200, 30, 0, 160]',
        pickable=True
    )

    # [VIZ3] PyDeck Map with tooltips
    view_state = pdk.ViewState(
        latitude=map_data['lat'].mean(),
        longitude=map_data['lon'].mean(),
        zoom=6,
        pitch=50
    )

    r = pdk.Deck(
        layers=[scatterplot_layer],
        initial_view_state=view_state,
        tooltip={"text": "{name} \nType: {type} \nMunicipality: {municipality}"}
    )
    st.pydeck_chart(r)
