# Generated by Django 4.2 on 2023-04-22 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='foydalanuvchi',
        ),
    ]