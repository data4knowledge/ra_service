from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from uuid import uuid4
from store.store import Store

class ApiBaseModel(BaseModel):
  
  def save(self):
    store = Store()
    store.put(jsonable_encoder(self), self.__class__.__name__, self.uri, self.uuid) 
    return self.uuid

  @classmethod
  def read(cls, uuid):
    return Store().get(str(uuid)) # uuid may be UUID or string 

  @classmethod
  def read_by_uri(cls, uri):
    return Store().get_by_uri(uri) 

  @classmethod
  def list(cls):
    return Store().list(cls)


