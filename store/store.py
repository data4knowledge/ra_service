from deta import Deta
import json
import os

class Store():
    
  def __init__(self):
    self.__deta = Deta(os.environ['RA_SERVICE_PROJ_KEY'])
    self.__store = self.__deta.Base("ra_service")
    
  def put(self, data, klass, key):
    self.__store.put({ 'value': data, 'klass': klass }, key)

  def get(self, key):
    print("KEY", key)
    print("DATA", self.__store.get(key))
    #data = json.loads(self.__store.get(key)["value"])
    data = self.__store.get(key)["value"]
    #data.pop('key', None)
    #data["uuid"] = key
    return data

  def list(self, klass):
    results = []
    items = self.__store.fetch({"klass": klass.__name__}).items
    for v in items:
      results.append(v["key"])
    return results