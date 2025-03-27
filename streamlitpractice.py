import streamlit as st
st.title("My first webapp")

annual_salary = st.number_input("Enter your salary")
year_work = st.number_input("Enter your year of work")
if st.button("Submit"):
    if annual_salary >= 500000 and year_work >= 5:
        st.write("Your application has accepted")
    else:
        st.write("Your application has rejected")