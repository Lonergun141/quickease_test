# Generated by Django 5.0.2 on 2024-08-12 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer_api', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usernotes',
            options={'verbose_name': 'User Note', 'verbose_name_plural': 'User Notes'},
        ),
    ]
