# Generated by Django 4.1 on 2022-08-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body_type', models.CharField(max_length=25)),
                ('engine', models.FloatField()),
            ],
        ),
    ]
