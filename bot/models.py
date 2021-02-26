from peewee import SqliteDatabase, Model, BigIntegerField, BooleanField
from configparser import ConfigParser


# parse config
config = ConfigParser()
config.read('config.ini')
database_path = config.get('database', 'sqlite')


# database connection
database = SqliteDatabase(database_path)


# base model for other models
class BaseModel(Model):
    class Meta:
        database = database


# model that represents user
class User(BaseModel):
    user_id = BigIntegerField(primary_key=True, unique=True)
    active = BooleanField(default=True)
