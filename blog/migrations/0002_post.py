# Generated by Django 4.2.5 on 2023-09-28 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("text", models.TextField()),
                ("image", models.ImageField(upload_to="postsimages/")),
                (
                    "index_title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.index"
                    ),
                ),
            ],
        ),
    ]
