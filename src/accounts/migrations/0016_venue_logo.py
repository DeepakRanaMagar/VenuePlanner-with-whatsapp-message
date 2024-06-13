# Generated by Django 5.0.6 on 2024-06-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_media"),
    ]

    operations = [
        migrations.AddField(
            model_name="venue",
            name="logo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/logo",
                verbose_name="Venue logo",
            ),
        ),
    ]
