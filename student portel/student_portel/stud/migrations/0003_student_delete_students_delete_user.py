# Generated by Django 4.2.6 on 2023-10-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=25)),
                ('dept', models.CharField(max_length=25)),
                ('program', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='students',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
