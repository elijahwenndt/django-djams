# Generated by Django 4.1.3 on 2022-11-17 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_song_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='myapp.genre'),
        ),
    ]
