from urllib.parse import urlparse
from model.api_base_model import ApiBaseModel
from pydantic import validator
import validators

class Configuration(ApiBaseModel):
  base_uri: str
  server_url: str

  @validator('base_uri')
  def uri_must_be_valid(cls, uri):
    if validators.url(uri):
      return uri
    else:
      raise ValueError('must ba a valid url')

  @validator('server_url')
  def url_must_be_valid(cls, uri):
    if validators.url(uri):
      return uri
    else:
      raise ValueError('must ba a valid url')

