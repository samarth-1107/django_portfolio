# Generated by Django 4.2.8 on 2024-01-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=15)),
                ('personal_link_icon', models.CharField(max_length=20)),
                ('personal_links', models.CharField(max_length=50)),
            ],
        ),
    ]
