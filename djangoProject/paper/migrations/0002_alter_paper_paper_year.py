# Generated by Django 3.2.9 on 2021-11-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='paper_year',
            field=models.CharField(max_length=30),
        ),
    ]