# Generated by Django 2.2.1 on 2019-06-07 09:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20190605_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'banner', 'verbose_name_plural': 'banners'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='wikipage',
            options={'verbose_name': 'wiki page', 'verbose_name_plural': 'wiki pages'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='text',
            field=wagtail.core.fields.RichTextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='text_de',
            field=wagtail.core.fields.RichTextField(null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='text_en',
            field=wagtail.core.fields.RichTextField(null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='categorypage',
            name='preview',
            field=models.TextField(blank=True, help_text='Short description of this category', verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='categorypage',
            name='preview_de',
            field=models.TextField(blank=True, help_text='Short description of this category', null=True, verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='categorypage',
            name='preview_en',
            field=models.TextField(blank=True, help_text='Short description of this category', null=True, verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='categorypage',
            name='side_content',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Text displayed in the sidebar of all child pages', verbose_name='sidebar content'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_references', to='personal.Person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.Banner', verbose_name='banner'),
        ),
    ]
