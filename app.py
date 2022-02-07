import streamlit as st
@st.cache
def main():
    for i in range(10):
      st.write('test!')
main()
