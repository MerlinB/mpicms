# Generated by Django 2.2.1 on 2019-05-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='phone number'),
        ),
    ]
