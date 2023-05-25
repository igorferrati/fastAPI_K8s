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


@app.post("/namespaces/create")    #localhost:8000/namespaces/create/novo-ns
def create_namespace(name: str):

    metadata = client.V1ObjectMeta(name=name)
    body = client.V1Namespace(metadata=metadata)
    k8s_api.create_namespace(body)
    


@app.delete("/namespaces/delete/{name}")
def delete_namespace(name: str):

    k8s_api.delete_namespace(name)
    