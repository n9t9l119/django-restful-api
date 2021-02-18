# Generated by Django 3.1.6 on 2021-02-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geonameid', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=64)),
                ('asciiname', models.CharField(max_length=64)),
                ('alternatenames', models.CharField(max_length=256)),
                ('latitude', models.CharField(max_length=64)),
                ('longitude', models.CharField(max_length=256)),
                ('feature_class', models.CharField(max_length=1)),
                ('feature_code', models.CharField(max_length=10)),
                ('country_code', models.CharField(max_length=2)),
                ('cc2', models.CharField(max_length=200)),
                ('admin1_code', models.CharField(max_length=20)),
                ('admin2_code', models.CharField(max_length=80)),
                ('admin3_code', models.CharField(max_length=20)),
                ('admin4_code', models.CharField(max_length=20)),
                ('population', models.IntegerField()),
                ('elevation', models.IntegerField(null=True)),
                ('dem', models.IntegerField()),
                ('modification_date', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Timezones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=2)),
                ('timezone_id', models.CharField(max_length=64)),
                ('gmt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='NameId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=384)),
                ('geonameid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geonames.geonames')),
            ],
        ),
        migrations.AddField(
            model_name='geonames',
            name='timezone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geonames.timezones'),
        ),
    ]