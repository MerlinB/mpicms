# Generated by Django 2.2.2 on 2019-07-23 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('news', '0013_auto_20190624_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsentry',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
