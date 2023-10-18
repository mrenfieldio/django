# Generated by Django 4.2.6 on 2023-10-18 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=2)),
                ('dept', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=10)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.teacher')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.batch')),
            ],
        ),
    ]
