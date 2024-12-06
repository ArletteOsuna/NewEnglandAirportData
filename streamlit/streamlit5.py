"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st

st.title("Welcome to Bentley University")
st.header("The CIS Department")
if st.checkbox("Click to display the image!"):
    st.image("CIS.jpb")

langs = st.multiselect("Which are programming languages?",
                         ["Python", "Java","English", "C++", "JavaScript","Farsi"])

if "Python" in langs:
    st.write("You are correct!")
if "Java" in langs:
    st.write("You are correct!")
if "C++" in langs:
    st.write("You are correct!")
if "JavaScript" in langs:
    st.write("You are correct!")
if "English" in langs:
    st.write("English is not a programming language!")
if "Farsi" in langs:
    st.write("Farsi is not a programming language!")