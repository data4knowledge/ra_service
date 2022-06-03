from typing import List, Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class NamespacePost(ApiBaseModel):
  name: str
  authority: str

class NamespaceGet(ApiBaseModel):
  uuid: UUID
  name: str
  authority: str
