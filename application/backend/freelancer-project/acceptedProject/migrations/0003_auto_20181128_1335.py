# Generated by Django 2.1.2 on 2018-11-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptedProject', '0002_modelforbackend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptedproject',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
