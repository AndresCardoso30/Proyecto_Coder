# Generated by Django 4.1.7 on 2023-04-21 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='clave1',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='clave2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='emisor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='mensaje',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='receptor',
            field=models.CharField(max_length=30),
        ),
    ]