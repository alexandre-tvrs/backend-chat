# Generated by Django 4.2.2 on 2023-06-22 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_grupo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipo_usuario',
            field=models.IntegerField(choices=[(1, 'Aluno'), (2, 'Professor')], default=1),
        ),
    ]
