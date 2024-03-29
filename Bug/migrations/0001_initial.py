# Generated by Django 4.2.6 on 2023-10-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bug",
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
                ("description", models.TextField()),
                (
                    "bug_type",
                    models.CharField(
                        choices=[
                            ("error", "Error"),
                            ("feature", "New Feature"),
                            ("enhancement", "Enhancement"),
                            ("other", "Other"),
                        ],
                        default="error",
                        max_length=30,
                    ),
                ),
                ("report_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("todo", "To Do"),
                            ("inprogress", "In Progress"),
                            ("done", "Done"),
                        ],
                        default="todo",
                        max_length=30,
                    ),
                ),
            ],
        ),
    ]
