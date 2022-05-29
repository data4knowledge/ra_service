from typing import List, Union
from .api_base_model import ApiBaseModel

class Company(ApiBaseModel):
  identifier: str
  country_code: str
  

