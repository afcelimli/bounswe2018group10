# Generated by Django 2.1.2 on 2019-01-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_project_accepted_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemanticSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
            ],
        ),
    ]
