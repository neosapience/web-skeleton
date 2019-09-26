# kubernetes recipe by kustomize
* https://kustomize.io/
* https://github.com/kubernetes-sigs/kustomize


### Run example

* Prerequisite
  1. Must have kubenetes cluster
  2. Must work kubectl
  3. prepare database


* deploy example app
```bash
$ kubectl apply -k overlays/example
```

## Database
1. setup [kubedb](https://kubedb.com/docs/0.12.0/)
2. run recipes
```
$ kubectl apply -f database/namespace.yaml
$ kubedb create -f database/mgo.yaml
$ kubectl apply -f database/mgo-ui.yaml
```

## Directories

### /app/base
base kustomize recipe

### /app/overlays
example for override kustomize recipe

### /database
mongodb recipe by kubedb
