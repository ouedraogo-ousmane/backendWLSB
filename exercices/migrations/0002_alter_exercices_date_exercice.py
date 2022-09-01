# Generated by Django 4.1 on 2022-08-31 17:42

from django.db import migrations, models
import exercices.validators


class Migration(migrations.Migration):

    dependencies = [
        ("exercices", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercices",
            name="date_exercice",
            field=models.DateTimeField(
                validators=[exercices.validators.no_TwoExercices]
            ),
        ),
    ]
