import streamlit as st
import pandas as pd
from faker import Faker
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import io
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def putBackground():
    # Defina a cor de fundo usando HTML
    page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"]
        {
            background-color: rgba(255, 0, 0, 0.5); /* Cor de fundo vermelha com 10% de transparência */
            /*background: -webkit-linear-gradient(to right, #FF0000 80%, #513a48); /* Gradiente com parte escura mais à esquerda */
            background: linear-gradient(to right, #FF0000 80%, #513a48);*/ /* Gradiente com parte escura mais à esquerda */

            background: rgb(121,9,9);
            background: linear-gradient(90deg, rgba(121,9,9,0.989233193277311) 0%, rgba(255,0,0,1) 24%, rgba(255,0,74,1) 100%);
            color: white; /* Define a cor do texto para branco */

            /* Estilo para o título */
            .st-emotion-cache-10trblm.e1nzilvr1 {
                color: white; /* Cor vermelha para o título */
            }
            
            /* Estilo para o texto dentro do div específico */
            .st-emotion-cache-16idsys.e1nzilvr5 p {
                color: white; /* Cor branca para o texto dentro do div */
            }

            /* Estilo para o botão específico */
            .st-emotion-cache-1vbkxwb.e1nzilvr5 p {
                color: black; /* Cor preta para o texto do botão */
            }
            </style>
    """

    img = get_img_as_base64("backg5.jpg")
    page_bg_img = f""" 
        <style>
        [data-testid="stAppViewContainer"]
        {{
            background-image: url("data:image/webp;base64,{img}");
            background-size: repeat;
            
        }}
        </style>

    """

    # Crie um elemento div com a classe de estilo background
    return st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    # Configurando o layout para o modo "wide"
    st.set_page_config(layout="wide", page_title="Parquet Generator", page_icon="📝", initial_sidebar_state='collapsed')
    
    putBackground()

    # Título da página
    st.title("Criar DataFrame Fake e Exportar para Parquet")

    # Solicita ao usuário o número de colunas e linhas
    num_colunas = st.number_input("Número de Colunas (1-10):", min_value=1, max_value=10, step=1)
    num_linhas = st.number_input("Número de Linhas (máx. 500):", min_value=1, max_value=500, step=1, value=25)

    # Lista de atributos do Faker que você deseja usar para as colunas
    atributos_faker = [
    "name", "address", "email", "phone_number", "date_of_birth",
    "job", "company", "credit_card_number", "city", "country"
    ]

    # Função para criar o DataFrame e exportar para Parquet em memória
    def exportar_para_parquet():
        # Crie uma instância do Faker
        faker = Faker()

        # Gera os nomes das colunas de acordo com o número informado pelo usuário
        nomes_colunas = [atributos_faker[i] for i in range(num_colunas)]

        # Gere os dados aleatórios usando o Faker
        dados = []
        for _ in range(num_linhas):
            linha = [getattr(faker, coluna)() for coluna in nomes_colunas]
            dados.append(linha)

        # Cria o DataFrame
        df = pd.DataFrame(dados, columns=nomes_colunas)

        # Exporta o DataFrame para Parquet em memória
        output = io.BytesIO()
        table = pa.Table.from_pandas(df)
        pq.write_table(table, output)

        # Exibe o DataFrame
        st.write("DataFrame Fake Gerado:")
        st.write(df)    

        return output.getvalue()

    # Botão para criar o DataFrame e exportar para Parquet
    if st.button("Criar DataFrame Fake e Exportar para Parquet"):
        parquet_file = exportar_para_parquet()
        
        # Botão para baixar o arquivo Parquet
        st.write("Clique no botão abaixo para baixar o arquivo Parquet:")
        st.download_button(label="Baixar Arquivo Parquet", data=parquet_file, file_name="parquet_faker.parquet", key="parquet")


if __name__ == '__main__':
    main()
