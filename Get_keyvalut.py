import os
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


KVUri = "https://dataops-poc.vault.azure.net/"
client_id = os.environ['ClientID']
client_secret = os.environ['Client_secret']
tenant_id = os.environ['Tenant_id']

# Creating a variable to store the key vault value in
account = 'account'
user = 'user'
password = 'password'
role = 'role'
warehouse = 'warehouse'
database = 'database'
schema = 'schema'
stage = 'stage'

credentials = ClientSecretCredential(client_id=client_id, client_secret=client_secret,tenant_id=tenant_id)
client = SecretClient(vault_url=KVUri, credential = credentials)

get_account_secret = client.get_secret(account).value
get_user_secret = client.get_secret(user).value
get_pass_secret = client.get_secret(password).value
get_role_secret = client.get_secret(role).value
get_warehouse_secret = client.get_secret(warehouse).value
get_database_secret = client.get_secret(database).value
get_schema_secret = client.get_secret(schema).value
get_stage_secret = client.get_secret(stage).value



