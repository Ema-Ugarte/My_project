# Importando las librerías necesarias
import pandas as pd
import plotly.express as px
import streamlit as st

# título de la aplicación
st.title("Analisis de datos de anuncios de ventas de coches")

vehicle_data = pd.read_csv("vehicles_us.csv")  # leyendo el archivo CSV

st.header("Selecciona el grafico a construir")

# botón para construir el histograma
hist_button = st.checkbox("Construir histograma")

# botón para construir el gráfico de dispersión
disp_button = st.checkbox("Construir grafico de dispersion")


if hist_button:  # si el botón es presionado
    # mostramos el título del histograma

    st.subheader("Histograma de odómetro")

    # escribimos el mensaje

    st.write(
        "Construimos un histograma para el conjunto de datos de anuncios de ventas de coches")

    # creamos el histograma
    fig = px.histogram(vehicle_data, x="odometer")

    # configuramos los ejes del histograma
    fig.update_layout(
        xaxis_title="Odómetro (millas)",
        yaxis_title="Número de vehículos"
    )

    # mostramos un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if disp_button:  # si el botón es presionado
    # mostramos el título del gráfico de dispersión

    st.subheader(
        "Gráfico de dispersión de la relación entre odómetro y precio")

    # escribimos el mensaje

    st.write(
        "Construyendo el gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches")

    # creamos el gráfico de dispersión
    fig = px.scatter(vehicle_data, x="odometer", y="price")

    # configuramos los ejes del gráfico de dispersión
    fig.update_layout(
        xaxis_title="Odómetro (millas)",
        yaxis_title="Precio (USD)"
    )

    # mostramos un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
