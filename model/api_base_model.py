from pydantic import BaseModel
from uuid import uuid4
from store.store import Store

class ApiBaseModel(BaseModel):
  
  def save(self):
    store = Store()
    uuid = str(uuid4())
    store.put(self.json(), self.__class__.__name__, uuid) 
    return uuid

  @classmethod
  def read(cls, uuid):
    return Store().get(str(uuid)) # uuid may be UUID or string 

  @classmethod
  def list(cls):
    return Store(cls.__name__).list()


