# Generated by Django 3.2.23 on 2023-12-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='guys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pictures')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
