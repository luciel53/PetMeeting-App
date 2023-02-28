# Generated by Django 4.1.7 on 2023-02-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breed', '0021_alter_annimal_post_bloodtype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annimal_post',
            name='bloodtype',
            field=models.CharField(blank=True, choices=[('1', 'A'), ('2', 'B'), ('3', 'AB'), ('4', 'non renseigné')], default=5, max_length=10, verbose_name='Groupe sanguin'),
        ),
        migrations.AlterField(
            model_name='annimal_post',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('1', 'Bleus'), ('2', 'Verts'), ('3', 'Or'), ('4', 'Vairons'), ('5', 'non renseigné')], default=5, max_length=100, verbose_name='Couleur des yeux'),
        ),
    ]