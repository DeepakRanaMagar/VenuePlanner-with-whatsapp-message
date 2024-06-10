# Generated by Django 5.0.6 on 2024-06-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_venue_pan_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="venue",
            name="property_type",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Property Type"
            ),
        ),
    ]