# Generated by Django 4.2.2 on 2023-06-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_task_entregueby'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comentario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]