# Generated by Django 5.1.3 on 2024-11-15 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
    ]
