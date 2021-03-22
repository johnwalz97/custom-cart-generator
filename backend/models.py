from peewee import MySQLDatabase, Model, AutoField, CharField

import config

db = MySQLDatabase(
    database=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
)


class Shop(Model):
    id = AutoField()
    shop = CharField()
    token = CharField()
    status = CharField()

    class Meta:
        database = db


db.connect()
