# Generated by Django 3.2.9 on 2021-11-24 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_department_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
    ]
