# Generated by Django 4.0.6 on 2022-07-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(default='Kenya', max_length=225),
        ),
    ]
