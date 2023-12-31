# Generated by Django 3.2.9 on 2023-12-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('materials', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('branches', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
            ],
        ),
    ]
