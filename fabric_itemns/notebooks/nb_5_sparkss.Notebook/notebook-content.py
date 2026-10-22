# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "dba0f676-0c05-4c16-8229-401e855faa24",
# META       "default_lakehouse_name": "lk_1",
# META       "default_lakehouse_workspace_id": "b609f989-9bba-4dfe-ac3f-e28288cbe234",
# META       "known_lakehouses": [
# META         {
# META           "id": "dba0f676-0c05-4c16-8229-401e855faa24"
# META         }
# META       ]
# META     },
# META     "event_stream": {
# META       "known_event_streams": [
# META         {
# META           "artifact_id": "8e72df86-c60e-4f85-aa7f-ced7695db9a2",
# META           "stream_id": "8e72df86-c60e-4f85-aa7f-ced7695db9a2"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ## SPARK STRUCTURED STREAMING

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Event stream and DataSources IDS

# PARAMETERS CELL ********************

# Set the event stream item and datasource IDs
__in_eventstream_item_id = "8e72df86-c60e-4f85-aa7f-ced7695db9a2"
__in_eventstream_datasource_id = "6a55f8a2-85a7-4360-97be-75e2b679a8e2"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# from pyspark.sql.types import StringType
# from pyspark.sql.dataframe import DataFrame


# eventstream_options = {
#     "eventstream.itemid": __in_eventstream_item_id,
#     "eventstream.datasourceid": __in_eventstream_datasource_id
# }


# # Read from Kafka using the config map
# df_raw = spark.readStream.format("kafka").options(**eventstream_options).load()

# decoded_df = df_raw.select(
#     col("key").cast(StringType()).alias("key"),
#     col("value").cast(StringType()).alias("value"),
#     col("partition"),
#     col("offset")
# )

# def showDf(x:DataFrame, y:int):
#     x.show()

# # Print messages to the console
# query = decoded_df.writeStream.foreachBatch(showDf).outputMode("append").start()
# query.awaitTermination()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## SPARK STREAMING PROCESING

# MARKDOWN ********************

# Import types and Libraries to processes data

# CELL ********************

from pyspark.sql.types import(
    StructType,
    StringType,
    DoubleType,
    TimestampType
)
import pyspark.sql.functions as F
import time


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Define paths and name tables

# CELL ********************

checkpoint_path = "Files/local_workstation_stream/checkpoint"
schema_name = "stream"
table_name = "local_workstation_metrics"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Json Schema

# CELL ********************

metrics_schema = (
    StructType()
    .add("host", StringType())
    .add("cpu_percent", DoubleType())
    .add("memory_percent", DoubleType())
    .add("disk_percent", DoubleType())
    .add("gpu_temperature_c", DoubleType())
    .add("timestamp", TimestampType())
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Define raw_stream_df 
# this df is still an unbounded Streaming Dataframe

# CELL ********************

eventstream_options = {
    "eventstream.itemid": __in_eventstream_item_id,
    "eventstream.datasourceid": __in_eventstream_datasource_id
}

# Read from Kafka using the config map
raw_stream_df = (
    spark.readStream
    .format("kafka")
    .options(**eventstream_options)
    .load())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Decoding Value

# CELL ********************

raw_stream_df.isStreaming

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

decoded_stream_df = (
    raw_stream_df
    .select(
        F.col("value").cast("string").alias("json_value"),
        F.col("partition"),
        F.col("offset")
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Parsing Stream Dataframe

# CELL ********************

parsed_stream_df = (
    decoded_stream_df
    .select(
        F.from_json(
            F.col("json_value"),
            metrics_schema
        ).alias("data"),
        "partition",
        "offset"
    )
    .select(
        "data.*",
        "partition",
        "offset"
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

parsed_stream_df.isStreaming

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

transformed_stream_df = (
    parsed_stream_df
    .withColumn(
        "processed_timestamp",
        F.current_timestamp()
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

transformed_stream_df.isStreaming

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Writing into a Delta Table

# CELL ********************

deltastream = (
    transformed_stream_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .start(f"Tables/{schema_name}/{table_name}")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

deltastream.stop()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

deltastream.isActive

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

while deltastream.isActive:
    print("✅ Stream is running...")
    print("📊 Last progress:", deltastream.lastProgress)
    time.sleep(5)

print("❌ Stream has stopped.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM lk_1.stream.local_workstation_metrics LIMIT 1000")

df_count = spark.sql(''' 
    SELECT COUNT(*) 
    FROM lk_1.stream.local_workstation_metrics 
'''
)
display(df)
display(df_count)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
