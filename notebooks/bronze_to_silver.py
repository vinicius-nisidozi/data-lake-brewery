# Databricks notebook source
from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType
from pyspark.sql.functions import current_date

# COMMAND ----------

year, month, day = datetime.now().strftime("%Y-%m-%d").split("-")

# COMMAND ----------

bronze_path = f"dbfs:/mnt/data/bronze/dataset_brewery/{year}/{month}/{day}/api_response"
df_bronze = spark.read.json(bronze_path)

# COMMAND ----------

schema = StructType([
    StructField("address_1", StringType(), True),
    StructField("address_2", StringType(), True),
    StructField("brewery_type", StringType(), True),
    StructField("city", StringType(), True),
    StructField("country", StringType(), True),
    StructField("id", StringType(), False),
    StructField("latitude", StringType(), True),
    StructField("longitude", StringType(), True),
    StructField("name", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("postal_code", StringType(), True),
    StructField("state", StringType(), True),
    StructField("state_province", StringType(), True),
    StructField("street", StringType(), True),
    StructField("website_url", StringType(), True),
    StructField("update_date", DateType(), True)
    ])

# COMMAND ----------

df_silver = df_bronze.distinct()
df_silver = df_silver.withColumn("update_date", current_date())
df_silver = spark.createDataFrame(df_silver.rdd, schema=schema)

# COMMAND ----------

silver_path = f"dbfs:/mnt/data/silver/dataset_brewery/{year}/{month}/{day}/brewery"

df_silver.write\
    .partitionBy("country", "state", "city")\
    .mode("overwrite")\
    .parquet(silver_path)

df_silver.write\
    .mode("overwrite")\
    .saveAsTable("data_lake_brewery.silver.brewery")

# COMMAND ----------

spark.sql("""
          INSERT INTO data_lake_brewery.monitoring.data
          SELECT 
            CURRENT_TIMESTAMP() AS UPDATE_TIME, 
            (SELECT COUNT(*) FROM data_lake_brewery.silver.brewery) AS QUANTITY_OF_LINES, 
            "silver.brewery" AS TABLE_NAME
          """)
