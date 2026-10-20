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

# # **Notebooks in Fabric**

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.read.format("csv").option("header","true").load("Files/ep_004/assignments.csv")
# df now is a Spark DataFrame containing CSV data from "Files/ep_004/assignments.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Notebook Utils (MsSparkUtils)

# CELL ********************

notebookutils.fs.mkdirs("Files/new_folder")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.ls("Files/ep_004")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.rm("Files/new_folder", True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Notebook

# CELL ********************

notebookutils.notebook.run("nb_1")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.exit("Output Value")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.list()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.session.stop()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.runtime.context

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Get Secrets

# CELL ********************

import notebookutils

vault_url = "https://graxiano-kv.vault.azure.net/"
secret_name = "graxiano"

secreto = notebookutils.credentials.getSecret(
    vault_url,
    secret_name
)

print("Secreto recuperado correctamente:", bool(secreto))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Magic Commands

# MARKDOWN ********************

# Cell magic commands.
# ```
# %%sql, %%pyspark, %%spark
# ```

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC SELECT * FROM lk_1.dbo.person LIMIT 1000

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%pyspark
# MAGIC 
# MAGIC df = spark.sql("SELECT * FROM lk_1.dbo.person LIMIT 1000")
# MAGIC display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%spark
# MAGIC 
# MAGIC val df = spark.sql("SELECT * FROM lk_1.dbo.person LIMIT 1000")
# MAGIC display(df)

# METADATA ********************

# META {
# META   "language": "scala",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sparkr
# MAGIC 
# MAGIC results <- sql("SELECT * FROM lk_1.dbo.person LIMIT 1000")
# MAGIC head(results)

# METADATA ********************

# META {
# META   "language": "r",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC echo "Hola desde Fabric"
# MAGIC 


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC pwd


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%bash
# MAGIC ls

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 

# MARKDOWN ********************

# ## Line Magic Commands
# 
# %pip, %run

# CELL ********************

%pip install pandas


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_1

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Running Notebooks
# - Run Manually
# - Run notebooks from notebook
# 
#     - %run magic command
#     - NotebookUtils library
#         - notebookutils.notebook.run
#         - notebookutils.notebook.runMultiple
