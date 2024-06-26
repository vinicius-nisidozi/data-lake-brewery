# Brewery Data Lake

<h4>Visão Geral do Projeto:</h4>
Este é um projeto de Data Engineering para exercitar os seguintes conceitos:<br>
. Desenho de solução<br>
. Desenvolvimento de pipelines de dados<br>
. Orquestração de dados<br>
. Escalabilidade<br>
. Qualidade de código<br>
. Observablidade<br>
. Completude<br>
. Consumo de dados de API<br>
. Transformação e tratamento de dados<br>

<h4>Solução proposta:</h4>
. Python<br>
. PySpark<br>
. Azure ADLS<br>
. Azure Databricks<br>
. Apache Airflow<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/4247df17-bc6d-4c4c-9dd9-33b3bfb754a9)

<br><h4>Desenvolvimento:</h4>
1. <h4>Criação da Estrutura do Data Lake:</h4>
Nessa etapa foram criadas todas as conexões entre Azure ADLS, Azure Databricks e Apache Airflow. Além de a criação das camadas Bronze, Silver e Gold.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/63bc5bd9-68a8-4765-87d9-6fb26700dad1)

2. <h4>Ingestão de Dados:</h4>
<h5>Camada Bronze:</h5>
Através do Azure Databricks foi desenvolvido um pipeline para ingestão dos dados da API openbrewerydb (https://www.openbrewerydb.org), que contém dados de cervejarias.
Nessa etapa os dados são carregados no formato que a API os fornece, dessa forma, os dados são salvos em um arquivo json no ADLS, e também disponibilizados em uma tabela no Databricks estruturada na camada bronze.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/7e23ad32-0381-4062-983e-abfdd3226389)


<h5>Camada Silver:</h5>
Na sequência, para a camada Silver, os dados recebem um schema, definindo data types para os dados recebidos, ocorre também a remoção de dados duplicados e é inserida uma coluna com os dados de data de inserção dos dados na camada silver.
Após isso, os dados são salvos particionados, por país, estado e cidade, em formato parquet.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/5a080ebd-1953-44d3-84d8-555f42a6a2d4)

<h5>Camada Gold:</h5>
Na última camada, os dados são agregados em uma view contendo a quantidade de cervejarias, agregadas por tipo de cervejaria e localização.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/4eaae7b5-5779-44bd-b393-54bf625513d1)

<h5>Estrutura dos dados no Azure ADLS:</h5>
Os arquivos foram salvos em uma estrutura organizada em pastadas por data, seguindo a seguinte lógica:
f"dbfs:/mnt/data/silver/dataset_brewery/{year}/{month}/{day}/brewery" em que year, month e day são variáveis que contém a data atual da execução do pipeline.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/1c59cc33-c7d6-4d99-840b-464cf14d3214)

3. <h4>Orquestração:</h4>
O Apache Airflow realiza a orquestração de todo o pipeline utilizando operadores Databricks integrados ao projeto na Azure.
Nele além da orquestração, é possível realizar o gerenciamento de erros através de logs, além de possibilitar a visualização das execuções do pipeline.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/04b24a4d-b0e0-436b-8fdb-15aff1a2dc49)

4. <h4>Monitoramento e observabilidade do pipeline:</h4>
Ao final de cada processo na execução das camadas existe um INSERT em uma tabela criada na camada "monitoring" que captura a quantidade de dados inseridos, a data atual e a respectiva tabela em que eles foram inseridos.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/ded4309e-12f2-48d3-893b-56789a34cdaa)

Além disso, as tasks executadas para cada camada no Airflow disparam e-mails com informações sobre a execução de cada job.<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/435b97df-ea10-4341-aaf0-f5466f586065)

<h4>Resultados e Impacto:</h4><br>
O resultado do projeto foi um Data Lake estruturado no ADLS, com tabelas e views disponibilizadas no Databricks, e com um pipeline sendo orquestrado pelo Apache Airflow.
A solução apresentada é robusta, escalável, proporciona colaboração, melhorias futuras, ingestão de novos dados de novas fontes e processamento de big data com alta performance.
O projeto está publicado em minha conta Azure, todos os códigos utilizados no pipeline estão neste repositório. 
