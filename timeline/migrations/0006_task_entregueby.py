# Generated by Django 4.2.2 on 2023-06-29 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_user_id_grupo'),
        ('timeline', '0005_task_arquivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='entregueBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='users.user'),
        ),
    ]
