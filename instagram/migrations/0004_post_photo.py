# Generated by Django 4.1.7 on 2023-03-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram", "0003_post_is_public"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="photo",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]