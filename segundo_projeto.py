#pip install plotly
import streamlit as st
# import plotly.express as px
#import matplotlib.pyplot as plt
import pandas as pd
import chardet  # Biblioteca para detectar encoding

def detect_encoding(file_path):
    # Detectar o encoding do arquivo CSV
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

st.title('Função para análise de distribuição geográfica')

def load_data():
    #clientes_encoding = detect_encoding('olist_customers_dataset.csv')
    #geolocal_encoding = detect_encoding("olist_geolocation_dataset.csv")
    
    df_clientes = pd.read_csv("olist_customers_dataset.csv",  encoding='ISO-8859-1')
    df_geolocal = pd.read_csv("olist_geolocation_dataset.csv",  encoding='ISO-8859-1')
    df_itens_por_pedido = pd.read_csv("olist_order_items_dataset.csv")
    df_forma_pag = pd.read_csv("olist_dados_forma_pag_limpos.csv")
    df_avaliacao_pedido = pd.read_csv("olist_dados_avaliacao_pedido_limpos.csv")
    df_pedido = pd.read_csv("olist_dados_pedidos_limpos.csv")
    df_produtos = pd.read_csv("olist_dados_produtos_limpos.csv")
    df_vendedores = pd.read_csv("olist_sellers_dataset.csv")
    df_categ_produto_traduzido = pd.read_csv("/os_datasets_tratados/product_category_name_translation.csv")
   
    return df_clientes, df_geolocal, df_itens_por_pedido, df_forma_pag, df_avaliacao_pedido, df_pedido, df_produtos, df_vendedores, df_categ_produto_traduzido
# Carregar os datasets
df_clientes, df_geolocal, df_itens_por_pedido, df_forma_pag, df_avaliacao_pedido, df_pedido, df_produtos, df_vendedores, df_categ_produto_traduzido = load_data()

# Função para análise de distribuição geográfica
def geographic_distribution():
    df_geolocal = pd.merge(df_clientes, df_geolocal, 
                                 left_on="customer_zip_code_prefix", 
                                 right_on="geolocation_zip_code_prefix")
    customers_by_state = df_geolocal["customer_state"].value_counts()
    st.header("Distribuição Geográfica dos Clientes")
    st.bar_chart(customers_by_state)
# Chamar a função de distribuição geográfica
geographic_distribution()
