# Generated by Django 2.2.2 on 2019-07-12 10:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_auto_20190712_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rootpage',
            name='banner_text',
        ),
        migrations.RemoveField(
            model_name='rootpage',
            name='banner_title',
        ),
        migrations.AddField(
            model_name='rootpage',
            name='banner',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))]))], blank=True),
        ),
    ]
