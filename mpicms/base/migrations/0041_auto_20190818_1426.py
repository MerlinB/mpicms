# Generated by Django 2.2.4 on 2019-08-18 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0040_auto_20190723_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rootpage',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wikipage',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
