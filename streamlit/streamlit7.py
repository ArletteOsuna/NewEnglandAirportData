"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import streamlit as st

st.title("Welcome to Bentley University")
st.header("The CIS Department")
st.image("CIS.jpg")

name = st.text_input("Enter your name")
st.write(f"Your name is {name}")

date1 = st.date_input("What is todays's date?")
st.write(f"Today is {date1}")

num1 = st.number_input("Enter a number:")
st.write(f"The number is {num1}")
