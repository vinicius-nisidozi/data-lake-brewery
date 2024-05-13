from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime

with DAG(
    'brewery_data',
    start_date=datetime(2024, 5, 12),
    schedule_interval="0 9 * * *"
    ) as dag:

    api_to_bronze = DatabricksRunNowOperator(
      task_id = 'api-to-bronze',
      databricks_conn_id = 'databricks_default',
      job_id = 1019727331507131
      )

    bronze_to_silver = DatabricksRunNowOperator(
      task_id = 'bronze-to-silver',
      databricks_conn_id = 'databricks_default',
      job_id = 517068571902468
      )

    silver_to_gold = DatabricksRunNowOperator(
      task_id = 'silver-to-gold',
      databricks_conn_id = 'databricks_default',
      job_id = 492001987316508
      )

    api_to_bronze >> bronze_to_silver >> silver_to_gold