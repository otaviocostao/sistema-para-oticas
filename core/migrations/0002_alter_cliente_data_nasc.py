# Generated by Django 5.0.4 on 2024-04-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nasc',
            field=models.DateField(),
        ),
    ]
