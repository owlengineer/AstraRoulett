from pymodm import MongoModel, fields


class Logs(MongoModel):
    _id = fields.CharField(primary_key=True)
    time = fields.DateTimeField()
    levelname = fields.CharField()
    message = fields.CharField()
    lineno = fields.CharField()
    pathname = fields.CharField()


class Players(MongoModel):
    name = fields.CharField(primary_key=True, max_length=80)
    wins = fields.IntegerField()
    deaths = fields.IntegerField()


class Revolvers(MongoModel):
    name = fields.CharField(primary_key=True, max_length=80)
    descr = fields.CharField(max_length=1000)
    drum_capacity = fields.IntegerField()
    drum_turn_period = fields.FloatField()