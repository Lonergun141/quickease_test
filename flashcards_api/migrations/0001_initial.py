# Generated by Django 5.0.2 on 2024-08-27 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('summarizer_api', '0003_alter_usernotes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFlashCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frontCardText', models.CharField(default='', max_length=100, verbose_name='Front Card Text')),
                ('backCardText', models.CharField(default='', max_length=100, verbose_name='Back Card Text')),
                ('noteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summarizer_api.usernotes')),
            ],
            options={
                'verbose_name': 'User FlashCard',
                'verbose_name_plural': 'User FlashCards',
            },
        ),
    ]
