from peewee import *

from google.protobuf.json_format import MessageToDict, ParseDict

import snakecase

from libs.database import db_conn
import datetime


def change_case(str):
    # return "".join(["_" + i.lower() if i.isupper() else i for i in str]).lstrip("_")
    return snakecase.convert(str)


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

        return self

    @classmethod
    def to_proto(self):
        if self.__proto__ is None:
            raise NotImplementedError("Proto not implemented")
        return ParseDict(self.__dict__, self.__proto__())
        pass

    @classmethod
    def create_from_proto(self, msg):
        dict_msg = MessageToDict(msg)
        dict_set = {}
        # self.__dict__.update(dict_msg)
        print(dict_msg)
        for key, value in dict_msg.items():
            if key != "id":
                dict_set[change_case(key)] = value
                # setattr(dict_set, change_case(key), value)
                # setattr(dict_set, "ID", value)
        print(dict_set)
        query =  self.insert(**dict_set)
        query.execute()
        # return self.create(**self.from_proto(msg))
        pass

    @classmethod
    def update_from_proto(self, msg):

        dict_msg = MessageToDict(msg)
        dict_set = {}
        # self.__dict__.update(dict_msg)
        for key, value in dict_msg.items():
            setattr(dict_set, change_case(key), value)
            if key == "id":
                dict_set.ID = value

        if self.ID is None:
            return
        query = self.update(**dict_set).where(self.ID == dict_set.ID)
        query.execute()
        pass

    @classmethod
    def select_to_proto(self):
        return self.select().where()
        pass
