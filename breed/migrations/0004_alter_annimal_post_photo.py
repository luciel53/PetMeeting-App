# Generated by Django 4.1.5 on 2023-02-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breed', '0003_alter_annimal_post_age_alter_annimal_post_bloodtype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annimal_post',
            name='photo',
            field=models.ImageField(upload_to='animal.pics'),
        ),
    ]