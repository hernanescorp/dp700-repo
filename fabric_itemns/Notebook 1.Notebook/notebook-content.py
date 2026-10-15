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
# META     }
# META   }
# META }

# MARKDOWN ********************

# # NOTEBOOK GLOBAL

# MARKDOWN ********************

# ## Creation of a delta table with Spark

# CELL ********************

df = spark.createDataFrame(
    [
        ("Hernan", 41, "Ingeniero"),
        ("Maria", 20, "Analista"),
        ("Juan", 31, "Cientifico")
    ],
    "name STRING, age INT, role STRING"
)

df.write.format("delta").saveAsTable("person")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Sintax Differences Example 1

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT name, age
# MAGIC FROM person

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **KQL QUERY**
# 
# ```
# person
# | project name, age
# ```

# CELL ********************

display(spark.table("dbo.person").select("name", "age"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Sintax difference Example 2

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT count(*) AS count
# MAGIC FROM person

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **KQL**
# 
# ```
# person 
# | count
# ```


# CELL ********************

display(spark.table("person") \
.agg({"*":"count"}) \
.withColumnRenamed("count(1)", "count"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
