# Generated by Django 4.2.8 on 2023-12-31 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_projectsectiondetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsectiondetail',
            name='project_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
