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
    .saveAsTable("data_lake_brewery.bronze.brewery")
