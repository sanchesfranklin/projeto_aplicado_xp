# Anuário Estatísticos da ANTAQ (Agência Nacional de Transportes Aquáticos)

A DAG realiza a extração, transformação e carga no banco de dados dos dados da ANTAQ, com o objetivo de capturar informações sobre Atracações e Cargas contidas nessas atracações, para a equipe de analistas poderem analisar os dados.

# Tasks

#### Landing
- 1. **Download (/landing_download_files_source_task.py)**: Realiza o download dos dados na origem, os dados vem no formato .zip.

- 2. **Descompacta Zip (/landing_descompacta_files_task.py)**: Descompacta os arquivos zip, e salva ainda na camada Landing no formato original .txt

#### Raw
- 1. **Normaliza Colunas (/raw_transform_files_task.py)**: Realiza a leitura dos dados na Landing,
e realiza uma transformação mínima nas colunas, e salva o dado em .parquet.

#### Trusted
- 1. **Transformação do dado (/trusted_transform_files_task.py)**: Aplica transformação no dataframe, aplicando
o schema, ou seja, nesse processo todas as colunas são renomeadas, e também alterado o seu tipo de dado

#### Business
- 1. **Transformação Negócio (/business_transform_files_task.py)**: Aplica transformação no dataframe aplicando regras de negócios.

- 2. **Load (/business_load_database.py)**: Realiza a carga no banco de dados.

