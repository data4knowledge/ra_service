from pydantic import BaseModel
from uuid import uuid4
from store.store import Store

class ApiBaseModel(BaseModel):

  def save(self):
    store = Store(self.__class__.__name__)
    uuid = str(uuid4())
    store.put(self.json(), uuid) 
    return uuid

  @classmethod
  def read(cls, uuid):
    return Store(cls.__name__).get(uuid) 

  @classmethod
  def list(cls):
    return Store(cls.__name__).list()


