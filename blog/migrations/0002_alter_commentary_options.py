# Generated by Django 4.1 on 2024-01-14 01:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={
                "ordering": ["-created_time"],
                "verbose_name": "commentary",
                "verbose_name_plural": "commentaries",
            },
        ),
    ]