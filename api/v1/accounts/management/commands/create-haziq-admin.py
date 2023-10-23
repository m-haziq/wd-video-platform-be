from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser with default credentials'

    def handle(self, *args, **kwargs):
        default_email = "m_haziq@outlook.com"
        default_password = "12345678"
        default_username = "m_haziq"

        if User.objects.filter(email=default_email).exists():
            self.stdout.write(self.style.WARNING(f"User '{default_email}' already exists. Skipping creation."))
        else:
            User.objects.create_superuser(username=default_username, email=default_email, password=default_password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{default_email}' created successfully."))
