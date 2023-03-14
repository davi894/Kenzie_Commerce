# Generated by Django 4.0.7 on 2023-03-14 13:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('zip_code', models.CharField(max_length=8)),
                ('street', models.CharField(max_length=127)),
                ('number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=127)),
            ],
        ),
    ]
