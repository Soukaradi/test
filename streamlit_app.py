import pandas as pd
import streamlit as st
st.title("Sales streamlit dashboard")
st.markdown("_Prototype v0.4.1_")
def load_data(path: str):
    df = pd.read_excel(path)
    return df
