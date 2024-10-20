import streamlit as st 
import pandas as pd
import plotly.express as px
import time



df = pd.read_csv("Clean_Capital_Flow_data.csv")
df = df.pivot(index=['Countries', 'Date', "Year", "Month", "Alpha-3 code" ], columns='Indicies', values='Value').reset_index()
df.columns = [col for col in df.columns]


# visulizing the Monthly Capital flow on a Geo-Map

df_x = df.dropna(axis=0)

df_x["Net Flow"] = df_x["Total"].apply(lambda x: "Inflow" if x > 0 else "Outflow")

df_x["Total_abs"] = pd.to_numeric(df_x["Total"], errors='coerce').abs()

df_x["Date"] = pd.to_datetime(df_x["Date"], errors='coerce')

df_x["Date"] = df_x["Date"].dt.strftime("%b %Y")

custom_colors = ['#ff0000','#008000']

def app():
    with st.spinner("The Map is loading"):
        time.sleep(2)
        fig = px.scatter_geo(df_x, 
                            locations="Alpha-3 code",
                            text = "Alpha-3 code",
                            hover_data = {"Net Flow":True,
                                        "Date": True,
                                        "Total_abs": False,
                                        "Alpha-3 code": False,
                                        "Total": True,
                                        "Equity": True,
                                        "Debt": True,
                                        },
                            projection="natural earth",
                            animation_frame= "Date",
                            template= "seaborn",
                            title="Monthly Capital Flows to Emerging Economies Over Time (1995 -2022)",
                            size="Total_abs",
                            color = "Net Flow",
                            size_max = 100,
                            color_discrete_sequence= custom_colors
                            )

        fig.update_layout(
            title_x = 0.2,font=dict(color='white'),
            width = 1000,
            height = 600
            )

        fig.update_traces(
            textposition='bottom center',
            textfont=dict(size=10, color='olive', family="Arial")  
        )

        st.plotly_chart(fig)
        
