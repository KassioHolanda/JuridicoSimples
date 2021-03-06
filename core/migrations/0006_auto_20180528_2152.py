# Generated by Django 2.0.4 on 2018-05-29 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_news_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='theme',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_theme', to='core.Theme'),
        ),
    ]
