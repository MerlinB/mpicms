# Generated by Django 2.2.1 on 2019-05-25 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190525_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsentry',
            options={'verbose_name': 'news entry', 'verbose_name_plural': 'news entries'},
        ),
        migrations.AlterModelOptions(
            name='newspage',
            options={'verbose_name': 'news Blog', 'verbose_name_plural': 'news Blogs'},
        ),
    ]