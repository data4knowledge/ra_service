from fastapi import FastAPI, Request, HTTPException
from model.configuration import *
from model.namespace import *
from model.registration_authority import *
from uuid import UUID

VERSION = "0.1"
SYSTEM_NAME = "d4k Registration Authority Microservice"

app = FastAPI()

@app.get("/")
def read_root():
  return { "system": SYSTEM_NAME, "version": VERSION }

@app.post("/configuration")
async def create_configuration(config: Configuration):
  return config.save_and_response

@app.post("/namespace")
async def create_namespace(namespace: NamespaceIn):
  return NamespaceOut.save_and_response(namespace) 

@app.get("/namespace/{uuid}")
def read_namespace(uuid: UUID):
  return NamespaceOut.read(uuid)

@app.get("/namespace")
def list_namespace():
  return NamespaceOut.list()

@app.post("/registration_authority")
async def create_registration_authority(authority: RegistrationAuthorityIn):
  return RegistrationAuthorityOut.save_and_response(authority) 

@app.get("/registration_authority/{uuid}")
def read_registration_authority(uuid: UUID):
  return RegistrationAuthorityOut.read(uuid)

@app.get("/registration_authority")
def list_registration_authority():
  return RegistrationAuthorityOut.list()

@app.api_route("/{path_name:path}", methods=["GET"])
async def resource(request: Request, path_name: str):
    print("PATH:", path_name, flush=True)
    # uri = PropertyUri(f'http://www.data4knowledge.dk/{path_name}')
    # klass = Model.klass_for_uri(uri)
    # print(f"Klass {klass}", flush=True)
    # if klass == None:
    #     raise HTTPException(status_code=404, detail="URI not found")
    # object = eval(klass).find(uri)
    # print(f"Object {object}", flush=True)
    # if object == None:
    #     raise HTTPException(status_code=404, detail="URI not found")
    # else:
    #     return {"type": object.__str__()}