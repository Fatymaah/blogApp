from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError)             
db = SqliteDatabase("blogs.db")
blogs = [
    {'id': 1, 'title': 'Birthday', 'body': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about  contents'},
    {'id': 2, 'title': 'Celebration', 'body': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about  contents'}
]


class Myentry(Model):
  
    title = CharField(max_length=255, unique=True)
    body = TextField(default="Body")
   

    

    class Meta:
        database = db


def initialize():
    try:
        Myentry.create_table()
    except OperationalError:
        pass
    for blog in blogs:
        try:
            Myentry.create(
                title=blog.get('title'),
                body=blog.get('body'),
                )
        except IntegrityError:
            pass