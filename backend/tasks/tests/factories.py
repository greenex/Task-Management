import factory
from django.utils.timezone import now
from tasks.models import Task
from users.tests.factories import UserFactory
from datetime import timedelta

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Sequence(lambda n: f"Task {n}")
    description = factory.Faker("sentence")
    completed = False
    due_date = factory.LazyFunction(lambda: now() + timedelta(hours=1))
    owner = factory.SubFactory(UserFactory)
