# Generated by Django 4.1.5 on 2023-02-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breed', '0008_remove_annimal_post_flaws_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='annimal_post',
            name='flaws',
            field=models.TextField(blank=True, default=None, max_length=350),
        ),
    ]
