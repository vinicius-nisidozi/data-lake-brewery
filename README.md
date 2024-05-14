# data-lake-brewery

Visão Geral do Projeto:<br>

<h3>Brewery Data Lake</h3>

<h4>Solução proposta:</h4>
. Python<br>
. PySpark<br>
. Azure ADLS<br>
. Azure Databricks<br>
. Apache Airflow<br>

<br><h4>Desenvolvimento:</h4>
1. <h4>Criação da Estrutura do Data Lake:</h4>
Nessa etapa foram criadas todas as conexões entre Azure ADLS, Azure Databricks e Apache Airflow. Além de a criação das camadas Bronze, Silver e Gold.

2. <h4>Ingestão de Dados:</h4>
<h5>Camada Bronze:</h5>
Através do Azure Databricks foi desenvolvido um pipeline para ingestão dos dados da API openbrewerydb (https://www.openbrewerydb.org), que contém dados de cervejarias.
Nessa etapa os dados são carregados no formato que a API os fornece, dessa forma, os dados são salvos em um arquivo json no ADLS, e também disponibilizados em uma tabela no Databricks estruturado na camada bronze.
<h5>Camada Silver:</h5>
Na sequência, para a camada Silver, os dados recebem um schema, definindo data types para os dados recebidos, ocorre também a remoção de dados duplicados e é insirida uma coluna com os dados de data de inserção dos dados na camada silver.
Após isso, os dados são salvos particionados, por país, estado e cidade, em formato parquet.
<h5>Camada Gold:</h5>
Na última camada, os dados são agregados em uma view contendo a quantidade de cervejarias, agregadas por tipo de cervejaria e localização.
<h5>Estrutura dos dados no Azure ADLS:</h5>
Os arquivos foram salvos em uma estrutura organizada em pastadas por data, seguindo a seguinte lógica:
f"dbfs:/mnt/data/silver/dataset_brewery/{year}/{month}/{day}/brewery" em que year, month e day são variáveis que contém a data atual da execução do pipeline.

3. <h4>Monitoramento e observabilidade dos pipeline:</h4>
Ao final de cada processo na execução das camadas existe um INSERT em uma tabela criada na camada "monitoring" que captura a quantidade de dados inseridos, a data atual e a respectiva tabela em que eles foram inseridos.
Além disso, as tasks executadas para cada camada no Airflow disparam e-mails com informações sobre a execução de cada job.


<h4>Resultados e Impacto:</h4><br>
O resultado do projeto foi um Data Lake estruturado no ADLS, com tabelas e views disponibilizadas no Databricks, e com um pipeline sendo orquestrado pelo Apache Airflow.
A solução apresentada é robusta, escalável, proporciona colcaboração, melhorias futuras, ingestão de novos dados de novas fontes, processamento de big data com alta performance.
O projeto está publicado em minha conta Azure, todos os códigos utilizados para a execução do pipeline estão neste repositório. 
