"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st

st.title("Welcome to Bentley University")
st.header("The CIS Department")
st.image("CIS.png")
st.subheader("Courses")
st.markdown("CS 230: Introduction to Programming")
st.video("Computers.mp4")
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("This is a caption")
st.code("x=2021")