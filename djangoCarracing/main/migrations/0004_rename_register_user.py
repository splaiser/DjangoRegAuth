# Generated by Django 3.2.5 on 2021-07-25 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_lemodele'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='User',
        ),
    ]