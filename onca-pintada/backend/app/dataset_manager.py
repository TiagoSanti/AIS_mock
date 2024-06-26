from google.cloud import storage
import google.auth
import pandas as pd
from io import StringIO
from google.oauth2 import service_account
import os

BUCKET_NAME = 'banks-dev-392615.appspot.com'
CREDENTIALS_PATH = 'banks-dev-392615-7412df8a19f0.json'

def get_credentials():
    '''
    Tenta carregar as credenciais a partir do arquivo JSON. Se não conseguir,
    cai de volta para as credenciais padrão do Google Cloud.

    ### Retorno:
    - `google.auth.credentials.Credentials`: Objeto de credenciais do Google Cloud.
    '''
    try:
        return service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)
    except Exception as e:
        credentials, _ = google.auth.default()
        return credentials
    
def load_csv(dataset_id: str, file_name: str, index: bool = False, from_gcs: bool = False) -> pd.DataFrame:
    '''
    Esta função carrega um arquivo CSV localmente ou de um bucket do Google Cloud Storage.
    
    ### Parâmetros:
    - `dataset_id` (str, obrigatório): O ID do dataset. O arquivo CSV correspondente a este dataset_id
                                        deve estar localizado no diretório `datasets/{dataset_id}/{file_name}.csv`
                                        se `from_gcs` for `False`, ou no bucket do Google Cloud Storage sob o
                                        caminho `{dataset_id}/{file_name}.csv` se `from_gcs` for `True`.
    - `file_name` (str, obrigatório): O nome do arquivo CSV.
    - `index` (bool, opcional): Se o índice do DataFrame deve ser salvo no arquivo CSV. O padrão é `False`.
    - `from_gcs` (bool, opcional): Se o arquivo CSV deve ser carregado do bucket do Google Cloud Storage. O padrão é `False`.
    
    ### Retorna:
    - `pd.DataFrame`: Um DataFrame pandas contendo os dados do arquivo CSV carregado.
    '''
    if from_gcs:
        return load_csv_from_gcs(dataset_id, file_name, index)
    else:
        return load_csv_from_local(dataset_id, file_name, index)

def load_csv_from_gcs(dataset_id: str, file_name: str, index: bool = False) -> pd.DataFrame:
    '''
    Esta função baixa e carrega um arquivo CSV de um bucket do Google Cloud Storage.

    ### Parâmetros:
    - `dataset_id` (str, obrigatório): O ID do dataset. O arquivo CSV correspondente a este dataset_id
                                        deve estar localizado no bucket do Google Cloud Storage sob o
                                        caminho `{dataset_id}/{file_name}.csv`.
    - `file_name` (str, obrigatório): O nome do arquivo CSV.
    - `index` (bool, opcional): Se o índice do DataFrame deve ser salvo no arquivo CSV. O padrão é `False`.

    ### Retorna:
    - `pd.DataFrame`: Um DataFrame pandas contendo os dados do arquivo CSV baixado.

    ### Gera uma exceção:
    - `google.cloud.exceptions.NotFound`: Se o arquivo CSV correspondente ao dataset_id não for encontrado no bucket.
    '''
    credentials = get_credentials()
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(BUCKET_NAME)
    blob_name = f'{dataset_id}/{file_name}.csv'
    blob = bucket.blob(blob_name)
    
    blob_content_as_string = blob.download_as_text()
    if index:
        data = pd.read_csv(StringIO(blob_content_as_string), index_col=0)
    else:
        data = pd.read_csv(StringIO(blob_content_as_string))

    return data

def load_csv_from_local(dataset_id: str, file_name: str, index: bool = False) -> pd.DataFrame:
    '''
    Esta função carrega um arquivo CSV localmente.

    ### Parâmetros:
    - `dataset_id` (str, obrigatório): O ID do dataset. O arquivo CSV correspondente a este dataset_id
                                        deve estar localizado no diretório `app/datasets/{dataset_id}/{file_name}.csv`.
    - `file_name` (str, obrigatório): O nome do arquivo CSV.
    - `index` (bool, opcional): Se o índice do DataFrame deve ser salvo no arquivo CSV. O padrão é `False`.

    ### Retorna:
    - `pd.DataFrame`: Um DataFrame pandas contendo os dados do arquivo CSV carregado.

    ### Gera uma exceção:
    - `FileNotFoundError`: Se o arquivo CSV correspondente ao dataset_id não for encontrado localmente.
    '''
    file_path = f'app/datasets/{dataset_id}/{file_name}.csv'
    if index:
        return pd.read_csv(file_path, index_col=0)
    return pd.read_csv(file_path)

