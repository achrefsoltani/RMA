# Generated by Django 3.2.5 on 2021-07-14 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('criticiteAffaire', models.IntegerField(null=True)),
                ('cid', models.IntegerField(null=True)),
                ('proprietaire', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actifRelation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actif.actif')),
            ],
        ),
        migrations.CreateModel(
            name='TypeActif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActifCritique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncidentsPasse', models.IntegerField(null=True)),
                ('maturite', models.IntegerField(null=True)),
                ('noteRisque', models.IntegerField(null=True)),
                ('actif', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actif.actif')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='session.session')),
            ],
        ),
        migrations.AddField(
            model_name='actif',
            name='typeActif',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actif.typeactif'),
        ),
    ]