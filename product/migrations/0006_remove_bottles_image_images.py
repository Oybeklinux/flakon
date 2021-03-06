# Generated by Django 4.0.3 on 2022-06-29 20:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_bottles_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottles',
            name='image',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(default='default.png', upload_to='bottles')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bottle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.bottles')),
            ],
        ),
    ]
