# Generated by Django 4.0.4 on 2022-06-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoUniApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vegetal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
