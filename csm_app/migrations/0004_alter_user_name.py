# Generated by Django 3.2 on 2023-08-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csm_app', '0003_remove_posts_is_public_posts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
