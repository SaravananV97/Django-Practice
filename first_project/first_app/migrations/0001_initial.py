# Generated by Django 2.0.2 on 2018-02-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_topic_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
