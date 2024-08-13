# Generated by Django 5.0.6 on 2024-08-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinginfo",
            name="request_accepted_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Request Sent Date"
            ),
        ),
        migrations.AlterField(
            model_name="bookinginfo",
            name="request_sent_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Request Sent Date"
            ),
        ),
    ]
