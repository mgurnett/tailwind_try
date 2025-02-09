from core.models import * 
from django.conf import settings
from datetime import datetime, date, timedelta
from icecream import ic
import plotly.express as px
import pandas as pd

def granary_graph(bin):
    nos = bin.num_of_sensors * (24 * 30) # 720 or 24hours worth
    readings_qs= bin.data_for_graph.values()
    # ic (len(readings_qs))
    df = pd.DataFrame(readings_qs).tail(nos)
    # ic (df)
    df["sensor_depth"] = df["sensor_depth"].astype(str)
    # # ic (df)
    alarm_list = []
    for a in bin.sensor_set.all():
        alarm_list.append(a.alarm)

    # fig = px.line(df, x="recorded", y="value", color="sensor_id", text="value")
    fig = px.scatter(
        df, 
        x="recorded", 
        y="value", 
        symbol="sensor_depth", 
        color_discrete_sequence = px.colors.qualitative.Alphabet,
        # title = f"Granary {bin.name} - {bin.description}",
        color="sensor_depth",
        trendline="rolling", 
        trendline_options=dict(window=5),
        width=1100, 
        height=800,
        labels={
            "recorded": "Date and Time of Measurement (last 24 hours)",
            "value": "Temperature (C)",
            "sensor_depth": "Depth from the top (ft)"
        },
    )
    fig.update_traces(
        marker=dict(
            size=8,
            symbol="diamond",
            line=dict(
                width=2,
                color='DarkSlateGrey'
                )
            ),
            selector=dict(mode='markers')
        )
    fig.update_layout(
        title=dict(text=f"{bin.serial_number} Granary: {bin.name} - {bin.description}", font=dict(size=30), automargin=True, yref='paper')
        )
    # fig.update_layout(hovermode="x unified")
    fig.add_shape(type='line',
                x0=df.recorded.min(),
                y0=alarm_list[0],
                x1=df.recorded.max(),
                y1=alarm_list[0],
                line=dict(color='Red',),
                # xref='x',
                # yref='y'
                )       

    fig.update_layout(
        {
            "paper_bgcolor": "rgb(142, 153, 215)",
            "plot_bgcolor": "rgb(161, 170, 222)",
        }
    )

    return fig


def granary_graph_history(bin):  #bin is an object
    readings_qs= bin.data_for_history_graph.values()
    # ic (len(readings_qs))
    df = pd.DataFrame(readings_qs)
    # ic (df)
    df["sensor_depth"] = df["sensor_depth"].astype(str)
    # # ic (df)
    alarm_list = []
    for a in bin.sensor_set.all():
        alarm_list.append(a.alarm)

    # fig = px.line(df, x="recorded", y="value", color="sensor_id", text="value")
    fig = px.scatter(
        df, 
        x="hour", 
        y=["average", "high"], 
        symbol="sensor_depth", 
        color_discrete_sequence = px.colors.qualitative.Alphabet,
        # title = f"Granary {bin.name} - {bin.description}",
        color="sensor_depth",
        trendline="rolling", 
        trendline_options=dict(window=5),
        width=1100, 
        height=800,
        labels={
            "hour": "Date and Time of Measurement",
            "average": "Average temperature (C)",
            "sensor_depth": "Depth from the top (ft)"
        },
    )
    fig.update_traces(
        marker=dict(
            size=8,
            symbol="diamond",
            line=dict(
                width=2,
                color='DarkSlateGrey'
                )
            ),
            selector=dict(mode='markers')
        )
    fig.update_layout(
        title=dict(text=f"{bin.serial_number} Granary: {bin.name} - {bin.description}", font=dict(size=30), automargin=True, yref='paper')
        )      

    fig.update_layout(
        {
            "paper_bgcolor": "rgb(142, 153, 215)",
            "plot_bgcolor": "rgb(161, 170, 222)",
        }
    )

    return fig


def granary_graph_battery(bin):  #bin is an object
    battery_qs= bin.data_for_battery_graph.values()
    # ic (len(readings_qs))
    df = pd.DataFrame(battery_qs)
    # ic (df)

    fig = px.scatter(
        df, 
        x="recorded", 
        y="battery", 
        # symbol="", 
        # color_discrete_sequence = px.colors.qualitative.Alphabet,
        # title = f"Granary {bin.name} - {bin.description}",
        color="battery",
        trendline="rolling", 
        trendline_options=dict(window=25),
        width=1800, 
        height=600,
        labels={
            "recorded": "Date and Time of Measurement",
            "battery": "Battery voltage (V)",
        },
    )
    fig.update_traces(
        marker=dict(
            size=8,
            symbol="diamond",
            line=dict(
                width=2,
                color='DarkSlateGrey'
                )
            ),
            selector=dict(mode='markers')
        )
    fig.update_layout(
        title=dict(text=f"Battery voltage for {bin.serial_number} Granary: {bin.name} - {bin.description}", font=dict(size=20), automargin=True, yref='paper')
        )      

    fig.update_layout(
        {
            "paper_bgcolor": "rgb(142, 153, 215)",
            "plot_bgcolor": "rgb(161, 170, 222)",
        }
    )

    return fig