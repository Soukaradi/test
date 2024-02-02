import streamlit as st
st.title("Sales streamlit dashboard")

def load_data(path: str):
    df = pd.read_excel(path)
    return df
