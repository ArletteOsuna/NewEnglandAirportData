"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st
import pandas as pd
import pydeck as pdk
import seaborn as sns
import matplotlib.pyplot as plt


# [PY3] Error checking with try/except
# [DA1] Clean the data
@st.cache_data
def load_data(file_path="new_england_airports.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
        return pd.DataFrame()  # Empty DataFrame for fallback


data = load_data()

# [DA9] Add a new column or perform calculations on DataFrame column
if not data.empty:
    data['elevation_m'] = data['elevation_ft'].apply(
        lambda x: x * 0.3048 if pd.notna(x) and isinstance(x, (int, float)) else None
    )

# [PY1] Function with two or more parameters, one with a default value
def filter_airports_by_type(data, airport_type="small_airport"):
    return data[data['type'] == airport_type]


# [PY2] Function that returns more than one value
def elevation_stats(data):
    return data['elevation_ft'].max(), data['elevation_ft'].min(), data['elevation_ft'].mean()


# [ST4] Customized page design features
st.title("New England Airports Data Explorer")
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a Page:", ["Summary Report", "Airport Queries", "Map Visualization"])

# Summary Report
if options == "Summary Report":
    st.header("Summary Report")
    st.write("Below is a summary of the New England Airports data:")

    # [VIZ1] Basic statistics table
    st.subheader("Basic Statistics")
    st.write(data.describe())

    # [VIZ2] Bar chart visualization
    st.subheader("Airport Counts by Type")
    airport_type_counts = data['type'].value_counts()
    st.bar_chart(airport_type_counts)

    # [PY2] Using a function that returns multiple values
    st.subheader("Elevation Analysis")
    max_elev, min_elev, avg_elev = elevation_stats(data)
    st.write(f"Maximum Elevation: {max_elev} ft")
    st.write(f"Minimum Elevation: {min_elev} ft")
    st.write(f"Average Elevation: {avg_elev:.2f} ft")

    # [DA2 + DA6] Combined: Sort and Analyze Data with Pivot Table
    st.subheader("Elevation by Airport Type (Sorted by Max Elevation)")
    pivot_table = data.pivot_table(
        index='type',
        values='elevation_ft',
        aggfunc=['max', 'min', 'mean']
    ).reset_index()

    pivot_table.columns = ['Airport Type', 'Max Elevation (ft)', 'Min Elevation (ft)', 'Mean Elevation (ft)']

    # Sort pivot table by Max Elevation
    sorted_pivot_table = pivot_table.sort_values(by='Max Elevation (ft)', ascending=False)

    st.write(sorted_pivot_table)
# Airport Queries
elif options == "Airport Queries":
    st.header("Airport Queries")

    # [ST1] Dropdown widget
    airport_types = data['type'].unique()
    selected_type = st.selectbox("Filter by Airport Type:", airport_types)

    # [PY1] Calling function with default and custom parameters
    filtered_data_type = filter_airports_by_type(data, selected_type)
    st.subheader(f"Airports of Type: {selected_type}")
    st.write(filtered_data_type)

    # [ST2] Text input widget
    municipality_query = st.text_input("Search Airports by Municipality:", "")
    if municipality_query:
        # [DA4] Filter data by one condition
        filtered_data_municipality = data[data['municipality'].str.contains(municipality_query, case=False, na=False)]
        st.subheader(f"Airports in Municipality: {municipality_query}")
        st.write(filtered_data_municipality)

    # [ST3] Slider widget
    st.subheader("Filter Airports by Elevation Range")
    min_elevation, max_elevation = st.slider("Select Elevation Range (ft):", int(data['elevation_ft'].min()),
                                             int(data['elevation_ft'].max()), (0, 5000))
    # [DA5] Filter data by two or more conditions
    filtered_data_elevation = data[(data['elevation_ft'] >= min_elevation) & (data['elevation_ft'] <= max_elevation)]
    st.write(f"Airports with Elevation between {min_elevation} and {max_elevation} ft:")
    st.write(filtered_data_elevation)

    # [PY5] Using a dictionary
    st.subheader("Airport Type Dictionary")
    airport_type_dict = {row['id']: row['type'] for _, row in data.iterrows()}
    st.write(f"Airport Types: {list(airport_type_dict.values())[:10]}")  # Display first 10 types

# Map Visualization
elif options == "Map Visualization":
    st.header("Map Visualization")

    # [MAP] PyDeck map with tooltips
    map_data = data.dropna(subset=['latitude_deg', 'longitude_deg'])
    map_data = map_data.rename(columns={'latitude_deg': 'lat', 'longitude_deg': 'lon'})

    scatterplot_layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        get_position='[lon, lat]',
        get_radius=500,
        get_fill_color='[200, 30, 0, 160]',
        pickable=True
    )

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

    # [VIZ3] Line chart visualization
    st.subheader("Line Chart of Elevations")
    st.line_chart(data['elevation_ft'])

    # [SEABORN] Scatter Plot - Elevation vs Latitude
    # Learned about Seaborn through data analytics internship during the summer
    st.subheader("Elevation vs Latitude (Scatter Plot)")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='latitude_deg', y='elevation_ft', hue='type', palette='Set2')
    plt.title("Elevation vs Latitude")
    plt.xlabel("Latitude (degrees)")
    plt.ylabel("Elevation (ft)")
    st.pyplot(plt)

# [ST4] Page styling
st.markdown("""
<style>
.main { background-color: black;
        color: pink;
}
</style>
""", unsafe_allow_html=True)
