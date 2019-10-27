import peewee
from database.BaseModel import BaseModel

class Author(BaseModel):

    name = peewee.CharField(unique=True)