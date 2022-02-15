# Generated by Django 3.0.7 on 2020-06-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csoport', models.CharField(max_length=200)),
                ('kontakt_szemely', models.CharField(max_length=200)),
                ('cim', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=20)),
                ('datum', models.DateField()),
                ('ido', models.TimeField()),
                ('fizetve', models.BooleanField()),
                ('letrehozva', models.DateField(blank=True, null=True)),
                ('modositva', models.DateField(blank=True, null=True)),
                ('szolgaltatasok', models.CharField(max_length=255)),
                ('jegy', models.IntegerField()),
                ('megjegyzes', models.TextField()),
            ],
        ),
    ]