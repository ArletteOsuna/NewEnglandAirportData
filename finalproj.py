"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (This Streamlit application allows users to explore data on New England airports through
summary statistics, interactive queries, and map visualizations.)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st
import pandas as pd
import pydeck as pdk


# Load the CSV file
@st.cache_data
def load_data():
    file_path = "new_england_airports.csv"  # file path
    return pd.read_csv(file_path)


data = load_data()

# Application Title
st.title("New England Airports Data Explorer")

# Sidebar for Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a Page:", ["Summary Report", "Airport Queries", "Map Visualization"])

# Summary Report
if options == "Summary Report":
    st.header("Summary Report")
    st.write("Here’s a summary of the data:")

    # basic statistics
    st.subheader("Basic Statistics")
    st.write(data.describe())

    # Airport counts by type
    st.subheader("Airport Counts by Type")
    airport_type_counts = data['type'].value_counts()
    st.bar_chart(airport_type_counts)

    # Elevation Statistics
    st.subheader("Elevation Analysis")
    st.write(f"Maximum Elevation: {data['elevation_ft'].max()} ft")
    st.write(f"Minimum Elevation: {data['elevation_ft'].min()} ft")
    st.write(f"Average Elevation: {data['elevation_ft'].mean():.2f} ft")

# Airport Queries
elif options == "Airport Queries":
    st.header("Airport Queries")

    # Filter by Airport Type
    airport_types = data['type'].unique()
    selected_type = st.selectbox("Filter by Airport Type:", airport_types)
    filtered_data_type = data[data['type'] == selected_type]
    st.subheader(f"Airports of Type: {selected_type}")
    st.write(filtered_data_type)

    # Search by Municipality
    municipality_query = st.text_input("Search Airports by Municipality:", "")
    if municipality_query:
        filtered_data_municipality = data[data['municipality'].str.contains(municipality_query, case=False, na=False)]
        st.subheader(f"Airports in Municipality: {municipality_query}")
        st.write(filtered_data_municipality)

    # Elevation Range Filter
    st.subheader("Filter Airports by Elevation Range")
    min_elevation, max_elevation = st.slider("Select Elevation Range (ft):", int(data['elevation_ft'].min()),
                                             int(data['elevation_ft'].max()), (0, 5000))
    filtered_data_elevation = data[(data['elevation_ft'] >= min_elevation) & (data['elevation_ft'] <= max_elevation)]
    st.write(f"Airports with Elevation between {min_elevation} and {max_elevation} ft:")
    st.write(filtered_data_elevation)

# Map Visualization
elif options == "Map Visualization":
    st.header("Map Visualization")

    # Prepare data for PyDeck Map
    map_data = data.dropna(subset=['latitude_deg', 'longitude_deg'])  # Remove rows without lat/lon
    map_data = map_data.rename(columns={'latitude_deg': 'lat', 'longitude_deg': 'lon'})

    # PyDeck Scatterplot Map
    st.subheader("PyDeck Scatterplot of Airports")
    scatterplot_layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        get_position='[lon, lat]',
        get_radius=500,
        get_fill_color='[200, 30, 0, 160]',
        pickable=True
    )

    # PyDeck Map Configuration
    view_state = pdk.ViewState(
        latitude=map_data['lat'].mean(),
        longitude=map_data['lon'].mean(),
        zoom=6,
        pitch=50
    )

    # Render PyDeck Map
    r = pdk.Deck(
        layers=[scatterplot_layer],
        initial_view_state=view_state,
        tooltip={"text": "{name} \nType: {type} \nMunicipality: {municipality}"}
    )
    st.pydeck_chart(r)
