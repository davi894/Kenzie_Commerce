# Generated by Django 4.0.7 on 2023-03-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Realizado', 'Default'), ('Em andamento', 'In Progress'), ('Entregue', 'Delivered')], default='Realizado', max_length=20)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
