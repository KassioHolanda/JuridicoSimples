# Generated by Django 2.0.4 on 2018-05-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180528_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='resume',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
