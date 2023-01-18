from pymodm import MongoModel, fields


class Logs(MongoModel):
    _id = fields.CharField(primary_key=True)
    time = fields.DateTimeField()
    levelname = fields.CharField()
    message = fields.CharField()
    lineno = fields.CharField()
    pathname = fields.CharField()


class Players(MongoModel):
    _id = fields.CharField(primary_key=True)
    wins = fields.IntegerField()
    deaths = fields.IntegerField()


class Revolvers(MongoModel):
    _id = fields.CharField(primary_key=True)
    descr = fields.CharField(max_length=1000)
    drum_capacity = fields.IntegerField()