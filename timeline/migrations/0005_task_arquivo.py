# Generated by Django 4.2.2 on 2023-06-29 03:58

from django.db import migrations, models
import timeline.models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_rename_entrege_task_entregue'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to=timeline.models.upload_arquive_task),
        ),
    ]
