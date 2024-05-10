# Databricks notebook source
import requests
import json

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
df_bronze = spark.read.json(spark.sparkContext.parallelize([json_string]))

# COMMAND ----------

path = "dbfs:/mnt/data/bronze/dataset_brewery/brewery_raw"
df_bronze\
    .write\
    .format("delta")\
    .mode("overwrite")\
    .save(path)
