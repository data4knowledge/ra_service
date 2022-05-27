from typing import List, Union
from .api_base_model import ApiBaseModel

class Namespace(ApiBaseModel):
  uuid: Union[str, None] = None
  uri: Union[str, None] = None
  name: str
  authority: str

