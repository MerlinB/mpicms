# Generated by Django 2.1.4 on 2019-03-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Post date'),
        ),
    ]
