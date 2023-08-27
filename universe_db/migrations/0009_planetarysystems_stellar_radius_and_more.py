# Generated by Django 4.2.2 on 2023-07-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("universe_db", "0008_merge_20230720_1948"),
    ]

    operations = [
        migrations.AddField(
            model_name="planetarysystems",
            name="stellar_radius",
            field=models.FloatField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name="planetarysystems",
            unique_together={("name", "hostname", "discovery_year")},
        ),
    ]
