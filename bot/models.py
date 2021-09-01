from peewee import SqliteDatabase, Model, IntegerField, BooleanField

from settings import SQLITE_PATH


# database connection
database = SqliteDatabase(SQLITE_PATH)


# base model for other models
class BaseModel(Model):
    class Meta:
        database = database


# model that represents user
class User(BaseModel):
    user_id = IntegerField(primary_key=True, unique=True)
    active = BooleanField(default=True)
