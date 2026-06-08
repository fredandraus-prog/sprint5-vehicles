import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('C:/Users/freda/sprint5-vehicles/vehicles.csv')

st.header('Análise de anúncios de venda de carros')
st.write('Explore os dados de anúncios de carros usados nos EUA.')
st.subheader('Dados dos Anúncios')
st.dataframe(car_data.head())

hist_button = st.button('Criar histograma de preços')
if hist_button:
    st.write('Distribuição de preços dos carros')
    fig = px.histogram(car_data, x='price', title='Distribuição de preços')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão de preço vs. milhas')
if scatter_button:
    st.write('Preço vs Quilometragem')
    fig = px.scatter(car_data, x='odometer', y='price', title='Preço vs Quilometragem')
    st.plotly_chart(fig, use_container_width=True)

box_button = st.button('Criar boxplot de preços por tipo de carro')
if box_button:
    st.write('Boxplot de preços por tipo de carro')
    fig = px.box(car_data, x='type', y='price', title='Boxplot de preços por tipo de carro')
    st.plotly_chart(fig, use_container_width=True)
