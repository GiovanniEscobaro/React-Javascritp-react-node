# Generated by Django 5.2.3 on 2025-06-20 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_rename_nombres_project_nombre"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tareas",
            old_name="Project_id",
            new_name="Project",
        ),
    ]
