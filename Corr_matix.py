import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    df = pd.read_csv("Clean_Capital_Flow_data.csv")
    df = df.pivot(index=['Countries', 'Date', "Year", "Month" ], columns='Indicies', values='Value').reset_index()
    total_agg = df.groupby([ "Countries", "Year"])["Total"].sum().reset_index(name = "Total")
    df_agg_pivot = pd.pivot(total_agg, index= "Year", columns= "Countries", values="Total" )
    corr_matirx = (df_agg_pivot.corr()).round(1)
    corr_matirx.drop(["Malaysia"], axis=0, inplace= True)
    corr_matirx.drop(["Malaysia"], axis=1, inplace= True)
 
    fig = px.imshow(corr_matirx,
                labels=dict(x="", y="", color="Correlation"),
                text_auto=f".2%",  # Automatically add text in each cell
                aspect="auto"  ,  # 'auto' stretches the heatmap to fit the dimensions of 'fig'
                color_continuous_scale= "rainbow",
                title='Correlation Between Cross Border Net Captal Flow',
               )

    fig.update_layout(title_x = 0.3,
                      width = 1000,
                      height = 800,
                      xaxis=dict(range=[0, 8])
                       )

    st.plotly_chart(fig)
