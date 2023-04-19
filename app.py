import streamlit as st

def find_max(a, b, c):
    return max(a, max(b, c))

st.title("Find Maximum of Three Numbers")

a = st.number_input("Enter first number:")
b = st.number_input("Enter second number:")
c = st.number_input("Enter third number:")

if st.button("Find Maximum"):
    max_num = find_max(a, b, c)
    st.success(f"The maximum number is {max_num}")
