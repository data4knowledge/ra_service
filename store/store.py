from deta import Deta
import json
import os

class Store():
    
  def __init__(self, klass):
    self.__deta = Deta(os.environ['RA_SERVICE_PROJ_KEY'])
    self.__store = self.__deta.Base("ra_service.%s" % (klass))
    
  def put(self, data, key):
    self.__store.put(data, key)

  def get(self, key):
    return json.loads(self.__store.get(key)["value"])

  def list(self):
    results = []
    items = self.__store.fetch().items
    for v in items:
      results.append(v["key"])
    return results