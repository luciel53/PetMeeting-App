# Generated by Django 4.1.5 on 2023-02-15 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breed', '0010_annimal_post_qualities_alter_annimal_post_flaws'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annimal_post',
            name='flaws',
        ),
    ]