def save_df(df: pd.DataFrame, dataset_id: str, file_name: str, index: bool = False, to_gcs: bool = False) -> None:
    '''
    Esta função salva um DataFrame pandas como um arquivo CSV localmente ou em um bucket do Google Cloud Storage.
    
    ### Parâmetros:
    - `df` (pd.DataFrame, obrigatório): O DataFrame a ser salvo.
    - `dataset_id` (str, obrigatório): O ID do dataset. O arquivo CSV será salvo no diretório `app/datasets/{dataset_id}/{file_name}.csv`
                                       se `to_gcs` for `False`, ou no bucket do Google Cloud Storage sob o caminho
                                       `{dataset_id}/{file_name}.csv` se `to_gcs` for `True`.
    - `file_name` (str, obrigatório): O nome do arquivo CSV.
    - `index` (bool, opcional): Se o índice do DataFrame deve ser salvo no arquivo CSV. O padrão é `False`.
    - `to_gcs` (bool, opcional): Se o arquivo CSV deve ser salvo no bucket do Google Cloud Storage. O padrão é `False`.
    
    ### Não retorna nada.
    '''
    if to_gcs:
        save_df_to_gcs(df, dataset_id, file_name, index)
    else:
        save_df_to_local(df, dataset_id, file_name, index)

def save_df_to_local(df: pd.DataFrame, dataset_id: str, file_name: str, index: bool = False) -> None:
    '''
    Esta função salva um DataFrame pandas como um arquivo CSV localmente.

    ### Parâmetros:
    - `df` (pd.DataFrame, obrigatório): O DataFrame a ser salvo.
    - `dataset_id` (str, obrigatório): O ID do dataset. O arquivo CSV será salvo no diretório `app/datasets/{dataset_id}/{file_name}.csv`.
    - `file_name` (str, obrigatório): O nome do arquivo CSV.
    - `index` (bool, opcional): Se o índice do DataFrame deve ser salvo no arquivo CSV. O padrão é `False`.

    ### Não retorna nada.

    ### Gera uma exceção:
    - `FileNotFoundError`: Se ocorrer um erro ao tentar salvar o arquivo localmente.
    '''
    os.makedirs(f'app/datasets/{dataset_id}', exist_ok=True)

    df.to_csv(f'app/datasets/{dataset_id}/{file_name}.csv', index=index)

def save_df_to_gcs(df: pd.DataFrame, dataset_id: str, file_name: str, index: bool = False) -> None:
    '''
    Esta função salva um DataFrame pandas como um arquivo CSV em um bucket do Google Cloud Storage e torna o arquivo carregado público.

    ### Parâmetros:
    - `df` (pd.DataFrame, obrigatório): O DataFrame a ser salvo.
    - `dataset_id` (str, obrigatório): O ID do dataset. O arquivo CSV será salvo no bucket do Google Cloud Storage 
                                       sob o caminho `{dataset_id}/{file_name}.csv`.
    - `file_name` (str, obrigatório): O nome do arquivo CSV.
    - `index` (bool, opcional): Se o índice do DataFrame deve ser salvo no arquivo CSV. O padrão é `False`.

    ### Não retorna nada.

    ### Gera uma exceção:
    - `google.cloud.exceptions.GoogleCloudError`: Se ocorrer um erro ao tentar salvar o arquivo no bucket.
    '''
    credentials = get_credentials()
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(BUCKET_NAME)
    blob_name = f'{dataset_id}/{file_name}.csv'
    blob = bucket.blob(blob_name)

    blob.upload_from_string(df.to_csv(index=index), 'text/csv')