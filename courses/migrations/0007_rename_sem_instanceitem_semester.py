# Generated by Django 3.2.19 on 2023-09-24 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_instanceitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instanceitem',
            old_name='sem',
            new_name='semester',
        ),
    ]