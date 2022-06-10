from model.api_base_model import ApiBaseModel
from pydantic import validator
import validators
import os

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

  def save_and_response(self):
    os.environ["RA_SERVICE_BASE_URI"] = self.base_uri
    os.environ["RA_SERVICE_SERVER_URL"] = self.server_url
    return { 'base_uri': os.environ["RA_SERVICE_BASE_URI"], 'server_uri': os.environ["RA_SERVICE_SERVER_URL"] }


