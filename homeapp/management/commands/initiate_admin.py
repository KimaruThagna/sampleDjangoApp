from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os
from django.conf import settings
from dotenv import load_dotenv

env_path = os.path.join(settings.BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)


class Command(BaseCommand):
# create a superuser
    def handle(self, *args, **options):
        User.objects.all().delete()
        print('Creating superuser admin account')
        if not User.objects.all().exists():
            User.objects.create_superuser(email="mail@admin.com",
                                      username="admin1",
                                      password="testuserpass")
        else:
            print("Admin already exists")