# Generated by Django 4.2.2 on 2023-06-26 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_bulkuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BulkUser',
        ),
    ]
