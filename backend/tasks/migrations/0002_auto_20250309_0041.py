from django_celery_beat.models import IntervalSchedule, PeriodicTask
from django.db import migrations

def add_periodic_tasks(apps, schema_editor):
    # Create an Interval Schedule if it doesn’t exist (e.g., every day)
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES,
    )

    # Add a periodic task using that schedule
    PeriodicTask.objects.get_or_create(
        name='Delete Old Completed Tasks',
        task='tasks.tasks.delete_old_completed_tasks',
        defaults={'interval': schedule}
    )

    PeriodicTask.objects.get_or_create(
        name='Run Task Reminder',
        task='tasks.tasks.send_task_reminder',
        defaults={'interval': schedule}
    )

class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0001_initial'),  # Adjust based on your actual migration dependency
    ]

    operations = [
        migrations.RunPython(add_periodic_tasks),
    ]

