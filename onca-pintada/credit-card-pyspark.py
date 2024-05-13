from pyspark.sql import SparkSession
from imblearn.over_sampling import SMOTE
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
from datetime import datetime
from google.api_core.exceptions import NotFound

spark = SparkSession.builder.appName('creditcardfraud').getOrCreate()
client = storage.Client()
bucket = client.get_bucket('analysis-4bank')

bq_client = bigquery.Client()
dataset_id = f'{bq_client.project}.creditCardFraudAnalysis'
dataset = bigquery.Dataset(dataset_id)
dataset.location = 'US'

try:
    bq_client.get_dataset(dataset_id)
    print(f'\n{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Dataset {dataset_id} already exists')
except NotFound:
    print(f'\n{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Dataset {dataset_id} is not found. Creating {dataset_id}...')
    dataset = bq_client.create_dataset(dataset, timeout=30)
    print(f'{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Created dataset {bq_client.project}.{dataset.dataset_id}')

print(f'\n{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Created BigQuery dataset {bq_client.project}.{dataset.dataset_id}')

print(f'\n{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Loading dataset...', end=' ')
df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load('gs://datasets-4bank/creditcard.csv')
print(f'{df.count()} rows e {len(df.columns)} columns')
df.show(5)

pdf = df.toPandas()

print(f'\n{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Applying SMOTE...')
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(pdf.drop('Class', axis=1), pdf['Class'])
balanced_df = spark.createDataFrame(pd.concat([pd.DataFrame(X_res), pd.DataFrame(y_res, columns=['Class'])], axis=1))

def save_bigquery(df, table_name):
    table_id = f'{dataset_id}.{table_name}'

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        field_delimiter=',',
        autodetect=True,
        write_disposition="WRITE_TRUNCATE",
    )

    print(f'{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Loading {table_name} to BigQuery...')
    uri = f'gs://analysis-4bank/creditcard/{table_name}.csv'
    load_job = bq_client.load_table_from_uri(uri, table_id, job_config=job_config)

    load_job.result()

    print(f'{datetime.now().strftime("%y/%m/%d %H:%M:%S")} {table_name} loaded to BigQuery!\n')

def save_results(df, file_name):
    print(f'{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Saving the analysis...')
    df.coalesce(1).write.option('header', 'true').option('delimiter', ',').mode('overwrite').csv(f'gs://analysis-4bank/creditcard/{file_name}.csv')

    blobs = bucket.list_blobs(prefix=f'creditcard/{file_name}.csv/')

    for blob in blobs:
        if '.' in blob.name.split('/')[-1]:
            print(f'{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Renaming {blob.name} ...')
            bucket.rename_blob(blob, f'creditcard/{file_name}.csv')
        else:
            print(f'{datetime.now().strftime("%y/%m/%d %H:%M:%S")} Removing {blob.name} ...')
            bucket.delete_blobs([blob.name])
    print()

    save_bigquery(df, file_name)

save_results(df, 'creditcard_unbalanced')
save_results(balanced_df, 'creditcard_smote_balanced')
