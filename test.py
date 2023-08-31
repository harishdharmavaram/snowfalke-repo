import unittest
import snowflake.connector
from snowflake_connector import SnowflakeConnector
import Get_keyvalut


class TestAddFishToAquarium(unittest.TestCase):
    def add_fish_to_aquarium(self, fish_list):
        if len(fish_list) > 10:
            raise ValueError("A maximum of 10 fish can be added to the aquarium")
        return {"tank_a": fish_list}

    def test_add_fish_to_aquarium_success(self):
        actual = self.add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)


class SnowflakeConnection(unittest.TestCase):
    # Set up the Snowflake connection here, return the connection object
    user = Get_keyvalut.get_user_secret
    password = Get_keyvalut.get_pass_secret
    account = Get_keyvalut.get_account_secret
    warehouse = Get_keyvalut.get_warehouse_secret
    database = Get_keyvalut.get_database_secret
    schema = Get_keyvalut.get_schema_secret
    role = Get_keyvalut.get_role_secret

    connection = SnowflakeConnector(user, password, account, warehouse, database, schema)
    connection.connect()

    def connect(self):
        self.connection = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )

    def is_connected(self):
        return self.connection is not None
    # Teardown: Close the connection after testing
    connection.close()


class TestSnowflakeConnection(unittest.TestCase):

    def test_snowflake_connection(self):
        connection = SnowflakeConnection()
        self.assertTrue(connection.is_connected())

