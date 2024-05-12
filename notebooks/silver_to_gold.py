# Databricks notebook source
from datetime import datetime

# COMMAND ----------

year, month, day = datetime.now().strftime("%Y-%m-%d").split("-")

silver_path = f"dbfs:/mnt/data/silver/dataset_brewery/{year}/{month}/{day}/brewery"
df_silver = spark.read.parquet(silver_path)

# COMMAND ----------

df_silver.createOrReplaceTempView("BREWERY")

query = """
SELECT
    COUNT(id) AS brewery_qunatity,
    brewery_type, 
    country, 
    state, 
    city
FROM BREWERY
GROUP BY brewery_type, country, state, city
"""
df_gold = spark.sql(query)

# COMMAND ----------

gold_path = f"dbfs:/mnt/data/gold/dataset_brewery/{year}/{month}/{day}/breweries"

df_gold.write\
    .mode("overwrite")\
    .parquet(gold_path)

# COMMAND ----------

# MAGIC %md
# MAGIC
