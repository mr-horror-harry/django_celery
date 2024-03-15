from celery import shared_task

@shared_task(bind=True)
def add_data(self, x, y):
    print(f"{x} + {y} = {x+y}")
    return f"Success...{x+y}"
    