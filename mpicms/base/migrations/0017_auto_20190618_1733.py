# Generated by Django 2.2.2 on 2019-06-18 15:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('base', '0016_auto_20190618_1730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryPage',
            new_name='HomePage',
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'homepage', 'verbose_name_plural': 'homepages'},
        ),
    ]
