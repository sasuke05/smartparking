# Generated by Django 3.0.4 on 2020-04-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hour',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='minutes',
            field=models.IntegerField(),
        ),
    ]
