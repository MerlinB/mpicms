# Generated by Django 2.2.2 on 2019-06-24 11:50

import mpicms.base.blocks
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190624_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(label='Editor')), ('markdown', mpicms.base.blocks.MarkdownBlock(label='Raw Markdown')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Table'))], blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='body_de',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(label='Editor')), ('markdown', mpicms.base.blocks.MarkdownBlock(label='Raw Markdown')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Table'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='body_en',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(label='Editor')), ('markdown', mpicms.base.blocks.MarkdownBlock(label='Raw Markdown')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Table'))], blank=True, null=True),
        ),
    ]
