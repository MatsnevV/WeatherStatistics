"""
from celery import Celery
from celery.schedules import crontab
from WebApp import create_app

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def cat_reminder():
    with flask_app():
        return f"Мяу, хозяин, чёт скучно. Может посмотришь погоду на другой день?"

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), cat_reminder.s())

<br></br>
   {{ reminder }}

"""
