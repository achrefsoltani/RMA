# Generated by Django 3.2.5 on 2021-10-13 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actif', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='menace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('HR', 'Acteur Humain & Access réseau'), ('HP', 'Acteur Humain & Access physique'), ('PS', 'Problèmes systèmes'), ('AP', 'Autres Problèmes')], max_length=50, null=True)),
                ('reference', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('access', models.CharField(max_length=50, null=True)),
                ('acteur', models.CharField(max_length=50, null=True)),
                ('motivation', models.CharField(max_length=50, null=True)),
                ('resultat', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actif', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actif.actifcritique')),
            ],
        ),
    ]
