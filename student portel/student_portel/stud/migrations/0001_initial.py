# Generated by Django 4.2.6 on 2023-10-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=25)),
                ('dept', models.CharField(max_length=25)),
                ('program', models.CharField(max_length=25)),
            ],
        ),
    ]