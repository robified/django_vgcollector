# Generated by Django 2.2.5 on 2019-09-16 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190916_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playtime',
            old_name='Videogame',
            new_name='videogame',
        ),
    ]