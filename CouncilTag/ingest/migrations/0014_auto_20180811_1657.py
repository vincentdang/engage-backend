# Generated by Django 2.0.7 on 2018-08-11 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0013_auto_20180811_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='ethnicity',
        ),
        migrations.DeleteModel(
            name='Ethnicity',
        ),
    ]
