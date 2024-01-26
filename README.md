![Forks](https://img.shields.io/badge/forks-44-blue)
![Stars](https://img.shields.io/badge/stars-13-yellow)

# Parquet Viewer Online

-- pt-br 
## Descrição
Bem-vindo ao projeto de visualizador online de parquet.
Este projeto foi pensado como um teste após a necessidade de abrir um arquivo .parquet de forma rápida em períodos de desenvolvimento.

Adicionamos um gerador de .parquet em uma das páginas também afim de testarmos o uso da lib Faker no python.

Dúvidas, leandroalves2w@gmail.com ou https://www.linkedin.com/in/leandrosilva-bi/

## Tecnologia
Em resumo foi utilizado o python na versão 3.10 e algumas bibliotecas externas para seu correto funcionamento, como: 

1. Streamlit para criação da página web
2. Pyarrow para utilização do parquet
3. Faker para criação de dados falsos
4. XlsxWriter para exportar o dataframe para excel

## Instruções
1. Tenha o python instalado na máquina
2. Abra o cmd na pasta desejada e execute o comando:
    > git clone https://github.com/leandrobi/viewer-parquet-on
3. Instale as libs necessárias do arquivo requirements através do:
    > pip install -r requirements.txt
4. Execute o comando:
    > streamlit run .\Home.py
5. Se tudo ocorreu certo, sua página será carregada no localhost em:
    > http://localhost:8501


-- en-us:
## Description
Welcome to the Parquet file online viewer project. This project was conceived as a test to quickly open a .parquet file during development periods.

We have also added a .parquet generator on one of the pages to test the use of the Faker library in Python.

## Technology
In summary, Python version 3.10 was used, along with some external libraries for its proper functioning, including:

1. Streamlit for creating the web page
2. Pyarrow for working with Parquet files
3. Faker for generating fake data
4. XlsxWriter for exporting the dataframe to Excel

## Instructions
1. Ensure that Python is installed on your machine.
2. Open the command prompt in your desired folder and execute the following command:
    > git clone https://github.com/leandrobi/viewer-parquet-on
3. Install the necessary libraries from the requirements file by running:
    > pip install -r requirements.txt
4. Execute the following command:
    > streamlit run .\Home.py
5. If everything goes well, your page will be loaded at the following address on localhost:
    > http://localhost:8501