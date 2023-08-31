from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

KVUri = "https://dataops-poc.vault.azure.net/"
client_id = "db2a1bcb-cb13-494d-9434-30b475033623"
client_secret = "tBO8Q~gXKf_d4bO_YCH9~cDImHREduWJ3-u4ndvw"
tenant_id = "9c9c6250-26b3-4f0c-90d9-0bc5a404777d"

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



