# Generated by Django 3.2.9 on 2021-12-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0005_paper_paper_most_used_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='paper_molecule',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_patients',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
