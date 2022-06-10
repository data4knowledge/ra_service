from typing import Union
from .api_base_model import ApiBaseModel
from .ror import ROR
from .grid import GRID
from .dun import DUN
from .company import Company
from uuid import uuid4
import os

class RegistrationAuthorityIn(ApiBaseModel):
  name: str
  namespace: str
  dun: Union[DUN, None]
  ror: Union[ROR, None]
  grid: Union[GRID, None]
  company: Union[Company, None]

class RegistrationAuthorityOut(RegistrationAuthorityIn):
  uuid: str
  uri: str

  @classmethod
  def save_and_response(cls, ra):
    dict = vars(ra)
    dict['uuid'] = str(uuid4())
    dict['uri'] = cls.generate_uri(dict['uuid'])
    result = RegistrationAuthorityOut.parse_obj(dict) 
    return result.save()

  @classmethod
  def generate_uri(cls, uuid):
    return "%sra/%s" % (os.environ["RA_SERVICE_BASE_URI"], uuid)


