# Generated by Django 3.2.5 on 2021-07-25 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_user_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='client',
            new_name='auth_user',
        ),
    ]
