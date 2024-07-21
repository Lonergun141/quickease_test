# Generated by Django 5.0.2 on 2024-07-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notetitle', models.CharField(max_length=30, verbose_name='Note Title')),
                ('notecontents', models.TextField(verbose_name='Note Contents')),
                ('notedatecreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
