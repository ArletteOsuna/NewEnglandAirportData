"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import pandas as pd
import streamlit as st

st.header('DataFrames and Streamlit')
st.write("This also creates a DataFrame:")
st.write(pd.DataFrame(dict(pears=[150, 175, 225],
                           apples=[175, 350, 230],
                           peaches=[200, 450, 435],
                           bananas=[225, 230, 435])))

