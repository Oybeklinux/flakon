# Generated by Django 4.0.3 on 2022-06-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_bottles_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottles',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bottles',
            name='neck_diameter',
            field=models.FloatField(blank=True, null=True),
        ),
    ]