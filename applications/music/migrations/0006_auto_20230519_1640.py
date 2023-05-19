# Generated by Django 2.2.6 on 2023-05-19 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20230519_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackfavorite',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='track_favorites', to='music.Album'),
        ),
        migrations.AddField(
            model_name='trackfavorite',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='track_favorites', to='music.Artist'),
        ),
        migrations.AlterField(
            model_name='trackfavorite',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='track_favorites', to='music.Track'),
        ),
        migrations.AlterUniqueTogether(
            name='trackfavorite',
            unique_together=set(),
        ),
    ]
