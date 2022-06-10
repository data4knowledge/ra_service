from .api_base_model import ApiBaseModel
from uuid import uuid4
import os

class NamespaceIn(ApiBaseModel):
  name: str
  authority: str

class NamespaceOut(NamespaceIn):
  uuid: str
  uri: str

  @classmethod
  def save_and_response(cls, namespace):
    dict = vars(namespace)
    dict['uuid'] = str(uuid4())
    dict['uri'] = cls.generate_uri(dict['uuid'])
    result = NamespaceOut.parse_obj(dict) 
    uuid = result.save()
    return { 'uuid': result.uuid, 'uri': result.uri }

  @classmethod
  def generate_uri(cls, uuid):
    return "%sdataset/ns/%s" % (os.environ["RA_SERVICE_BASE_URI"], uuid)