from django.apps import AppConfig


class NewappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newapp'


    def ready(self):
        import newapp.signals

red = redis.Redis(
    host='redis-16974.c258.us-east-1-4.ec2.cloud.redislabs.com',
    port=16974,
    password='SLltAfLjaeIah58aXZBP6rICl6g60J2N'
)