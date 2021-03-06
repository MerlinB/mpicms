# Generated by Django 2.2.2 on 2019-06-24 10:19

from django.db import migrations, models
import django.db.models.deletion
import mpicms.base.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('base', '0018_auto_20190619_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooserPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(label='Editor')), ('markdown', mpicms.base.blocks.MarkdownBlock(label='Raw Markdown'))])),
                ('body_en', wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(label='Editor')), ('markdown', mpicms.base.blocks.MarkdownBlock(label='Raw Markdown'))], null=True)),
                ('body_de', wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(label='Editor')), ('markdown', mpicms.base.blocks.MarkdownBlock(label='Raw Markdown'))], null=True)),
            ],
            options={
                'verbose_name': 'chooser page',
                'verbose_name_plural': 'chooser pages',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
