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

# # **DP 700 NOTEBOOK**

# MARKDOWN ********************

# # Parameters

# PARAMETERS CELL ********************

dataset = "movies"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Reading data from a file in Lakehouse

# CELL ********************

df = spark.read.format("csv").option("header","true").load(f"Files/demo/{dataset}.csv")
# df now is a Spark DataFrame containing CSV data from "Files/demo/movies.csv".


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Displaying data

# CELL ********************

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Using Spark SQL

# CELL ********************

df.createOrReplaceTempView("df_view")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * 
# MAGIC , now() AS ts
# MAGIC FROM df_view

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_ts = spark.sql('''
    SELECT * 
    , now() AS ts
    FROM df_view
'''
)

display(df_ts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Writing data to a table in Lakehouse 

# CELL ********************

spark.sql('''
CREATE SCHEMA IF NOT EXISTS sch
''')

df_ts.write.mode("overwrite").format("delta").saveAsTable(f"sch.{dataset}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql('''
CREATE TABLE sch.table1
(column_id INT  NOT NULL)
''')

# spark.sql('''
# DROP TABLE sch.table1
# ''')


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_table = spark.sql(f"SELECT * FROM lk_1.sch.{dataset}")
display(df_table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Using NotebookUtils to set an exit value for the notebook

# CELL ********************

notebookutils.notebook.exit(f"Dataset {dataset} was processed Ok")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
