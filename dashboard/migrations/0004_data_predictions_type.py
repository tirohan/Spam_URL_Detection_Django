# Generated by Django 3.0.14 on 2021-11-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20211101_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='predictions_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
