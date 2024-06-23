# Generated by Django 5.0.6 on 2024-06-23 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
