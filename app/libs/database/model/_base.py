from peewee import *

from google.protobuf.json_format import MessageToDict, ParseDict


from libs.database import db_conn
import datetime


class BaseModel(Model):
    ID = BigAutoField(primary_key=True, column_name="id")
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = DateTimeField(null=True)

    __proto__ = None

    class Meta:
        schema = "public"
        database = db_conn

    @classmethod
    def from_proto(self, msg):
        dict_msg = MessageToDict(msg)
        self.__dict__.update(dict_msg)
        pass

    @classmethod
    def to_proto(self):
        if self.__proto__ is None:
            raise NotImplementedError("Proto not implemented")
        return ParseDict(self.__dict__, self.__proto__())
        pass

    @classmethod
    def create_from_proto(self, msg):
        return self.create(**self.from_proto(msg))
        pass

    @classmethod
    def update_from_proto(self, msg):
        self.from_proto(msg)
        if self.ID is None:
            return

        self.save()

        pass

    @classmethod
    def select_to_proto(self):
        return self.select().where()
        pass
