import streamlit as st

def display_dashboard():
    """Display a simple dashboard."""
    st.title("Phishing Detection Dashboard")
    st.write("Welcome to the phishing detection system!")
    st.write("Use the sidebar to navigate.")

if __name__ == "_main_":
    display_dashboard()