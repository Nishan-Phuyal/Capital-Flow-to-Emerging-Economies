import streamlit as st 
import pandas as pd
import plotly.express as px
import time
import geo_visual
import Interactive_Visuals
import Corr_matix

st.set_page_config(layout="wide", page_title= "Capital Flow to Emerging Economies", page_icon="$")
st.header("IMF Record of Capital Flow to Emerging Economies")
st.sidebar.header("Content")


url = "https://www.imf.org/en/Publications/WP/Issues/2020/08/21/Capital-Flow-Data-A-Guide-for-Empirical-Analysis-and-Real-time-Tracking-49646"

st.write("The data is published by the IMF as part of Robin Koepke and Simon Paetzold's work. Please visit [IMF Website](%s) for Updated Dataset and News Update"% url) 

content = {"1. Capital Flow On Map": geo_visual,
           "2. Interactive Insights": Interactive_Visuals,
           "Cross-Country Correlation" : Corr_matix}

select = st.sidebar.radio("", list(content.keys()))

content[select].app()