# Generated by Django 4.2.2 on 2023-06-22 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_alter_group_id_professor'),
        ('users', '0005_user_id_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
        ),
    ]
