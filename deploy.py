# app.py
import os
import streamlit as st
import subprocess

st.title("Executable File Runner")

executable_path = os.path.join(os.path.dirname(__file__), "GUI.exe")

if st.button("Run Executable"):
    result = subprocess.run([executable_path], capture_output=True)
    st.text(result.stdout.decode())
