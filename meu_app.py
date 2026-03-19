import streamlit as st
from forex_python.converter import CurrencyRates


#Nome da página
st.set_page_config(page_title="C.C.G - Coin Conversion Global")

#Título ao site
st.title('Welcome to C.C.G - Coin Conversion Global!')
st.write('Convert currency values in seconds!')

c = CurrencyRates()

moedas = ['BRL', 'USD', 'EUR', 'GBP', 'JPY', 'CAD']

#Sistema de seleção das moedas
moeda_origem = st.selectbox('Select currency:', moedas)
moeda_destino = st.selectbox('Result:', moedas)

#Seleção
valor = st.number_input('Enter value:', min_value=0.0)

#Resultados
if st.button('Convert'):
    taxa = c.get_rate(moeda_origem, moeda_destino)
    resultado = valor * taxa

    st.success(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")

#Extras
st.sidebar.title('ATTENTION!!')
st.sidebar.write('This website operates as a conversion calculator for informational purposes. We have no link to bank accounts and do not perform exchange transactions.')







