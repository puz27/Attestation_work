from django.core.management import BaseCommand
from users.models import Users


def create_user(email: str, is_superuser: bool, is_staff: bool, is_active: bool, password: str) -> None:
    user_check = Users.objects.filter(email=email)
    if not user_check:
        user = Users.objects.create(
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active
        )

        user.set_password(password)
        user.save()


# Load users to base
class Command(BaseCommand):

    def handle(self, *args, **options):
        create_user("admin@gmail.com", True, True, True, "admin")
        create_user("test1@gmail.com", False, False, True, "test1")
        create_user("test2@gmail.com", False, False, False, "test2")
