# Databricks notebook source
import requests
import json
from datetime import datetime

# COMMAND ----------

def extract_data(url):
    response = requests.request("GET", url)
    status_code = response.status_code

    if status_code != 200:
        raise Exception("Request failed.")

    return response.json()

# COMMAND ----------

response = extract_data("https://api.openbrewerydb.org/breweries")

# COMMAND ----------

json_string = json.dumps(response)
df_bronze = spark.read.json(spark.sparkContext.parallelize([json_string])).coalesce(1)

# COMMAND ----------

year, month, day = datetime.now().strftime("%Y-%m-%d").split("-")

path = f"dbfs:/mnt/data/bronze/dataset_brewery/{year}/{month}/{day}/api_response"
df_bronze.write.json(path, mode="overwrite")

df_bronze.write\
    .mode("overwrite")\
    .saveAsTable("data_lake_brewery.bronze.brewery")

# COMMAND ----------

spark.sql("""
          INSERT INTO data_lake_brewery.monitoring.data
          SELECT 
            CURRENT_TIMESTAMP() AS UPDATE_TIME, 
            (SELECT COUNT(*) FROM data_lake_brewery.bronze.brewery) AS QUANTITY_OF_LINES, 
            "bronze.brewery" AS TABLE_NAME
          """)
