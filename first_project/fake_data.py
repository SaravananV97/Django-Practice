import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")

import django,random
django.setup()
from first_app.models import Webpage,AccessRecords,Topic
topics = ["Calvin","Moguey","Pooch","Lil'Raj","Stephen"]

def topdata():
    t = Topic.objects.get_or_create(my_topic_name = random.choice(topics))[0]
    t.save()
    return t
from faker import Faker
fake = Faker()
def populate(N):
    for entry in range(N):
        fake_date = fake.date()
        fake_url = fake.url()
        fake_name = fake.company()

        web =  Webpage.objects.get_or_create(topic= topdata(),name = fake_name,url = fake_url)[0]

        access = AccessRecords.objects.get_or_create(topic = web,date = fake_date)[0]

if __name__ == '__main__':
    print("Populating..")
    populate(20)
    print("Populated..!!!!")
