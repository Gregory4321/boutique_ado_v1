# Generated by Django 3.1.7 on 2021-03-05 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='street_address1',
            new_name='default_street_address1',
        ),
    ]
