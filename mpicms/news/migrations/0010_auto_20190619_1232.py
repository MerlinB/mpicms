# Generated by Django 2.2.2 on 2019-06-19 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20190615_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsentry',
            name='preview',
        ),
        migrations.RemoveField(
            model_name='newsentry',
            name='preview_de',
        ),
        migrations.RemoveField(
            model_name='newsentry',
            name='preview_en',
        ),
    ]