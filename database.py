from peewee import Model, SqliteDatabase, FloatField, CharField, DateTimeField
import os
from datetime import datetime

db = SqliteDatabase(os.getcwd() + '/cords.db')


class Cords(Model):
    serial = CharField()
    lat = FloatField()
    lon = FloatField()
    time = DateTimeField(default=datetime.utcnow())

    class Meta:
        database = db


Cords.create_table()
