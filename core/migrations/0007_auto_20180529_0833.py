# Generated by Django 2.0.4 on 2018-05-29 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180528_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='name',
        ),
    ]
