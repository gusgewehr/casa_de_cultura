# Generated by Django 4.1.5 on 2023-05-31 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_event_gratuito_alter_event_ingresso_comunitario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdates',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='eventdates',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 22, 53, 34, 688633)),
            preserve_default=False,
        ),
    ]
