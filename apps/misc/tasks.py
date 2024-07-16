from celery import shared_task


@shared_task
def task_dummy(a, b):
    print('Called tast_dummy with a:%s b:%s' % (a, b))
