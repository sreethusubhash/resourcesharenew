# Generated by Django 4.2.4 on 2023-08-30 08:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="resources",
            options={"verbose_name_plural": "Resources"},
        ),
        migrations.RemoveField(
            model_name="resources",
            name="rate",
        ),
    ]