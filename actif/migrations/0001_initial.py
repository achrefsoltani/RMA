# Generated by Django 3.2.5 on 2021-10-13 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='actif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('criticite_affaire', models.IntegerField(null=True)),
                ('cid', models.IntegerField(null=True)),
                ('proprietaire', models.CharField(max_length=50, null=True)),
                ('intervenant', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actifs_en_relations', models.ManyToManyField(blank=True, null=True, related_name='_actif_actif_actifs_en_relations_+', to='actif.actif')),
            ],
        ),
        migrations.CreateModel(
            name='typeActif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='actifCritique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents', models.IntegerField(null=True)),
                ('maturite', models.IntegerField(null=True)),
                ('note_risque', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actif', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actif.actif')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='session.session')),
            ],
        ),
        migrations.AddField(
            model_name='actif',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actif.typeactif'),
        ),
    ]
