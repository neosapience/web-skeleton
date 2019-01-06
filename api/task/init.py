from celery import Celery
celery_app = Celery(__name__)
celery_app.config_from_object('app_settings.Config')
