# Generated by Django 4.2.2 on 2023-06-22 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_group_aprovado_alter_group_id_professor'),
        ('users', '0002_user_id_grupo_alter_user_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
        ),
    ]
