# Generated by Django 2.2 on 2020-12-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_auto_20201205_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petfoodmodel',
            old_name='Food_image',
            new_name='food_image',
        ),
        migrations.RenameField(
            model_name='petfoodmodel',
            old_name='Foodname',
            new_name='foodname',
        ),
        migrations.AlterField(
            model_name='pettoymodel',
            name='toy_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]