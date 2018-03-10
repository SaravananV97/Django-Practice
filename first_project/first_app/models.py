from django.db import models

# Create your models here.
class Topic(models.Model):
    my_topic_name = models.CharField(max_length = 264,unique = True)

    def __str__(self):
        return self.my_topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    name = models.CharField(max_length = 264,unique = True)
    url = models.URLField(max_length = 264,unique = True)

    def __str__(self):
        return self.name

class AccessRecords(models.Model):
    topic = models.ForeignKey(Webpage,on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
