# Generated by Django 2.2.2 on 2019-07-09 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_auto_20190709_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='postition',
            new_name='position',
        ),
    ]
