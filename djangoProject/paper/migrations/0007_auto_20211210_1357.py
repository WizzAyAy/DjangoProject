# Generated by Django 3.2.9 on 2021-12-10 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0006_auto_20211210_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='paper_molecule',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='paper_patients',
        ),
    ]
