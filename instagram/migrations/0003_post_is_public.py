# Generated by Django 4.1.7 on 2023-03-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram", "0002_rename_update_at_post_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_public",
            field=models.BooleanField(default=False, verbose_name="공개여부"),
        ),
    ]
