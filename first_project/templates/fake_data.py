import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")
from first_app.models import AccessRecords,Topic,Webpage
import django,random
django.setup()

topics = ["Calvin","Moguey","Pooch","Lil'Raj","Stephen"]

def topdata():
    t = Topic.objects.get_or_create(my_topic_name = random.choice(topics))[0]
    t.save()
    return t
from faker import Faker
def populate(N = 5):
    for entry in range(N):
        fake_date = fakegen.date()
        fake_url = fakegen.url()
        fake_name = fakegen.company()

    web =  Webpage.objects.get_or_create(topic= topdata(),name = fake_name,url = fake_url)[0]
    web.save()

    access = AccessRecords.objects.get_or_create(topic = topdata(),date = fake_date)[0]

if __name__ == '__main__':
    print("Populating..")
    populate(20)
    print("Populated..!!!!")
