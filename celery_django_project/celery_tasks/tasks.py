from celery import shared_task
# from celery_tasks.models import Student_data

@shared_task(bind=True)
def add_data(self, x, y):
    print(f"{x} + {y} = {x+y}")
    # instance1 = Student_data(regno='A1234', name='John Doe', marks=85.5, gender='M')
    # instance1.save()
    return f"Success...{x+y}"

@shared_task(bind=True)
def sub_data(self, x, y):
    print(f"{x} - {y} = {x-y}")
    # instance2 = Student_data(regno='B5678', name='Jane Smith', marks=75.0, gender='F')
    # instance2.save()
    return f"Success...{x-y}"

@shared_task(bind=True)
def mul_data(self, x, y):
    print(f"{x} * {y} = {x*y}")
    # instance3 = Student_data(regno='C91011', name='Alice Johnson', marks=92.3, gender='F')
    # instance3.save()
    return f"Success...{x*y}"