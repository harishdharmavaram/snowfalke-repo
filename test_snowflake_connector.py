import pytest
import json
from snowflake_connector import SnowflakeConnector


# Fixture to set up and tear down a Snowflake connection for testing
@pytest.fixture(scope="module")
def snowflake_connection():
    # Set up the Snowflake connection here, return the connection object

    with open("secret_dev.json") as secrets_file:
        secrets = json.load(secrets_file)

    user = secrets["snowflake"]["snowflake_user"]
    password = secrets["snowflake"]["snowflake_password"]
    warehouse = secrets["snowflake"]["snowflake_warehouse"]
    database = secrets["snowflake"]["snowflake_database"]
    schema = secrets["snowflake"]["snowflake_schema"]
    account = secrets["snowflake"]["snowflake_account"]

    connection = SnowflakeConnector(user, password, account, warehouse, database, schema)
    connection.connect()

    yield connection
    # Teardown: Close the connection after testing
    connection.close()


# Test case to check if the Snowflake connection is successful
def test_snowflake_connection(snowflake_connection):
    assert snowflake_connection.is_connected()