

## code tree
```
├── .env
├── README.md
├── Makefile
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── secrets
│   ├── api_secret_dev
│   └── api_secret_live
├── api
│   ├── Dockerfile
│   ├── Makefile
│   ├── app
│   │   ├── __init__.py
│   │   ├── api_task.py
│   │   ├── core.py
│   │   └── settings.py
│   ├── task
│   │   ├── __init__.py
│   │   └── mytask.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_app.py
│   ├── docker-entrypoint.sh
│   ├── manage.py
│   ├── requirements.txt
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
