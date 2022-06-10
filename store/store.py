from deta import Deta
import json
import os

class Store():
    
  def __init__(self):
    self.__deta = Deta(os.environ['RA_SERVICE_PROJ_KEY'])
    self.__store = self.__deta.Base("ra_service")
    
  def put(self, data, klass, uri, key):
    self.__store.put({ 'value': data, 'uri': uri, 'klass': klass }, key)

  def get(self, key):
    data = self.__store.get(key)["value"]
    return data

  def get_by_uri(self, uri):
    items = self.__store.fetch({ "uri": uri }).items
    for v in items:
      return v["value"]
    return None

  def list(self, klass):
    results = []
    items = self.__store.fetch({"klass": klass.__name__}).items
    for v in items:
      results.append(v["key"])
    return results