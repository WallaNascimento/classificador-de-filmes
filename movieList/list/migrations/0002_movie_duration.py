# Generated by Django 5.0.2 on 2024-03-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]