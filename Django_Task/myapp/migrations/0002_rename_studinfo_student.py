# Generated by Django 4.2.5 on 2023-10-02 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='studinfo',
            new_name='student',
        ),
    ]