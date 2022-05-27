from argparse import Namespace
from fastapi import FastAPI
from model.namespace import Namespace

VERSION = "0.1"
SYSTEM_NAME = "d4k Registration Authority Microservice"

app = FastAPI()

@app.get("/")
def read_root():
  return {"Version":VERSION, "System": SYSTEM_NAME}

@app.post("/namespace")
async def create_namespace(namespace: Namespace):
  namespace.save
  return namespace.uuid

@app.get("/namespace/{uuid}")
def read_namespace(uuid: str):
  return Namespace.read(uuid)