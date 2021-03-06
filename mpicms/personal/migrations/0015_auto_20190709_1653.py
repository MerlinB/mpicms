# Generated by Django 2.2.2 on 2019-07-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0014_contact_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='contact',
            name='postition',
            field=models.CharField(blank=True, max_length=255, verbose_name='position'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=5, verbose_name='title'),
        ),
    ]
