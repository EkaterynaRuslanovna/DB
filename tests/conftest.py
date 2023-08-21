import pytest
from database import Database


@pytest.fixture
def db():
    database = Database("store")
    database.connect()
    database.create_table()
    yield database
    database.close()
