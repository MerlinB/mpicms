# Generated by Django 2.2.2 on 2019-06-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20190613_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='phone number'),
            preserve_default=False,
        ),
    ]
