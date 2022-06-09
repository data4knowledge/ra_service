from typing import List, Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class NamespaceIn(ApiBaseModel):
  name: str
  authority: str

class NamespaceOut(NamespaceIn):
  uuid: UUID
