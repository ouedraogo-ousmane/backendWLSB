# Generated by Django 4.1 on 2022-08-31 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("exercices", "0002_alter_exercices_date_exercice"),
        ("missions", "0003_alter_vehicules_poids_vide"),
    ]

    operations = [
        migrations.CreateModel(
            name="InfosPieces",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("coutUnitaire", models.DecimalField(decimal_places=10, max_digits=19)),
                ("nombre", models.PositiveIntegerField(default=0)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PiecesEchanges",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=250)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mantenances",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("motif", models.TextField()),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("date_maintenance", models.DateTimeField()),
                ("montant", models.DecimalField(decimal_places=5, max_digits=19)),
                (
                    "exerciceConcerne",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="maintenances",
                        to="exercices.exercices",
                    ),
                ),
                (
                    "piecesEchangees",
                    models.ManyToManyField(
                        through="maintenances.InfosPieces",
                        to="maintenances.piecesechanges",
                    ),
                ),
                (
                    "vehiculeConcerne",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="maintenances_effectuees",
                        to="missions.vehiculeparcs",
                    ),
                ),
            ],
            options={"ordering": ["vehiculeConcerne", "-date_creation"],},
        ),
        migrations.AddField(
            model_name="infospieces",
            name="maintenanceConcernee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pieces_enregistrees",
                to="maintenances.mantenances",
            ),
        ),
        migrations.AddField(
            model_name="infospieces",
            name="nomPiece",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="maintenances.piecesechanges",
            ),
        ),
    ]
