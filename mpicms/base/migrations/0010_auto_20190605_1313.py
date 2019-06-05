# Generated by Django 2.2.1 on 2019-06-05 11:13

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20190605_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('text', wagtail.core.fields.RichTextField()),
                ('text_en', wagtail.core.fields.RichTextField(null=True)),
                ('text_de', wagtail.core.fields.RichTextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.Banner'),
        ),
    ]
