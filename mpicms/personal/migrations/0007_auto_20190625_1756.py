# Generated by Django 2.2.2 on 2019-06-25 15:56

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20190625_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactgroups',
            name='contact',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='personal.Contact'),
        ),
        migrations.AlterField(
            model_name='contactgroups',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='personal.Group', verbose_name='groups'),
        ),
    ]
