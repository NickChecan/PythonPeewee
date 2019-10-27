import peewee
from database.BaseModel import BaseModel
from model.Author import Author

class Book(BaseModel):

    title = peewee.CharField(unique=True)

    # Set the Author as a Foreign Key at the Book table
    author = peewee.ForeignKeyField(Author)
