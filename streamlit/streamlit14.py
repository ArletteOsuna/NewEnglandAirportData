"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st
import pandas as pd

locations = [("Miami Beach", 25.793449, -80.139198),
             ("New Castle, DE", 39.668564, -75.586189),
             ('Roswell, NM', 33.400322, -104.534897),
             ("Pocatello, ID", 42.880363, -112.452911),
             ("Steamboat Springs, CO", 40.490429, -106.842384)]

df = pd.DataFrame(locations, columns=["City", "lat", "lon"])
st.title("Cities in the United States")
st.dataframe(df)

st.write("Map of Cities in the United States")
st.map(df)
