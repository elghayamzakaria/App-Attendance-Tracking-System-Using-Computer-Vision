# Generated by Django 2.2.2 on 2022-07-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190628_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.DateTimeField(null=True),
        ),
    ]
