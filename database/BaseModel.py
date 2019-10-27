import peewee

# SQLite Database creation
db = peewee.SqliteDatabase('books.db')

class BaseModel(peewee.Model):

    class Meta:
        database = db