# Generated by Django 2.2.1 on 2019-05-28 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_contacts_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikipage',
            name='date',
        ),
    ]
