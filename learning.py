# following the documentation at https://docs.streamlit.io/library/get-started/create-an-app 
# run with this: python -m streamlit run NAMEHERE.py
# To stop the Streamlit server, press Ctrl+C in the terminal.

# libraries
import streamlit as st
import numpy as np

# writing a dataframe
randframe = np.random.rand(10, 20)
st.write(randframe)
