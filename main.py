from argparse import Namespace
from fastapi import FastAPI
from model.namespace import *
from model.registration_authority import *
from uuid import UUID

VERSION = "0.1"
SYSTEM_NAME = "d4k Registration Authority Microservice"

app = FastAPI()

@app.get("/")
def read_root():
  return {"Version":VERSION, "System": SYSTEM_NAME}

@app.post("/namespace")
async def create_namespace(namespace: NamespacePost):
  return namespace.save()

@app.get("/namespace/{uuid}")
def read_namespace(uuid: UUID):
  return NamespaceGet.read(uuid)

@app.get("/namespace")
def list_namespace():
  return NamespaceGet.list()

@app.post("/registration_authority")
async def create_registration_authority(authority: RegistrationAuthorityPost):
  return authority.save()

@app.get("/registration_authority/{uuid}")
def read_registration_authority(uuid: UUID):
  return RegistrationAuthorityGet.read(uuid)

@app.get("/registration_authority")
def list_registration_authority():
  return RegistrationAuthorityGet.list()

