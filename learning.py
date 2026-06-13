# following the documentation at https://docs.streamlit.io/library/get-started/create-an-app 
# run with this: python -m streamlit run NAMEHERE.py
# To stop the Streamlit server, press Ctrl+C in the terminal.

# libraries
import streamlit as st
import numpy as np
import pandas as pd

# example snippets
'''
# writing a dataframe
randframe = np.random.rand(10, 20)
st.write(randframe)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# session state counter
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
'''

