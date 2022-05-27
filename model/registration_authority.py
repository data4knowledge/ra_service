from pydantic import Union
from api_base_model import ApiBaseModel

class RegistrationAuthority(ApiBaseModel):
  uuid: Union[str, None] = None
  uri: Union[str, None] = None
  name: str
  namespace: str
  

