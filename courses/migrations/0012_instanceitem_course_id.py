# Generated by Django 3.2.19 on 2023-09-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_instanceitem_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='instanceitem',
            name='course_id',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
