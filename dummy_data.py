
import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from django.contrib.auth.models import User
from django.db import models
from faker import Faker
import random
from taggit.managers import TaggableManager
from django.utils import timezone
from todo.models import Tasks  # Adjust this import based on your app structure


import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from todo.models import Tasks
from django.contrib.auth.models import User




def seed_tasks(n):
    fake = Faker()
    users = User.objects.all()

    for _ in range(n):
        Tasks.objects.create(
            user =fake.random_element(users),
            task =fake.text(max_nb_chars=15),
            tags =fake.random_element(elements=('work', 'personal', 'urgent', 'important', 'meeting', 'project')),
            status =fake.random_element(elements=('todo', 'inprogress', 'finished')),
        )

    print(f"Seed {n} Tasks Successfully")

seed_tasks(20)  # Change the number as needed

