# Databricks notebook source
from datetime import datetime

# COMMAND ----------

year, month, day = datetime.now().strftime("%Y-%m-%d").split("-")

# COMMAND ----------

spark.sql(f"""
          CREATE OR REPLACE VIEW data_lake_brewery.gold.breweries_vw AS
          SELECT
                COUNT(id) AS brewery_qunatity,
                brewery_type, 
                country, 
                state, 
                city
            FROM data_lake_brewery.silver.brewery
            GROUP BY brewery_type, country, state, city
          """)

# COMMAND ----------

df_gold = spark.sql("""
    SELECT
        COUNT(id) AS brewery_qunatity,
        brewery_type, 
        country, 
        state, 
        city
    FROM data_lake_brewery.silver.brewery
    GROUP BY brewery_type, country, state, city
          """)

# COMMAND ----------

gold_path = f"dbfs:/mnt/data/gold/dataset_brewery/{year}/{month}/{day}/breweries"

df_gold.write\
    .mode("overwrite")\
    .parquet(gold_path)

# COMMAND ----------

spark.sql("""
          INSERT INTO data_lake_brewery.monitoring.data
          SELECT 
            CURRENT_TIMESTAMP() AS UPDATE_TIME, 
            (SELECT COUNT(*) FROM data_lake_brewery.gold.breweries_vw) AS QUANTITY_OF_LINES, 
            "gold.breweries_vw" AS TABLE_NAME
          """)

# COMMAND ----------

# MAGIC %md
# MAGIC
