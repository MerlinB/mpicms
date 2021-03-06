# Generated by Django 2.2.2 on 2019-07-03 15:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_auto_20190703_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sidebar_de',
            field=wagtail.core.fields.StreamField([('Editor', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'h6', 'bold', 'italic', 'link', 'document-link'])), ('Contacts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('contact', wagtail.snippets.blocks.SnippetChooserBlock('personal.Contact', label='Contact')), ('information', wagtail.core.blocks.TextBlock(required=False))]), icon='user'))], blank=True, null=True, verbose_name='sidebar content'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sidebar_en',
            field=wagtail.core.fields.StreamField([('Editor', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'h6', 'bold', 'italic', 'link', 'document-link'])), ('Contacts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('contact', wagtail.snippets.blocks.SnippetChooserBlock('personal.Contact', label='Contact')), ('information', wagtail.core.blocks.TextBlock(required=False))]), icon='user'))], blank=True, null=True, verbose_name='sidebar content'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.core.fields.StreamField([('Editor', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'h6', 'bold', 'italic', 'link', 'document-link'])), ('Contacts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('contact', wagtail.snippets.blocks.SnippetChooserBlock('personal.Contact', label='Contact')), ('information', wagtail.core.blocks.TextBlock(required=False))]), icon='user'))], blank=True, verbose_name='sidebar content'),
        ),
    ]
