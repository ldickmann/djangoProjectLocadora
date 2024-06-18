# Generated by Django 5.0.6 on 2024-06-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RosaTrip', '0004_remove_trip_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroPendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
    ]
