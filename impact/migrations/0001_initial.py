# Generated by Django 3.2.5 on 2021-10-13 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menace', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='impact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('faible', models.CharField(max_length=50, null=True)),
                ('moyen', models.CharField(max_length=50, null=True)),
                ('fort', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='typeImpact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='impactNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_impact', models.IntegerField(null=True)),
                ('note_occurence', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('impact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='impact.impact')),
                ('menace', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='menace.menace')),
            ],
        ),
        migrations.AddField(
            model_name='impact',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='impact.typeimpact'),
        ),
    ]
