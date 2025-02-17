# Generated by Django 4.2.19 on 2025-02-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tail_number', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('production_year', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
