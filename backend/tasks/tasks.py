from celery import shared_task, group
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from .models import Task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def send_single_task_reminder(task_id):
    """
    Send reminder for a single tasks.
    """

    logger.info("Sending reminder for task %s", task_id)
    task = Task.objects.get(id=task_id)
    send_mail(
        subject="Task Reminder",
        message=f"Reminder: Your tasks '{task.name}' is due soon!",
        from_email="noreply@yourapp.com",
        recipient_list=[task.owner.email],
    )
    return f"Reminder sent for tasks: {task_id}"

@shared_task
def send_task_reminder():
    """
    Split large tasks sets into smaller sub-tasks using Celery's `group`.
    """
    logger.info("Start send_task_reminder");
    upcoming_tasks = Task.objects.filter(
        completed=False,
        due_date__lte=now() + timedelta(minutes=30),
        due_date__gte=now()
    ).values_list("id", flat=True)

    if not upcoming_tasks:
        # Handle the case where no tasks are found
        return

    task_chunks = group(send_single_task_reminder.s(task_id) for task_id in upcoming_tasks)
    task_chunks.apply_async()

    return f"Dispatched {len(upcoming_tasks)} tasks reminders."

@shared_task
def delete_old_completed_tasks():
    """
    Delete tasks that have been completed and not updated for more than 1 day.
    """
    cutoff_time = now() - timedelta(days=1)
    logger.info(
        f"Deleting Old completed tasks since {cutoff_time}"
    )
    deleted_count, _ = Task.objects.filter(
        completed=True,
        updated_at__lt=cutoff_time  #  Only delete if last update was over 1 day ago
    ).delete()

    return f"Deleted {deleted_count} old completed tasks."