# Generated by Django 4.2.6 on 2023-10-24 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Video",
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
                ("url", models.URLField(max_length=500)),
                ("title", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "tags",
                    models.ManyToManyField(related_name="videos", to="videos.tag"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ratings",
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
                    "rating",
                    models.FloatField(
                        choices=[
                            (0.0, "ZERO"),
                            (0.5, "HALF"),
                            (1.0, "ONE"),
                            (1.5, "ONE_AND_A_HALF"),
                            (2.0, "TWO"),
                            (2.5, "TWO_AND_A_HALF"),
                            (3.0, "THREE"),
                            (3.5, "THREE_AND_A_HALF"),
                            (4.0, "FOUR"),
                            (4.5, "FOUR_AND_A_HALF"),
                            (5.0, "FIVE"),
                        ],
                        default=0.0,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to="videos.video",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Dashboard",
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
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "videos",
                    models.ManyToManyField(
                        related_name="dashboards", to="videos.video"
                    ),
                ),
            ],
        ),
    ]
