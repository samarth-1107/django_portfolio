# Generated by Django 4.2.8 on 2023-12-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_servicesectiondetail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesectiondetail',
            name='descreption',
            field=models.CharField(max_length=500),
        ),
    ]
