# Generated by Django 4.1 on 2022-08-31 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exercices", "0001_initial"),
        ("missions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategorieVehicules",
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
                ("intitule", models.CharField(max_length=60, unique=True)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["intitule", "-date_creation"],},
        ),
        migrations.CreateModel(
            name="DepenseMissions",
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
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "intitule",
                    models.CharField(
                        choices=[
                            ("frais de carburant", "frais de carburant"),
                            ("frais de voyage", "frais de voyage"),
                            ("frais de douane", "frais de douane"),
                        ],
                        max_length=250,
                        unique=True,
                    ),
                ),
            ],
            options={"ordering": ["-date_creation"],},
        ),
        migrations.CreateModel(
            name="docsTransports",
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
                ("intitule", models.CharField(choices=[], max_length=250)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("date_expiration", models.DateField()),
            ],
            options={"ordering": ["intitule"],},
        ),
        migrations.CreateModel(
            name="InfoDepenseMissions",
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
                (
                    "montant",
                    models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
                ),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "intitule_depense",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="detail_cout",
                        to="missions.depensemissions",
                    ),
                ),
            ],
            options={"ordering": ["intitule_depense"],},
        ),
        migrations.CreateModel(
            name="LoueurVehicules",
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
                ("prenom", models.CharField(max_length=250, null=True)),
                ("telephone", models.CharField(max_length=20, unique=True)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["nom", "prenom"],},
        ),
        migrations.CreateModel(
            name="Missions",
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
                ("date_mission", models.DateField()),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                ("etat_mission", models.BooleanField(default=False)),
                (
                    "motif",
                    models.CharField(
                        choices=[
                            ("Approvissionement", "Approvissionement"),
                            ("Livraision", "Livraison"),
                        ],
                        default="Approvissionement",
                        max_length=250,
                        unique=True,
                    ),
                ),
                (
                    "exercice_conerne",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="liste_missions",
                        to="exercices.exercices",
                    ),
                ),
                (
                    "liste_depenses",
                    models.ManyToManyField(
                        through="missions.InfoDepenseMissions",
                        to="missions.depensemissions",
                    ),
                ),
            ],
            options={"ordering": ["-date_mission"],},
        ),
        migrations.CreateModel(
            name="Produits",
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
                (
                    "unite",
                    models.CharField(
                        choices=[
                            ("Kg", "kilogramme"),
                            ("tonne", "tonne"),
                            ("tube", "tube"),
                        ],
                        default="Kg",
                        max_length=25,
                    ),
                ),
            ],
            options={"ordering": ["nom"],},
        ),
        migrations.CreateModel(
            name="Recettes",
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
                (
                    "cout_unitaire",
                    models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
                ),
                ("qte_produit", models.PositiveIntegerField(default=1)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-date_creation"],},
        ),
        migrations.CreateModel(
            name="Trajets",
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
                (
                    "ville_depart",
                    models.CharField(
                        choices=[
                            ("Ouaga", "Ouagadougou"),
                            ("Bobo", "Bobo Dioulasso"),
                            ("Bamako", "Bamako"),
                            ("Accra", "Accra"),
                        ],
                        default="Bobo",
                        max_length=50,
                    ),
                ),
                (
                    "ville_arrivee",
                    models.CharField(
                        choices=[
                            ("Ouaga", "Ouagadougou"),
                            ("Bobo", "Bobo Dioulasso"),
                            ("Bamako", "Bamako"),
                            ("Accra", "Accra"),
                        ],
                        default="Bobo",
                        max_length=50,
                    ),
                ),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-date_creation"],},
        ),
        migrations.CreateModel(
            name="Vehicules",
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
                ("immat", models.CharField(max_length=250, unique=True)),
                ("marque", models.CharField(max_length=60, null=True)),
                ("couleur", models.CharField(max_length=60, null=True)),
                ("est_disponible", models.BooleanField(default=True)),
                ("poids_vide", models.DecimalField(decimal_places=3, max_digits=5)),
                (
                    "categorie",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="vehicules",
                        to="missions.categorievehicules",
                    ),
                ),
            ],
            options={"ordering": ["immat"],},
        ),
        migrations.AlterField(
            model_name="clients",
            name="telephone",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name="RecetteDetailPesage",
            fields=[
                (
                    "recettes_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="missions.recettes",
                    ),
                ),
                (
                    "premier_pese",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "deuxieme_pese",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
            ],
            bases=("missions.recettes",),
        ),
        migrations.CreateModel(
            name="RecetteDetailSansPesage",
            fields=[
                (
                    "recettes_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="missions.recettes",
                    ),
                ),
            ],
            bases=("missions.recettes",),
        ),
        migrations.CreateModel(
            name="VehiculeParcs",
            fields=[
                (
                    "vehicules_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="missions.vehicules",
                    ),
                ),
            ],
            bases=("missions.vehicules",),
        ),
        migrations.AddField(
            model_name="recettes",
            name="client_concerne",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_recette",
                to="missions.clients",
            ),
        ),
        migrations.AddField(
            model_name="recettes",
            name="mission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_recette",
                to="missions.missions",
            ),
        ),
        migrations.AddField(
            model_name="recettes",
            name="produit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_recette",
                to="missions.produits",
            ),
        ),
        migrations.AddField(
            model_name="missions",
            name="liste_produits",
            field=models.ManyToManyField(
                through="missions.Recettes", to="missions.produits"
            ),
        ),
        migrations.AddField(
            model_name="missions",
            name="trajet_concerne",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="liste_missions",
                to="missions.trajets",
            ),
        ),
        migrations.AddField(
            model_name="missions",
            name="vehicule_concerne",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="liste_missions",
                to="missions.vehicules",
            ),
        ),
        migrations.AddField(
            model_name="infodepensemissions",
            name="mission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_depenses",
                to="missions.missions",
            ),
        ),
        migrations.CreateModel(
            name="VehiculeLoues",
            fields=[
                (
                    "vehicules_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="missions.vehicules",
                    ),
                ),
                (
                    "proprietaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicules",
                        to="missions.loueurvehicules",
                    ),
                ),
            ],
            bases=("missions.vehicules",),
        ),
        migrations.CreateModel(
            name="documentVehicules",
            fields=[
                (
                    "docstransports_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="missions.docstransports",
                    ),
                ),
                (
                    "vehicule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="infos_documents",
                        to="missions.vehiculeparcs",
                    ),
                ),
            ],
            bases=("missions.docstransports",),
        ),
        migrations.CreateModel(
            name="Chauffeurs",
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
                ("prenom", models.CharField(max_length=250)),
                ("telephone", models.CharField(max_length=20)),
                (
                    "salaire",
                    models.DecimalField(decimal_places=10, default=0.0, max_digits=19),
                ),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "vehicule",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="chauffeur",
                        to="missions.vehiculeparcs",
                    ),
                ),
            ],
            options={"ordering": ["nom", "prenom"],},
        ),
    ]