# Generated by Django 2.2.2 on 2019-07-12 11:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_auto_20190712_1314'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AlterField(
            model_name='rootpage',
            name='footer_items',
            field=wagtail.core.fields.StreamField([('menu', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title')), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title')), ('url', wagtail.core.blocks.URLBlock(label='URL'))], label='Items')))], icon='list-ul', label='Menu'))], blank=True, verbose_name='Footer Items'),
        ),
        migrations.AlterField(
            model_name='rootpage',
            name='footer_items_de',
            field=wagtail.core.fields.StreamField([('menu', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title')), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title')), ('url', wagtail.core.blocks.URLBlock(label='URL'))], label='Items')))], icon='list-ul', label='Menu'))], blank=True, null=True, verbose_name='Footer Items'),
        ),
        migrations.AlterField(
            model_name='rootpage',
            name='footer_items_en',
            field=wagtail.core.fields.StreamField([('menu', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title')), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title')), ('url', wagtail.core.blocks.URLBlock(label='URL'))], label='Items')))], icon='list-ul', label='Menu'))], blank=True, null=True, verbose_name='Footer Items'),
        ),
    ]