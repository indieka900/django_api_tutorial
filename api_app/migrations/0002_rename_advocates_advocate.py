# Generated by Django 4.1.2 on 2022-10-29 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advocates',
            new_name='Advocate',
        ),
    ]