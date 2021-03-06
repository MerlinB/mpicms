# Generated by Django 2.2.4 on 2019-09-05 09:19

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=wagtail.core.fields.RichTextField(verbose_name='authors'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='groups',
            field=wagtail.core.fields.RichTextField(verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='source',
            field=wagtail.core.fields.RichTextField(verbose_name='source'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=wagtail.core.fields.RichTextField(verbose_name='title'),
        ),
    ]
