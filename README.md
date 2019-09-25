## build images && test
```
make build
make test
```

## monitoring
* flower for celery
* mongo-express for mongo

## code tree
```
├── .env
├── README.md
├── Makefile
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.test.yml
├── secrets
│   ├── api_secret_dev
│   └── api_secret_live
├── api
│   ├── app
│   │   ├── __init__.py
│   │   └── api
│   │       ├── __init__.py
│   │       ├── api_task.py
│   │       └── bp.py
│   ├── task
│   │   ├── __init__.py
│   │   ├── init.py
│   │   └── mytask.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_app.py
│   ├── Dockerfile
│   ├── Makefile
│   ├── docker-entrypoint.sh
│   ├── requirements.txt
│   ├── app_settings.py
│   └── wsgi.py
└── frontend
    ├── Dockerfile
    ├── Makefile
    ├── app
    │   └── dist
    │       └── index.html
    └── nginx
        ├── conf.d
        │   ├── .app.conf
        │   ├── default.conf
        │   ├── forward-elb-addr.conf
        │   └── forward-https.conf
        └── nginx.conf
```
