import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","leveltwo.settings")
import django
django.setup()
from my_app.models import User
from faker import Faker
fake = Faker()
def populate(N = 20):
    for usr in range(N):
        Name = fake.name()
        Name = Name.split(' ')
        fake_first_name,fake_last_name = Name[0],Name[1]
        fake_email = fake.email()

        usr = User.objects.get_or_create(first_name = fake_first_name,last_name = fake_last_name,email = fake_email)


if __name__ == '__main__':
    print("Populating...")
    populate()
    print("Populated...!")
