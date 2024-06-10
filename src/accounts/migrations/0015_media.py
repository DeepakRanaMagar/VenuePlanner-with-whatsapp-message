# Generated by Django 5.0.6 on 2024-06-10 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_venue_issubscribed_venue_photo2_venue_social1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Media",
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
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/subscription/",
                        verbose_name="Subscription photo",
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="videos/subscription/",
                        verbose_name="Subscription video",
                    ),
                ),
                (
                    "venue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.venue",
                        verbose_name="venue",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media",
                "verbose_name_plural": "Medias",
                "managed": True,
            },
        ),
    ]
