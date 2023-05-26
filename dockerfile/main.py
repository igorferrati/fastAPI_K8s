from fastapi import FastAPI
from fastapi.responses import FileResponse
from kubernetes import client, config

app = FastAPI()
config.load_incluster_config()
k8s_api = client.CoreV1Api()

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/namespaces")
def list_namespaces():

    namespaces = k8s_api.list_namespace().items
    return {"namespaces": [ns.metadata.name for ns in namespaces]}


@app.post("/create")
def create_namespace(name: str):
    new_namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=name))
    k8s_api.create_namespace(new_namespace)
    

@app.delete("/delete/{name}")
def delete_namespace(name: str):

    k8s_api.delete_namespace(name)
    