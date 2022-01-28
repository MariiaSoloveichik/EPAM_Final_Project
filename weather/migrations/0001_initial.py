# Generated by Django 4.0.1 on 2022-01-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "city_name",
                    models.CharField(max_length=100, verbose_name="City name"),
                ),
                ("date", models.DateField()),
                ("date_year", models.IntegerField(verbose_name="weather year")),
                ("min_temp", models.FloatField(null=True)),
                ("avg_temp", models.FloatField(null=True)),
                ("max_temp", models.FloatField(null=True)),
                ("precip_mm", models.FloatField(blank=True, null=True)),
                ("most_common_weather", models.CharField(max_length=100)),
                ("wind_speed", models.FloatField(blank=True, null=True)),
                ("wind_direction", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
