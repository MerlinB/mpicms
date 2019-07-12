# Generated by Django 2.2.2 on 2019-07-12 10:38

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20190712_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rootpage',
            name='banner',
        ),
        migrations.AddField(
            model_name='rootpage',
            name='banner_text',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='text'),
        ),
        migrations.AddField(
            model_name='rootpage',
            name='banner_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='title'),
        ),
    ]
