"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import pandas as pd
import numpy as np
import streamlit as st

chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
st.write(chart_data)
st.bar_chart(chart_data)
