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

<h4>Solução proposta:</h4>
. Python<br>
. PySpark<br>
. Azure ADLS<br>
. Azure Databricks<br>
. Apache Airflow<br>

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/1644cfc5-4c4b-44f0-b6ef-3268458121f4)

<br><h4>Desenvolvimento:</h4>
1. <h4>Criação da Estrutura do Data Lake:</h4>
Nessa etapa foram criadas todas as conexões entre Azure ADLS, Azure Databricks e Apache Airflow. Além de a criação das camadas Bronze, Silver e Gold.

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/63bc5bd9-68a8-4765-87d9-6fb26700dad1)

2. <h4>Ingestão de Dados:</h4>
<h5>Camada Bronze:</h5>
Através do Azure Databricks foi desenvolvido um pipeline para ingestão dos dados da API openbrewerydb (https://www.openbrewerydb.org), que contém dados de cervejarias.
Nessa etapa os dados são carregados no formato que a API os fornece, dessa forma, os dados são salvos em um arquivo json no ADLS, e também disponibilizados em uma tabela no Databricks estruturado na camada bronze.

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/32396a95-5538-4c7b-a01f-9a0582123a9c)

<h5>Camada Silver:</h5>
Na sequência, para a camada Silver, os dados recebem um schema, definindo data types para os dados recebidos, ocorre também a remoção de dados duplicados e é insirida uma coluna com os dados de data de inserção dos dados na camada silver.
Após isso, os dados são salvos particionados, por país, estado e cidade, em formato parquet.

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/5a080ebd-1953-44d3-84d8-555f42a6a2d4)

<h5>Camada Gold:</h5>
Na última camada, os dados são agregados em uma view contendo a quantidade de cervejarias, agregadas por tipo de cervejaria e localização.

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/4eaae7b5-5779-44bd-b393-54bf625513d1)

<h5>Estrutura dos dados no Azure ADLS:</h5>
Os arquivos foram salvos em uma estrutura organizada em pastadas por data, seguindo a seguinte lógica:
f"dbfs:/mnt/data/silver/dataset_brewery/{year}/{month}/{day}/brewery" em que year, month e day são variáveis que contém a data atual da execução do pipeline.

![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/1c59cc33-c7d6-4d99-840b-464cf14d3214)

3. <h4>Orquestração:</h4>
O Apache Airflow realiza a orquestração de todo o pipeline utilizando operadores Databricks integrados ao projeto na Azure.
Nele além da orquestração, é possível realizar o gerenciamento de erros através de logs, além de possibilitar a visualização das execuções do pipeline.
![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/04b24a4d-b0e0-436b-8fdb-15aff1a2dc49)

5. <h4>Monitoramento e observabilidade dos pipeline:</h4>
Ao final de cada processo na execução das camadas existe um INSERT em uma tabela criada na camada "monitoring" que captura a quantidade de dados inseridos, a data atual e a respectiva tabela em que eles foram inseridos.
![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/ded4309e-12f2-48d3-893b-56789a34cdaa)

Além disso, as tasks executadas para cada camada no Airflow disparam e-mails com informações sobre a execução de cada job.
![image](https://github.com/vinicius-nisidozi/data-lake-brewery/assets/113652441/975a7ee8-c019-47d5-9d3d-55dfa64b4da1)

<h4>Resultados e Impacto:</h4><br>
O resultado do projeto foi um Data Lake estruturado no ADLS, com tabelas e views disponibilizadas no Databricks, e com um pipeline sendo orquestrado pelo Apache Airflow.
A solução apresentada é robusta, escalável, proporciona colcaboração, melhorias futuras, ingestão de novos dados de novas fontes, processamento de big data com alta performance.
O projeto está publicado em minha conta Azure, todos os códigos utilizados para a execução do pipeline estão neste repositório. 
