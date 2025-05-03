import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config('wide')
data = pd.read_csv('india_Census.csv')

list_state= list(data['State'].unique())
list_state.insert(0,'Overall India')

list_pas = ['Population','Literacy Rate','Households_with_Internet','sex ratio']
list_pas2 = ['Literacy Rate','Households_with_Internet','sex ratio','Population']

pas = sorted(data[list_pas])
pas2 = sorted(data[list_pas2])

st.sidebar.title('India Ka Data')
state= st.sidebar.selectbox('select a state',list_state)
primary = st.sidebar.selectbox('select primary',pas)
secondary = st.sidebar.selectbox('select secondary',pas2)
plot = st.sidebar.button('Plot Graph')

if plot:

    if state=='Overall India':
        st.title('Size Represent Primary Parameter')
        st.title('Color Represent Secondary Parameter')

        fig = px.scatter_mapbox(data, lat='Latitude', lon='Longitude',size = primary, color = secondary,
                                hover_name='State',zoom=3.5,size_max=20,mapbox_style='carto-positron',
                                width=1200, height=800, color_continuous_scale='hsv')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.title('Size Represent Primary Parameter')
        st.title('Color Represent Secondary Parameter')

        state_main = data[data['State'] == state]

        fig = px.scatter_mapbox(state_main, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                hover_name='District', zoom=5, size_max=30, mapbox_style='carto-positron',
                                width=1200, height=800, color_continuous_scale= 'hsv')
        st.plotly_chart(fig, use_container_width=True)