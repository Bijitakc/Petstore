# Generated by Django 2.2 on 2020-12-05 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_auto_20201205_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petfoodmodel',
            options={'verbose_name_plural': 'petfoodposts'},
        ),
        migrations.AlterModelOptions(
            name='pettoymodel',
            options={'verbose_name_plural': 'pettoyposts'},
        ),
    ]
