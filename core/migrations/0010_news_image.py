# Generated by Django 2.0.4 on 2018-05-30 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180529_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.FileField(default=1, upload_to='media/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
