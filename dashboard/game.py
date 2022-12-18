import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
from plotly.subplots import make_subplots
import datetime

st.set_page_config(layout="wide")

st.title("Game Analytics Dashboard")

###############Line Map############################


# st.header("Monthwise distribution of refugees arriving in Ireland")
# df_refugees1 = pd.read_csv('chart33.csv', on_bad_lines='skip')

# left_column1, right_column1 = st.columns([1, 1])

# options = ['All', 'Ukrainians', 'All other refugees'] 
# select1 = left_column1.selectbox("Choose the population type", options)


# df_refugees = df_refugees1.groupby('Month').sum().reset_index()

# # encoding='utf-8-sig', sep='\s*,\s*', engine='python'

# if select1 == 'All':
#     trace1 = px.line(x = df_refugees['Month'], y = df_refugees['All'], labels={'x':'Months', 'y':'All refugees'})
#     st.plotly_chart(trace1)
# elif select1 == 'Ukrainians':
#     trace2 = px.line(x = df_refugees['Month'], y = df_refugees['Ukraine'], labels={'x':'Months', 'y':'Ukrainian'})
#     st.plotly_chart(trace2)
# elif select1 == 'All other refugees':
#     trace2 = px.line(x = df_refugees['Month'], y = df_refugees['Other'], labels={'x':'Months', 'y':'All Other nationalities with protected status'})
#     st.plotly_chart(trace2)

################ Row 1 with all the metrics cards##############
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("#Players", "70k", "1.2%")
col2.metric("Highest Score", "500k", "5.6%")
col3.metric("Highest Score", "500k", "5.6%")
col4.metric("Highest Score", "500k", "5.6%")
col5.metric("Highest Score", "500k", "5.6%")


############## Row with a choropleth map and a pie chart###########

col11, col12 = st.columns(2)



###############Choropleth Map############################


with open("countries.geojson") as response:
    geo = json.load(response)

df_counties = pd.read_csv('counries2.csv')

# Add title and header

# Geographic Map
fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geo,
        locations=df_counties.coun,
        featureidkey="properties.ADMIN",
        z=df_counties.count1,
        colorscale="sunsetdark",
        # zmin=0,
        # zmax=500000,
        marker_opacity=0.5,
        marker_line_width=0,
    )
)


fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=0.25,
    mapbox_center={"lat": 40.701464, "lon": -85.772746},
    width=700,
    height=400,
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
with col11:
    st.header("Demographic Analysis")
    st.plotly_chart(fig)

df = pd.read_csv('userdata.csv')
bins = [10, 18, 30, 40, 50, 60, 70, 120]
labels = ['10-17', '18-29', '30-39', '40-49', '50-59', '60-69', '70+']
df['agerange'] = pd.cut(df.age, bins, labels = labels,include_lowest = True)

gk = df.groupby(['agerange', 'gender'])['gender'].count().reset_index(name='count')

with col12:
    st.header("Gender wise distribution")
    fig13 = px.pie(gk, values='count', names='gender')
    st.plotly_chart(fig13)



col_1, col_2 = st.columns(2)


with col_1:
    st.header("Age wise distribution")
    fig1 = px.bar(gk,x='agerange', y='count', color='gender',height=500, width=600)
    st.plotly_chart(fig1)

df_game = pd.read_csv('gamedata.csv')
game_data = df_game.groupby(['playing_date'])['session_time(min)'].mean().reset_index(name='mean_sess')
# game_data['playing_date'] = pd.to_datetime(game_data['playing_date'])
# df_ = game_data[(game_data['playing_date']>datetime.date(2022,12,1)) & (game_data['playing_date']<datetime.date(2022,12,15))]  
# df_ = game_data.loc[(game_data["playing_date"] >= "01/12/2022") & (game_data["playing_date"] <= "15/12/2022")]

with col_2:
    st.header("Session Analysis")
    trace1 = px.line(x = game_data['playing_date'], y = game_data['mean_sess'], labels={'x':'Date', 'y':'Mean Session Time (minutes)'})
    st.plotly_chart(trace1)



  
# Let's print the first entries
# in all the groups formed.


# ###############Stack Bar Graph Map############################

# df_months = pd.read_csv('chart2.csv', on_bad_lines='skip')

# st.header("Division across age group and gender")
# left_column, right_column = st.columns([1, 1])

# # Widgets: selectbox
# months = ['March', 'April', 'May', 'April', 'May', 'June', 'July', 'September', 'October', 'November', 'All']
# select = left_column.selectbox("Choose the month", months)

# if select == 'March':
#     fig1 = px.bar(df_months,x='Age Group', y='March', color='Sex',height=400, width=700)
#     st.plotly_chart(fig1)
# elif select =='April':
#     fig2 = px.bar(df_months,x='Age Group', y='April', color='Sex',height=400, width=700)
#     st.plotly_chart(fig2)
# elif select =='May':
#     fig3 = px.bar(df_months,x='Age Group', y='May', color='Sex',height=400, width=700)
#     st.plotly_chart(fig3)
# elif select =='June':
#     fig4 = px.bar(df_months,x='Age Group', y='June', color='Sex',height=400, width=700)
#     st.plotly_chart(fig4)
# elif select =='July':
#     fig5 = px.bar(df_months,x='Age Group', y='July', color='Sex',height=400, width=700)
#     st.plotly_chart(fig5)
# elif select =='August':
#     fig6 = px.bar(df_months,x='Age Group', y='August', color='Sex',height=400, width=700)
#     st.plotly_chart(fig6)
# elif select =='September':
#     fig7 = px.bar(df_months,x='Age Group', y='September', color='Sex',height=400, width=700)
#     st.plotly_chart(fig7)
# elif select =='October':
#     fig8 = px.bar(df_months,x='Age Group', y='October', color='Sex',height=400, width=700)
#     st.plotly_chart(fig8)
# elif select =='November':
#     fig9 = px.bar(df_months,x='Age Group', y='November', color='Sex',height=400, width=700)
#     st.plotly_chart(fig9)
# else:
#     fig10 = px.bar(df_months,x='Age Group', y='All', color='Sex',height=400, width=700)
#     st.plotly_chart(fig10)



# ###############Pie Chart Map############################


# st.header("Relationship status of refugees in Ireland")

# df_pie = pd.read_csv('chart4.csv', on_bad_lines='skip')

# left_column2, right_column2 = st.columns([1, 1])

# relationships_months = ['May', 'June', 'July', 'August', 'September', 'Total'] 
# select2 = left_column2.selectbox("Choose the month", relationships_months)

# if select2 == 'May':
#     fig11 = px.pie(df_pie, values='May', names='Relationship', title='Population of European continent')
#     st.plotly_chart(fig11)
# elif select2 == 'June':
#     fig12 = px.pie(df_pie, values='June', names='Relationship', title='Population of European continent')
#     st.plotly_chart(fig12)
# elif select2 == 'July':
#     fig13 = px.pie(df_pie, values='July', names='Relationship', title='Population of European continent')
#     st.plotly_chart(fig13)
# elif select2 == 'August':
#     fig13 = px.pie(df_pie, values='August', names='Relationship', title='Population of European continent')
#     st.plotly_chart(fig13)
# elif select2 == 'September':
#     fig13 = px.pie(df_pie, values='September', names='Relationship', title='Population of European continent')
#     st.plotly_chart(fig13)
# elif select2 == 'Total':
#     fig13 = px.pie(df_pie, values='Total', names='Relationship', title='Population of European continent')
#     st.plotly_chart(fig13)




