## How to install streamlit

```
pip install streamlit
```

## How to start streamlit 

notepad start.bat
```
@echo off
REM Change to the desired directory
cd /d "C:\Program Files\myworkspace"

REM Start the Streamlit app
streamlit run streamlit-app.py
```
notepad streamlit-app.py
```
import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is your first Streamlit app.')
```
