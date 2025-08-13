from django.apps import AppConfig
from django.db.models.signals import post_migrate
import os

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'

    def ready(self):
        post_migrate.connect(create_admin_user, sender=self)


def create_admin_user(sender, **kwargs):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

    if not username or not email or not password:
        print("Superuser environment variables not set. Skipping creation.")
        return

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_superuser(username=username, email=email, password=password)
        if hasattr(user, "role"):
            user.role = "admin" # type: ignore  # Custom user model has 'role' field
            user.save()
        print(f"Superuser created with role=admin: username={username}, email={email}")
    else:
        print("Superuser already exists")
