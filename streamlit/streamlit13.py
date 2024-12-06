"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
sales = [230, 850, 720, 430, 520]
ax.bar(range(5),sales,color='m')
ax.set_xlabel('Regions')
ax.set_title('Sales')
ax.set_xticks(range(5))
ax.set_xticklabels(['Northeast', 'South', 'Mid-Atlantic', 'Midwest', 'West'])
st.pyplot(fig)
