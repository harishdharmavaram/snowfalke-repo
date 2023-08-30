import pytest
import json
from snowflake_connector import SnowflakeConnector


# Fixture to set up and tear down a Snowflake connection for testing
@pytest.fixture(scope="module")
def snowflake_connection():
    # Set up the Snowflake connection here, return the connection object

    # with open("secret_dev.json") as secrets_file:
     #   secrets = json.load(secrets_file)

   connection_parameters ={
    "user" : "Aklesh",
    "password" : "Ran@_123",
    "warehouse" : "COMPUTE_WH",
    "database" : "DEMO",
    "schema" : "PUBLIC",
    "account" : "yudedse-av63812",
    "role" : "ACCOUNTADMIN",
    "stage" : "STG"
}
    connection = SnowflakeConnector(user, password, account, warehouse, database, schema)
    connection.connect()

    yield connection
    # Teardown: Close the connection after testing
    connection.close()


# Test case to check if the Snowflake connection is successful
def test_snowflake_connection(snowflake_connection):
    assert snowflake_connection.is_connected()
