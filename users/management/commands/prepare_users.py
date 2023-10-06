from django.core.management import BaseCommand
from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_check_1 = Users.objects.filter(email="admin@gmail.com")
        if not user_check_1:
            user = Users.objects.create(
                email="admin@gmail.com",
                is_superuser=True,
                is_staff=True,
                is_active=True
                )

            user.set_password("admin")
            user.save()

        user_check_2 = Users.objects.filter(email="test@gmail.com")
        if not user_check_2:
            user = Users.objects.create(
                email="test@gmail.com",
                is_superuser=False,
                is_staff=False,
                is_active=True
            )

            user.set_password("test")
            user.save()

        user_check_3 = Users.objects.filter(email="test2@gmail.com")
        if not user_check_3:
            user = Users.objects.create(
                email="test2@gmail.com",
                is_superuser=False,
                is_staff=False,
                is_active=False
            )

            user.set_password("test2")
            user.save()
