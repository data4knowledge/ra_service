from typing import List, Union
from .api_base_model import ApiBaseModel
from .ror import ROR
from .grid import GRID
from .dun import DUN
from .company import Company
from uuid import UUID

class RegistrationAuthorityPost(ApiBaseModel):
  name: str
  namespace: UUID
  dun: Union[DUN, None]
  ror: Union[ROR, None]
  grid: Union[GRID, None]
  company: Union[Company, None]

class RegistrationAuthorityGet(ApiBaseModel):
  uuid: UUID
  name: str
  namespace: UUID
  dun: Union[DUN, None]
  ror: Union[ROR, None]
  grid: Union[GRID, None]
  company: Union[Company, None]
