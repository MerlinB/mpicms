# Generated by Django 2.2.4 on 2019-09-02 08:59

from django.db import migrations, models
import django.db.models.deletion
import mpicms.personal.models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0023_auto_20190729_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='position',
        ),
        migrations.CreateModel(
            name='ContactPositions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('contact', mpicms.personal.models.FilterableParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='personal.Contact')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='personal.Position', verbose_name='positions')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
