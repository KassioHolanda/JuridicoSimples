# Generated by Django 2.0.4 on 2018-05-31 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180531_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='resume',
            field=models.CharField(max_length=80, null=True, verbose_name='Resumo'),
        ),
    ]