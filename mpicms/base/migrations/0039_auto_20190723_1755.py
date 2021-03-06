# Generated by Django 2.2.2 on 2019-07-23 15:55

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('base', '0038_auto_20190712_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title')),
                ('title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('title_de', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('text', wagtail.core.fields.RichTextField(verbose_name='text')),
                ('text_en', wagtail.core.fields.RichTextField(null=True, verbose_name='text')),
                ('text_de', wagtail.core.fields.RichTextField(null=True, verbose_name='text')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
        migrations.AddField(
            model_name='rootpage',
            name='featured_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.FeaturedImage', verbose_name='featured image'),
        ),
    ]
