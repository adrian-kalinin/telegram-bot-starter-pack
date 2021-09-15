from peewee import Model, IntegerField, BooleanField
from playhouse.sqliteq import SqliteQueueDatabase

from settings import SQLITE_PATH


# database connection
database = SqliteQueueDatabase(SQLITE_PATH)


# base model for other models
class BaseModel(Model):
    class Meta:
        database = database


# model that represents user
class User(BaseModel):
    user_id = IntegerField(primary_key=True, unique=True)
    active = BooleanField(default=True)
