# Generated by Django 3.2.3 on 2021-10-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actif', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actif',
            name='intervenants',
            field=models.CharField(max_length=50, null=True),
        ),
    ]