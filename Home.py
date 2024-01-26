import streamlit as st
import pandas as pd
import base64
import pyarrow.parquet as pq
import io

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
    st.set_page_config(layout="wide", page_title="Parquet Viewer", page_icon="📝", initial_sidebar_state='collapsed')
    
    putBackground()

    # Título da página
    st.title('Visualizador de Arquivo .parquet')

    # Nota sobre os dados não serem armazenados
    st.write("Nota: Os dados carregados persistem na sessão atual e não são armazenados em nenhum local.")

    # Upload do arquivo .parquet
    parquet_file = st.file_uploader("Faça o upload de um arquivo .parquet", type=["parquet"])

    if parquet_file is not None:
        # Lê o arquivo .parquet usando o pyarrow
        table = pq.read_table(parquet_file)
        
        # Obtém informações resumidas sobre o arquivo Parquet
        num_rows = table.num_rows
        num_columns = len(table.schema.names)

        st.write("---")
        
        # Exibe as informações resumidas
        st.subheader("Informações sobre o arquivo:")
        st.write(f"Total de Linhas: {num_rows} | Total de Colunas: {num_columns}")

        # Exibe as 100 primeiras linhas do DataFrame
        if num_rows >= 100:
            records = 100
        else:
            records = num_rows
        
        st.subheader(f"{records} Primeiras Linhas:")
        
            
        df = table.to_pandas()
        st.write(df.head(records))

        # Opções para fazer o download em .xlsx ou .csv usando botões de rádio
        download_format = st.radio("Selecione o formato de download:", [".xlsx", ".csv"])

        if download_format == ".xlsx":
            # Crie um buffer para armazenar o arquivo Excel
            excel_buffer = io.BytesIO()
            
            # Salva o DataFrame em um arquivo .xlsx no buffer
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as excel_writer:
                df.to_excel(excel_writer, index=False)
            
            # Defina o cursor do buffer para o início
            excel_buffer.seek(0)
                        
            st.download_button(label="Baixar Arquivo .xlsx", data=excel_buffer.read(), file_name="output.xlsx", key="xlsx")

        elif download_format == ".csv":
            # Salva o DataFrame em um arquivo .csv
            csv_file = df.to_csv(index=False)  

            st.download_button(label="Baixar Arquivo .csv", data=csv_file, file_name="output.csv", key="csv")
            

    st.markdown('<img src="https://github.com/fluidicon.png" width="25" height="25"/> <a href="https://github.com/leandrobi/viewer-parquet-on">https://github.com/leandrobi/viewer-parquet-on</a>', unsafe_allow_html=True)


if __name__=='__main__':
    main()
