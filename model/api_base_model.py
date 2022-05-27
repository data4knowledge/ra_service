from pydantic import BaseModel
from uuid import uuid4
from deta import Deta

class ApiBaseModel(BaseModel):

  def __init__(self):
    deta = Deta()
    self.db = deta.Base("ra_service")

  def save(self):
    self.uuid = uuid4() 
    self.db.put(self.json(), self.uuid) 
    return self.uuid

  @classmethod
  def read(cls, uuid):
    json = cls.db.get(uuid) 
    return json # cls()
    