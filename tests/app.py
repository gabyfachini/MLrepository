import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizza.csv")
x = df[["diametro"]]
y = df[["preco"]]
modelo = LinearRegression()
modelo.fit(x, y)

st.title("Previsão de Preço de Pizzas")
st.write("Este é um aplicativo simples para prever o preço de uma pizza com base no seu diâmetro.")

diametro = st.number_input("Diâmetro da pizza (cm): ", min_value=0.0)

if st.button("Prever Preço"):
   preco = modelo.predict([[diametro]])
   st.write(f"O preço estimado para uma pizza de {diametro} cm é R$ {preco[0][0]:.2f}.")