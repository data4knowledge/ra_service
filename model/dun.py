from pydantic import validator
from .api_base_model import ApiBaseModel

class DUN(ApiBaseModel):
  identifier: str

  @validator('identifier')
  def identifier_must_be_valid(cls, identifier):
    if len(identifier) == 9 and identifier.isdigit():
      return identifier
    else:
      raise ValueError('must ba a 9 digit string')
