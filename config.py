from importlib.metadata import metadata
import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
TEST_DATABASE = os.getenv('TEST_DATABASE', 'fase') in ('true', 'yes')
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
metadata = sqlalchemy.MetaData()