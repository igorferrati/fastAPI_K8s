# FastAPI in Kubenertes :snake:

## FastAPI consome a API do Kubernetes

Criação de um servidor que lista namespace de um cluster com topologia:

* Aplicação lista, deleta e cria namespaces dentro do cluster kubernetes do qual ela for implantada
* Vunicorn como servidor HTTP 
* Cluster Role / Service Account para acesso para aplicação
* Implantação via helm
---

:file_folder: wsgi
* chart helm

:file_folder: dockerfile
* .dockerignore
* Dockerfile
* index.html
* main.py
* requirements.txt

---

## Config vunigorn

Ao montar o container, executamos o vunicorn para expôr nossa aplicação:
``` ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] ```


## Dockerfile

* Imagem python 3.9
* O build da imagem cria as dependências necessárias a partir do requirements.txt
* O comando ```pip install -r requirements.txt``` instala as dependências
* É utilizado o [Kubernetes Python Client](https://github.com/kubernetes-client/python) API para consumir recursos do cluster

### Index.html

* O html utiliza a biblioteca Axios para realizar solicitações em HTTP.

* Temos uma página html (front) que possuí uma lógica de mapemaneto para as funções python do fastAPI (backend).


## ServiceAccount / ClusterRole / ClusterRoleBinding

* A aplicação deve possuir acesso para listar, deletar e criar os namespaces.

Para acesso do cluster do qual deseja rodar a imagem é necessário criar uma RBAC de acesso e vincular um serviceaccount ao tipo de permissão desejada.

* No helm temos o seguinte exemplo, partindo do principio que já temos um namespace em questão para a aplicação e devemos víncular o helm a um namespace:

``` helm install <release> <chart-name> -n <namespace>```

* Este namespace já prédefinido deve estar no ClusterRoleBinding

```
clusterrolebind:
  name: sa-get-ns
  subjects:
  - kind: ServiceAccount
    name: get-app-desafio     #name sa
    namespace: app-desafio
  roleRef:
    kind: ClusterRole
    name: get-namespaces      #name role
    apiGroup: rbac.authorization.k8s.io
```


