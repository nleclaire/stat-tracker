# Generated by Django 4.0.2 on 2022-02-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('run_stats', '0002_auto_20211115_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='split',
            name='date',
            field=models.DateField(),
        ),
    ]