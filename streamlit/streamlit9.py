"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import pandas as pd
import streamlit as st

data = ([150,175,200,125],
        [175,350,450,250],
        [225,230,435,650])
df = pd.DataFrame(data, columns=['pears', 'apples', 'peaches', 'bananas'])

st.header('DataFrames and Streamlit')
st.write(df)
