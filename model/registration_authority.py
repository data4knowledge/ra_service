from typing import Union
from .api_base_model import ApiBaseModel
from .ror import ROR
from .grid import GRID
from .dun import DUN
from .company import Company

class RegistrationAuthority(ApiBaseModel):
  uuid: Union[str, None] = None
  name: str
  namespace: str
  ror: Union[ROR, None] = None
  grid: Union[GRID, None] = None
  dun: Union[DUN, None] = None
  company: Union[Company, None] = None
