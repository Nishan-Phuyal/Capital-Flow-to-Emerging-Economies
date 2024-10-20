import pandas as pd 
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import calendar

def app():
    col1, col2 = st.columns((1,0.9), gap= "medium")

    with col1:
        df = pd.read_csv("Clean_Capital_Flow_data.csv")

        df.dropna(axis=0, inplace=True)

        year = st.slider("Select the year", min_value = 1995, max_value = 2022, step = 1, value = 2015)

        month = st.slider("Select the Month", min_value = 1, max_value = 12, step = 1, value = 9)

        df = df[(df["Year"] == year ) & (df["Month"] == month)]
        
        fig_title = f"Per Country Capital Flow in {calendar.month_name[month]} of {year}"

        fig = px.histogram(df, x = "Countries", y = "Value", barmode = "stack", color="Indicies", text_auto=True, title=fig_title)

        fig.update_layout( xaxis= dict(range = [0,12]), 

            yaxis_title = "Indices (in Million USD )" )
        
        st.plotly_chart(fig)

        with col2 : 
            df =  pd.read_csv("Clean_Capital_Flow_data.csv")

            df = df.pivot(index=['Countries', 'Date', "Year", "Month" ], columns='Indicies', values='Value').reset_index()

            country = st.selectbox("Select a country", df["Countries"].unique())
            
            df = df[df["Countries"] == country]

            layout = dict(
                hoversubplots="axis",
                title="Capital Flow over Time per Economy",
                hovermode="x",
                grid=dict(rows=3, columns=1),
            )

            data = [
                go.Scatter(x=df["Date"], y=df["Total"], xaxis="x", yaxis="y", name="Netflow"),
                go.Scatter(x=df["Date"], y=df["Equity"], xaxis="x", yaxis="y2", name="Equity"),
                go.Scatter(x=df["Date"], y=df["Debt"], xaxis="x", yaxis="y3", name="Debt"),
            ]

            fig = go.Figure(data=data, layout=layout)
            
            st.plotly_chart(fig)
